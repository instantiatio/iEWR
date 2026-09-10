"""P: bounded POSIX fixture IO. No permission, Method, or scheduling decisions."""
from contextlib import contextmanager
from hashlib import sha256
import fcntl
import json
import os
from pathlib import Path, PurePosixPath
import stat
import uuid
from modules.effects.api import Boundary, Observation, Receipt


MAX_BYTES = 1024 * 1024


def parts_of(relative):
    if not isinstance(relative, str) or not relative or "\\" in relative or "\x00" in relative:
        raise ValueError("unsafe_path")
    path = PurePosixPath(relative)
    if path.is_absolute() or any(p in ("", ".", "..") for p in relative.split("/")):
        raise ValueError("unsafe_path")
    return path.parts


def directory_at(parent, name):
    return os.open(name, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=parent)


def read_at(parent, name):
    fd = os.open(name, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK, dir_fd=parent)
    try:
        info = os.fstat(fd)
        if not stat.S_ISREG(info.st_mode) or info.st_nlink != 1 or info.st_size > MAX_BYTES:
            raise ValueError("unsafe_file_or_byte_budget")
        chunks = bytearray()
        while True:
            chunk = os.read(fd, min(65536, MAX_BYTES + 1 - len(chunks)))
            if not chunk:
                break
            chunks.extend(chunk)
            if len(chunks) > MAX_BYTES:
                raise ValueError("byte_budget_exceeded")
        return bytes(chunks), info
    finally:
        os.close(fd)


class Tree:
    def __init__(self, root: Path, allowed_parent: Path):
        root, allowed_parent = Path(root).absolute(), Path(allowed_parent).absolute()
        if root.parent != allowed_parent or root == allowed_parent:
            raise ValueError("workspace_outside_fixture_boundary")
        # Open every absolute component without following aliases/symlinks.
        fd = os.open("/", os.O_RDONLY | os.O_DIRECTORY)
        try:
            for part in root.parts[1:]:
                child = directory_at(fd, part)
                os.close(fd)
                fd = child
        except BaseException:
            os.close(fd)
            raise
        self.fd, self.root = fd, root

    def close(self):
        if self.fd is not None:
            os.close(self.fd)
            self.fd = None

    @contextmanager
    def parent(self, relative):
        parts = parts_of(relative)
        fd = os.dup(self.fd)
        try:
            for part in parts[:-1]:
                child = directory_at(fd, part)
                os.close(fd)
                fd = child
            yield fd, parts[-1]
        finally:
            os.close(fd)

    def read(self, relative):
        with self.parent(relative) as (parent, name):
            return read_at(parent, name)[0]

    def ensure_owner_directory(self, owner, namespace="state"):
        if owner not in ("execution", "effects", "governance", "reliance", "interaction"):
            raise ValueError("unsupported_store_owner")
        if namespace not in ("state", "project/process/ewr"):
            raise ValueError("unsupported_owner_namespace")
        fd = os.dup(self.fd)
        try:
            for part in (*namespace.split("/"), owner):
                try:
                    os.mkdir(part, 0o700, dir_fd=fd)
                    os.fsync(fd)
                except FileExistsError:
                    pass
                child = directory_at(fd, part)
                os.close(fd)
                fd = child
        finally:
            os.close(fd)

    def current_parent(self, relative, pinned):
        # Detect a relocated/replaced workspace or ancestor before commit.
        try:
            fresh = Tree(self.root, self.root.parent)
            try:
                if not os.path.samestat(os.fstat(fresh.fd), os.fstat(self.fd)):
                    return False
                with fresh.parent(relative) as (again, _):
                    return os.path.samestat(os.fstat(again), os.fstat(pinned))
            finally:
                fresh.close()
        except OSError:
            return False

    def replace(self, relative, before: bytes | None, after: bytes, guard=lambda: True, hook=lambda stage: None):
        if len(after) > MAX_BYTES:
            raise ValueError("byte_budget_exceeded")
        with self.parent(relative) as (parent, name):
            fcntl.flock(parent, fcntl.LOCK_EX | fcntl.LOCK_NB)
            temporary = ".b1-" + uuid.uuid4().hex
            made = False
            try:
                try:
                    current, info = read_at(parent, name)
                except FileNotFoundError:
                    current, info = None, None
                if current != before:
                    raise ValueError("input_bytes_changed")
                fd = os.open(temporary, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW,
                             stat.S_IMODE(info.st_mode) if info else 0o600, dir_fd=parent)
                made = True
                try:
                    remaining = memoryview(after)
                    while remaining:
                        written = os.write(fd, remaining)
                        if written <= 0:
                            raise OSError("incomplete_write")
                        remaining = remaining[written:]
                    os.fsync(fd)
                finally:
                    os.close(fd)
                hook("before_replace")
                if not self.current_parent(relative, parent):
                    raise ValueError("directory_binding_changed")
                try:
                    latest, latest_info = read_at(parent, name)
                except FileNotFoundError:
                    latest, latest_info = None, None
                if latest != before or ((info is None) != (latest_info is None)):
                    raise ValueError("input_bytes_changed")
                if info is not None and not os.path.samestat(info, latest_info):
                    raise ValueError("target_binding_changed")
                if not guard():
                    raise ValueError("decision_changed_before_commit")
                os.replace(temporary, name, src_dir_fd=parent, dst_dir_fd=parent)
                made = False
                hook("after_replace")
                os.fsync(parent)
                observed, _ = read_at(parent, name)
                if observed != after:
                    raise OSError("post_write_readback_mismatch")
                hook("before_receipt")
                return observed
            finally:
                if made:
                    os.unlink(temporary, dir_fd=parent)
                fcntl.flock(parent, fcntl.LOCK_UN)


class LocalEffects:
    def __init__(self, tree: Tree, hook=lambda stage: None, supported=True):
        self.tree, self.hook, self.supported = tree, hook, supported
        self.target_effects = 0

    def boundary(self):
        return Boundary("compensated" if self.supported else "unsupported",
                        "b1-posix-single-writer-v1",
                        "no-follow + directory flock + precommit compare; single cooperative writer; no hostile-writer atomic CAS")

    def observe(self, target):
        try:
            if parts_of(target)[:2] not in (("project", "artifacts"), ("project", "handoff")):
                raise ValueError("unsafe_target_scope")
            return Observation(target, self.tree.read(target))
        except (OSError, ValueError) as error:
            return Observation(target, None, "unsafe_or_unreadable_path: " + str(error))

    def replace(self, scope, guard):
        committed = False

        def hook(stage):
            nonlocal committed
            if stage == "after_replace":
                committed = True
                self.target_effects += 1
            self.hook(stage)

        try:
            if parts_of(scope.target)[:2] not in (("project", "artifacts"), ("project", "handoff")):
                raise ValueError("unsafe_target_scope")
            output = self.tree.replace(scope.target, scope.before.encode("utf-8"), scope.after.encode("utf-8"), guard, hook)
            return Receipt(scope.target, "applied", "readback_matches_requested_bytes", sha256(output).hexdigest(), 1,
                           "represented_in_result")
        except (OSError, ValueError) as error:
            return Receipt(scope.target, "unknown" if committed else "not_performed", str(error), None,
                           None if committed else 0, "dependent_use_blocked" if committed else "no_target_effect")


class OwnerStore:
    """Each instance writes one consumer-owned namespace, never a shared domain DB."""
    def __init__(self, tree: Tree, owner: str, namespace="state"):
        if owner not in ("execution", "effects", "governance", "reliance", "interaction"):
            raise ValueError("unsupported_store_owner")
        if namespace not in ("state", "project/process/ewr"):
            raise ValueError("unsupported_owner_namespace")
        self.tree, self.owner, self.namespace = tree, owner, namespace

    def locus(self, key):
        if len(key) != 64 or any(c not in "0123456789abcdef" for c in key):
            raise ValueError("invalid_record_locator")
        return f"{self.namespace}/{self.owner}/{key}.json"

    def decode(self, raw):
        obj = json.loads(raw)
        if obj.get("schema") != 1 or obj.get("owner") != self.owner or not isinstance(obj.get("record"), dict):
            raise ValueError("unsupported_owner_record")
        return obj["record"]

    def read(self, key):
        try:
            return self.decode(self.tree.read(self.locus(key)))
        except FileNotFoundError:
            return None

    def write(self, key, value, previous):
        self.tree.ensure_owner_directory(self.owner, self.namespace)
        path = self.locus(key)
        try:
            old = self.tree.read(path)
        except FileNotFoundError:
            old = None
        observed = self.decode(old) if old is not None else None
        if json.dumps(observed, sort_keys=True, allow_nan=False) != json.dumps(previous, sort_keys=True, allow_nan=False):
            raise ValueError("owner_revision_conflict")
        data = json.dumps({"schema": 1, "owner": self.owner, "record": value}, ensure_ascii=False, sort_keys=True).encode("utf-8")
        self.tree.replace(path, old, data)

    def snapshot(self):
        try:
            with self.tree.parent(f"{self.namespace}/{self.owner}/probe") as (parent, _):
                names = os.listdir(parent)
                if len(names) > 1000:
                    raise ValueError("owner_record_budget")
                result = []
                for name in sorted(names):
                    if name.startswith(".b1-"):
                        raise ValueError("unreconciled_owner_temporary")
                    key = name.removesuffix(".json")
                    if name != key + ".json":
                        raise ValueError("unsupported_owner_path")
                    self.locus(key)
                    record = self.decode(read_at(parent, name)[0])
                    result.append((key, json.dumps(record, ensure_ascii=False, sort_keys=True)))
                return tuple(result)
        except FileNotFoundError:
            return ()
