#!/usr/bin/env python3
"""Bounded local DPF byte inventory and discoverability, Python 3.10+ / POSIX.

REPERTOIRE.yaml is the JSON subset of YAML 1.2, not arbitrary YAML. Downloaded
content is data: no script execution, archive extraction, network access, source
edits, applicability decisions, or automatic edition selection occur here.

Security boundary: descriptor-relative O_NOFOLLOW reads, bounded inventories,
before/after identity checks, cooperative directory flock, atomic replacement,
fsync and post-write source reconciliation. This is not a sandbox against a
hostile same-user process or filesystem administrator. Locks are advisory;
external readers/writers must honour the same convention. A digest describes an
observed snapshot, not a permanent capability or permission to use its claims.
"""

from __future__ import annotations

import argparse
from contextlib import contextmanager
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import stat
import sys
import unicodedata
import uuid

try:
    import fcntl
except ImportError:  # No silent fallback to weaker Windows controls.
    fcntl = None


SCHEMA_VERSION = "1.0"
INDEX_NAME = "REPERTOIRE.yaml"
SCOPE_ROOTS = {"package": "frameworks/dpf", "project": "project/dpf"}
MAX_FILES = 10000
MAX_DEPTH = 24
MAX_FILE_BYTES = 32 * 1024 * 1024
MAX_TOTAL_BYTES = 128 * 1024 * 1024
MAX_INDEX_BYTES = 4 * 1024 * 1024
MAX_ENTRIES = 1000
METADATA_FIELDS = {"source_id", "display_name", "aliases", "edition_id", "normative_loci",
                   "declared_status", "publication_locator", "fpf_grounding_claim"}
ENTRY_FIELDS = METADATA_FIELDS | {"scope", "source_locus", "files", "edition_manifest_sha256",
                                  "registered_at", "registration_basis",
                                  "source_bytes_modified_by_registration"}
PACKAGE_FIELDS = {"required_slot", "distribution_basis"}
HEX = re.compile(r"^[0-9a-f]{64}$")
IDENTIFIER = re.compile(r"^[a-z0-9][a-z0-9._-]{0,127}$")


class RepertoireError(Exception):
    """Named failure; effects names any material write that already occurred."""

    def __init__(self, code, message, effects=None):
        super().__init__(message)
        self.code = code
        self.effects = effects or {"repertoire_written": False, "source_bytes_modified": False}


def _fail(code, message):
    raise RepertoireError(code, message)


def _text(value, name, allow_empty=False):
    if not isinstance(value, str) or (not value and not allow_empty):
        _fail("invalid_metadata", f"{name} must be an explicit string")
    if len(value) > 8192 or any(unicodedata.category(c).startswith("C") for c in value):
        _fail("invalid_metadata", f"{name} contains control characters or exceeds its budget")
    return value


def _collision_key(value):
    return unicodedata.normalize("NFC", value).casefold()


def _name(name):
    if (not isinstance(name, str) or name in ("", ".", "..") or
            any(c in name for c in '/\\\t\r\n') or
            any(unicodedata.category(c).startswith("C") for c in name) or
            len(name.encode("utf-8")) > 255):
        _fail("unsafe_path", f"Unsafe path component: {name!r}")
    return name


def _relative(locus):
    if not isinstance(locus, str) or locus.startswith("/") or not locus:
        _fail("unsafe_path", "Expected a nonempty repository-relative path")
    parts = locus.split("/")
    for part in parts:
        _name(part)
    if len(parts) > MAX_DEPTH + 8:
        _fail("budget_exceeded", "Path exceeds depth budget")
    return parts


def _source_path(locus, scope):
    if scope not in SCOPE_ROOTS:
        _fail("invalid_scope", "Scope must be package or project")
    _relative(locus)
    prefix = SCOPE_ROOTS[scope] + "/"
    if not locus.startswith(prefix) or locus == prefix + INDEX_NAME:
        _fail("unsafe_path", "Source must be below the scope root, not the repertoire itself")
    return locus


def _signature(info):
    return (info.st_dev, info.st_ino, info.st_mode, info.st_size,
            info.st_mtime_ns, info.st_ctime_ns)


def _names(fd):
    names = os.listdir(fd)
    if len(names) > MAX_FILES * 2:
        _fail("budget_exceeded", "Directory entry count exceeds budget")
    seen = set()
    for name in names:
        _name(name)
        key = _collision_key(name)
        if key in seen:
            _fail("path_collision", "Case/NFC-colliding directory entries")
        seen.add(key)
    return sorted(names)


def _directory_child(fd, name):
    _name(name)
    if name not in _names(fd):
        _fail("missing_path", f"Exact directory component is absent: {name}")
    before = os.stat(name, dir_fd=fd, follow_symlinks=False)
    if not stat.S_ISDIR(before.st_mode):
        _fail("unsafe_path", f"Not a plain directory (symlinks prohibited): {name}")
    child = os.open(name, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=fd)
    after = os.fstat(child)
    if (before.st_dev, before.st_ino) != (after.st_dev, after.st_ino):
        os.close(child)
        _fail("source_changed", "Directory changed while opening")
    return child


@contextmanager
def _root_fd(root):
    if os.name != "posix" or fcntl is None or not all(
            hasattr(os, n) for n in ("O_DIRECTORY", "O_NOFOLLOW", "O_NONBLOCK")):
        _fail("unsupported_platform", "This beta requires POSIX descriptor controls and flock")
    raw = os.fspath(root)
    if not isinstance(raw, str):
        _fail("unsafe_path", "Root must be a text path")
    absolute = raw if raw.startswith("/") else os.getcwd() + "/" + raw
    parts = absolute.split("/")[1:]
    if any(p in (".", "..") for p in parts):
        _fail("unsafe_path", "Root cannot contain dot or parent components")
    fd = os.open("/", os.O_RDONLY | os.O_DIRECTORY)
    try:
        for part in parts:
            if not part:  # Trailing slash is harmless; source loci stay strict.
                continue
            child = _directory_child(fd, part)
            os.close(fd)
            fd = child
        yield fd
    except OSError as exc:
        raise RepertoireError("filesystem_error", str(exc)) from exc
    finally:
        os.close(fd)


@contextmanager
def _directory(rootfd, parts):
    fd = os.dup(rootfd)
    try:
        for part in parts:
            child = _directory_child(fd, part)
            os.close(fd)
            fd = child
        yield fd
    finally:
        os.close(fd)


def _read_file(fd, name, limit=MAX_FILE_BYTES, exact_name_observed=False):
    _name(name)
    if not exact_name_observed and name not in _names(fd):
        _fail("missing_path", f"Exact file component is absent: {name}")
    before = os.stat(name, dir_fd=fd, follow_symlinks=False)
    if not stat.S_ISREG(before.st_mode):
        _fail("unsafe_path", f"Only regular files are supported: {name}")
    if before.st_size > limit:
        _fail("budget_exceeded", f"File exceeds byte budget: {name}")
    filefd = os.open(name, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK, dir_fd=fd)
    try:
        start = os.fstat(filefd)
        if _signature(start) != _signature(before):
            _fail("source_changed", f"File changed while opening: {name}")
        chunks, size = [], 0
        while True:
            chunk = os.read(filefd, 1024 * 1024)
            if not chunk:
                break
            size += len(chunk)
            if size > limit:
                _fail("budget_exceeded", f"File grew beyond byte budget: {name}")
            chunks.append(chunk)
        end = os.fstat(filefd)
        named = os.stat(name, dir_fd=fd, follow_symlinks=False)
        if _signature(start) != _signature(end) or _signature(end) != _signature(named):
            _fail("source_changed", f"File changed while reading: {name}")
        return b"".join(chunks)
    finally:
        os.close(filefd)


def _read_locus(rootfd, locus, limit=MAX_FILE_BYTES):
    parts = _relative(locus)
    with _directory(rootfd, parts[:-1]) as fd:
        return _read_file(fd, parts[-1], limit)


def _inventory_directory(fd, prefix="", depth=0, budget=None):
    if budget is None:
        budget = [0, 0, 0]
    if depth > MAX_DEPTH:
        _fail("budget_exceeded", "Source tree exceeds depth budget")
    before = _signature(os.fstat(fd))
    names = _names(fd)
    records = []
    for name in names:
        budget[2] += 1
        if budget[2] > MAX_FILES * 2:
            _fail("budget_exceeded", "Source tree exceeds total directory-entry budget")
        relative = prefix + name
        info = os.stat(name, dir_fd=fd, follow_symlinks=False)
        if stat.S_ISDIR(info.st_mode):
            child = _directory_child(fd, name)
            try:
                records.extend(_inventory_directory(child, relative + "/", depth + 1, budget))
            finally:
                os.close(child)
        elif stat.S_ISREG(info.st_mode):
            budget[0] += 1
            if budget[0] > MAX_FILES:
                _fail("budget_exceeded", "Source tree exceeds file-count budget")
            content = _read_file(fd, name, exact_name_observed=True)
            budget[1] += len(content)
            if budget[1] > MAX_TOTAL_BYTES:
                _fail("budget_exceeded", "Source tree exceeds total-byte budget")
            records.append({"path": relative, "sha256": hashlib.sha256(content).hexdigest()})
        else:
            _fail("unsafe_path", f"Symlink or special file in source: {relative}")
    if names != _names(fd) or before != _signature(os.fstat(fd)):
        _fail("source_changed", "Directory changed during inventory")
    return sorted(records, key=lambda item: item["path"])


def _digest(files, single):
    if single:
        return files[0]["sha256"]
    manifest = "".join(f'{item["path"]}\t{item["sha256"]}\n' for item in files)
    return hashlib.sha256(manifest.encode("utf-8")).hexdigest()


def inspect_source(root, locus, scope="project"):
    """Observe a local source. Metadata or normative claims are never inferred."""
    _source_path(locus, scope)
    parts = _relative(locus)
    with _root_fd(root) as rootfd, _directory(rootfd, parts[:-1]) as parent:
        if parts[-1] not in _names(parent):
            _fail("missing_path", f"Source not found: {locus}")
        info = os.stat(parts[-1], dir_fd=parent, follow_symlinks=False)
        single = stat.S_ISREG(info.st_mode)
        if single:
            content = _read_file(parent, parts[-1])
            files = [{"path": parts[-1], "sha256": hashlib.sha256(content).hexdigest()}]
        elif stat.S_ISDIR(info.st_mode):
            fd = _directory_child(parent, parts[-1])
            try:
                files = _inventory_directory(fd)
            finally:
                os.close(fd)
            if not files:
                _fail("empty_source", "An empty directory is not a registered source edition")
        else:
            _fail("unsafe_path", "Source is a symlink or special file")
    return {"status": "inspected", "scope": scope, "source_locus": locus,
            "source_kind": "file" if single else "directory", "files": files,
            "edition_manifest_sha256": _digest(files, single)}


def _unique_object(pairs):
    obj = {}
    for key, value in pairs:
        if key in obj:
            _fail("corrupt_index", f"Duplicate JSON object key: {key}")
        obj[key] = value
    return obj


def _decode_json(raw):
    try:
        return json.loads(raw.decode("utf-8"), object_pairs_hook=_unique_object,
                          parse_constant=lambda value: _fail("corrupt_index", f"Invalid JSON: {value}"))
    except (UnicodeError, ValueError, RecursionError) as exc:
        raise RepertoireError("corrupt_index", "Expected strict UTF-8 JSON (YAML 1.2 subset)") from exc


def _claim(value, name):
    if not isinstance(value, dict) or set(value) != {"value", "locus"}:
        _fail("invalid_metadata", f"{name} must contain value and locus")
    _text(value["value"], name + ".value")
    _text(value["locus"], name + ".locus")


def _validate_metadata(metadata):
    if not isinstance(metadata, dict) or set(metadata) != METADATA_FIELDS:
        _fail("invalid_metadata", "Supply exactly the documented explicit metadata fields")
    for name in ("source_id", "edition_id"):
        if not isinstance(metadata[name], str) or not IDENTIFIER.fullmatch(metadata[name]):
            _fail("invalid_metadata", f"{name} must be a lowercase ASCII identity, max 128 characters")
    _text(metadata["display_name"], "display_name")
    _text(metadata["publication_locator"], "publication_locator")
    for name in ("aliases", "normative_loci"):
        if not isinstance(metadata[name], list) or len(metadata[name]) > 1000:
            _fail("invalid_metadata", f"{name} must be a bounded list")
        for value in metadata[name]:
            _text(value, name)
        if len(set(metadata[name])) != len(metadata[name]):
            _fail("invalid_metadata", f"Duplicate {name}")
    if not metadata["normative_loci"]:
        _fail("invalid_metadata", "At least one explicit normative locus is required")
    _claim(metadata["declared_status"], "declared_status")
    _claim(metadata["fpf_grounding_claim"], "fpf_grounding_claim")


def _entry_file_loci(entry):
    locus = entry["source_locus"]
    # File-vs-directory is inferred only from the recorded paths. On binding it
    # is checked against an actual observed inventory, never an extension guess.
    basename = locus.rsplit("/", 1)[-1]
    if len(entry["files"]) == 1 and entry["files"][0]["path"] == basename:
        return {locus, locus + "/" + basename}
    return {locus + "/" + item["path"] for item in entry["files"]}


def _check_claim_loci(entry, observation):
    loci = ({entry["source_locus"]} if observation["source_kind"] == "file" else
            {entry["source_locus"] + "/" + item["path"] for item in observation["files"]})
    for locus in entry["normative_loci"] + [entry["declared_status"]["locus"],
                                           entry["fpf_grounding_claim"]["locus"]]:
        if locus.split("#", 1)[0] not in loci:
            _fail("invalid_metadata", "Claim locus is not an actual observed source file")


def _validate_entry(entry, scope):
    if not isinstance(entry, dict):
        _fail("corrupt_index", "Entry must be an object")
    allowed = ENTRY_FIELDS | (PACKAGE_FIELDS if scope == "package" else set())
    if not ENTRY_FIELDS <= set(entry) or set(entry) - allowed:
        _fail("corrupt_index", "Missing or unsupported entry fields")
    _validate_metadata({key: entry[key] for key in METADATA_FIELDS})
    if entry["scope"] != scope or entry["source_bytes_modified_by_registration"] is not False:
        _fail("corrupt_index", "Scope/source-mutation declaration is invalid")
    _source_path(entry["source_locus"], scope)
    if not isinstance(entry["files"], list) or not 1 <= len(entry["files"]) <= MAX_FILES:
        _fail("corrupt_index", "Invalid file inventory")
    seen, paths, components = set(), [], {}
    for item in entry["files"]:
        if not isinstance(item, dict) or set(item) != {"path", "sha256"}:
            _fail("corrupt_index", "Invalid inventory record")
        _relative(item["path"])
        if not isinstance(item["sha256"], str) or not HEX.fullmatch(item["sha256"]):
            _fail("corrupt_index", "Invalid file digest")
        key = _collision_key(item["path"])
        if key in seen:
            _fail("path_collision", "Duplicate/case/NFC-colliding inventory paths")
        seen.add(key)
        paths.append(item["path"])
        segments = item["path"].split("/")
        for depth, segment in enumerate(segments):
            parent = _collision_key("/".join(segments[:depth]))
            component_key = (parent, _collision_key(segment))
            previous = components.setdefault(component_key, segment)
            if previous != segment:
                _fail("path_collision", "Case/NFC-colliding inventory directory components")
    if paths != sorted(paths):
        _fail("corrupt_index", "Inventory paths must be lexicographically sorted")
    path_set = set(paths)
    if any(any("/".join(path.split("/")[:depth]) in path_set
                   for depth in range(1, len(path.split("/")))) for path in paths):
        _fail("corrupt_index", "Inventory path is both file and directory")
    digest = entry["edition_manifest_sha256"]
    if not isinstance(digest, str) or not HEX.fullmatch(digest):
        _fail("corrupt_index", "Invalid edition digest")
    if digest not in {_digest(entry["files"], False),
                      _digest(entry["files"], True) if len(entry["files"]) == 1 else ""}:
        _fail("corrupt_index", "Edition digest does not match the recorded inventory")
    loci = _entry_file_loci(entry)
    for locus in entry["normative_loci"] + [entry["declared_status"]["locus"],
                                           entry["fpf_grounding_claim"]["locus"]]:
        path = locus.split("#", 1)[0]
        _relative(path)
        if path not in loci:
            _fail("invalid_metadata", "Source claim/normative locus is outside its recorded files")
    _text(entry["registration_basis"], "registration_basis")
    try:
        timestamp = datetime.fromisoformat(entry["registered_at"].replace("Z", "+00:00"))
        if timestamp.tzinfo is None:
            raise ValueError("timezone required")
    except (AttributeError, TypeError, ValueError) as exc:
        raise RepertoireError("corrupt_index", "registered_at must be an RFC-3339 timezone timestamp") from exc
    if "required_slot" in entry:
        _text(entry["required_slot"], "required_slot")
    if "distribution_basis" in entry:
        basis = entry["distribution_basis"]
        if not isinstance(basis, dict) or set(basis) != {"status", "statement", "locus"}:
            _fail("corrupt_index", "distribution_basis requires status, statement and locus")
        if basis["status"] not in ("confirmed", "user_reported_pending_confirmation",
                                   "project_authored_local_trial_only", "unresolved"):
            _fail("corrupt_index", "Unknown distribution-basis status")
        _text(basis["statement"], "distribution_basis.statement")
        _text(basis["locus"], "distribution_basis.locus")


def _load_index(fd, scope):
    names = _names(fd)
    if any(_collision_key(name) == _collision_key(INDEX_NAME) and name != INDEX_NAME for name in names):
        _fail("path_collision", "Repertoire filename has non-exact case/NFC spelling")
    if INDEX_NAME not in names:
        return {"schema_version": SCHEMA_VERSION, "scope": scope, "entries": []}, None
    raw = _read_file(fd, INDEX_NAME, MAX_INDEX_BYTES)
    value = _decode_json(raw)
    if (not isinstance(value, dict) or set(value) != {"schema_version", "scope", "entries"} or
            value["schema_version"] != SCHEMA_VERSION or value["scope"] != scope or
            not isinstance(value["entries"], list) or len(value["entries"]) > MAX_ENTRIES):
        _fail("corrupt_index", "Invalid repertoire schema")
    seen = set()
    for entry in value["entries"]:
        _validate_entry(entry, scope)
        identity = (entry["source_id"], entry["edition_id"])
        if identity in seen:
            _fail("corrupt_index", "Duplicate source identity/edition")
        seen.add(identity)
    return value, raw


def _scope_index(root, scope, missing_ok=True):
    with _root_fd(root) as rootfd:
        try:
            with _directory(rootfd, SCOPE_ROOTS[scope].split("/")) as fd:
                return _load_index(fd, scope)
        except RepertoireError as exc:
            if missing_ok and exc.code == "missing_path":
                return {"schema_version": SCHEMA_VERSION, "scope": scope, "entries": []}, None
            raise


def list_repertoire(root, scope="both"):
    if scope not in ("both", "package", "project"):
        _fail("invalid_scope", "Scope must be both, package or project")
    entries, missing = [], []
    for current in ("package", "project") if scope == "both" else (scope,):
        index, raw = _scope_index(root, current)
        entries.extend(index["entries"])
        if raw is None:
            missing.append(SCOPE_ROOTS[current] + "/" + INDEX_NAME)
    return {"status": "listed", "entries": entries, "missing_indexes": missing,
            "limit": "Availability only; order is not precedence and bindings are not verified by listing."}


def _find_entry(index, source_id, edition_id):
    return next((e for e in index["entries"] if
                 (e["source_id"], e["edition_id"]) == (source_id, edition_id)), None)


def _same_observation(entry, observed):
    return all(entry[key] == observed[key] for key in
               ("source_locus", "files", "edition_manifest_sha256"))


def verify_binding(root, scope, source_id, edition_id, expected_digest=None):
    if scope not in SCOPE_ROOTS:
        _fail("invalid_scope", "Scope must be package or project")
    index, _ = _scope_index(root, scope)
    entry = _find_entry(index, source_id, edition_id)
    if entry is None:
        _fail("not_registered", "Exact source identity/edition is not registered")
    if expected_digest is not None and entry["edition_manifest_sha256"] != expected_digest:
        _fail("stale_binding", "Requested digest differs from the registered edition")
    observation = inspect_source(root, entry["source_locus"], scope)
    if not _same_observation(entry, observation):
        _fail("stale_binding", "Source bytes no longer match the registered edition")
    _check_claim_loci(entry, observation)
    return {"status": "verified", "entry": entry, "observation": observation,
            "limit": "Exact byte observation only, not source applicability, safety, truth or permission."}


@contextmanager
def _project_lock(root):
    with _root_fd(root) as rootfd, _directory(rootfd, ["project", "dpf"]) as fd:
        try:
            fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except OSError as exc:
            raise RepertoireError("repertoire_busy", "Another cooperative writer holds the repertoire lock") from exc
        try:
            yield fd
        finally:
            fcntl.flock(fd, fcntl.LOCK_UN)


def _check_project_directory_binding(root, locked_fd):
    with _root_fd(root) as rootfd, _directory(rootfd, ["project", "dpf"]) as current:
        before, after = os.fstat(locked_fd), os.fstat(current)
        if (before.st_dev, before.st_ino) != (after.st_dev, after.st_ino):
            _fail("concurrent_directory_change", "Project repertoire directory was replaced; reconcile before continuing")


def _write_index(fd, previous, index):
    """Atomic cooperative update. Any after-replace error explicitly names it."""
    payload = (json.dumps(index, ensure_ascii=False, indent=2, allow_nan=False) + "\n").encode("utf-8")
    if len(payload) > MAX_INDEX_BYTES:
        _fail("budget_exceeded", "Resulting repertoire exceeds index-byte budget")
    temporary = ".iewr-repertoire-" + uuid.uuid4().hex + ".tmp"
    replaced = False
    temp_created = False
    try:
        tempfd = os.open(temporary, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW,
                         0o600, dir_fd=fd)
        temp_created = True
        try:
            remaining = memoryview(payload)
            while remaining:
                remaining = remaining[os.write(tempfd, remaining):]
            os.fsync(tempfd)
        finally:
            os.close(tempfd)
        _, current = _load_index(fd, "project")
        if current != previous:
            _fail("concurrent_index_change", "Index changed since read; no replacement performed")
        os.replace(temporary, INDEX_NAME, src_dir_fd=fd, dst_dir_fd=fd)
        replaced = True
        temp_created = False
        os.fsync(fd)
        _, reread = _load_index(fd, "project")
        if reread != payload:
            _fail("postwrite_index_mismatch", "Written index was changed or could not be recovered exactly")
    except (OSError, RepertoireError) as exc:
        error = exc if isinstance(exc, RepertoireError) else RepertoireError("filesystem_error", str(exc))
        error.effects = {"repertoire_written": replaced, "source_bytes_modified": False,
                         "repertoire_locus": "project/dpf/REPERTOIRE.yaml"}
        raise error
    finally:
        if temp_created:
            try:
                os.unlink(temporary, dir_fd=fd)
            except OSError as exc:
                raise RepertoireError("temporary_cleanup_failed", str(exc),
                                      {"repertoire_written": replaced, "source_bytes_modified": False,
                                       "unresolved_temporary_locus": "project/dpf/" + temporary}) from exc


def register(root, locus, metadata, registration_basis, expected_digest=None, commit_guard=None):
    _validate_metadata(metadata)
    _text(registration_basis, "registration_basis")
    _source_path(locus, "project")
    with _project_lock(root) as fd:
        index, raw = _load_index(fd, "project")
        observation = inspect_source(root, locus)
        if expected_digest is not None and observation["edition_manifest_sha256"] != expected_digest:
            _fail("source_changed", "Selected source differs from the intended binding")
        existing = _find_entry(index, metadata["source_id"], metadata["edition_id"])
        if existing is not None:
            if existing["edition_manifest_sha256"] != observation["edition_manifest_sha256"]:
                _fail("identity_content_collision", "Same identity/edition has different bytes; preserve both bases")
            # Matching bytes at a second path do not silently relocate the old binding.
            if not _same_observation(existing, inspect_source(root, existing["source_locus"])):
                _fail("stale_binding", "Existing registered locus is stale; no silent rebinding")
            return {"status": "already_registered", "entry": existing,
                    "effects": {"repertoire_written": False, "source_bytes_modified": False}}
        if len(index["entries"]) >= MAX_ENTRIES:
            _fail("budget_exceeded", "Repertoire exceeds entry-count budget")
        entry = {**metadata, "scope": "project", "source_locus": locus,
                 "files": observation["files"], "edition_manifest_sha256": observation["edition_manifest_sha256"],
                 "registered_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
                 "registration_basis": registration_basis,
                 "source_bytes_modified_by_registration": False}
        _validate_entry(entry, "project")
        _check_claim_loci(entry, observation)
        if not _same_observation(entry, inspect_source(root, locus)):
            _fail("source_changed", "Source changed before registration; nothing was written")
        index["entries"].append(entry)
        index["entries"].sort(key=lambda e: (e["source_id"], e["edition_id"]))
        _check_project_directory_binding(root, fd)
        if commit_guard is not None and not commit_guard():
            _fail("current_basis_changed", "Current governance/configuration no longer supports this effect")
        _write_index(fd, raw, index)
        try:
            _check_project_directory_binding(root, fd)
            if not _same_observation(entry, inspect_source(root, locus)):
                _fail("source_changed", "Source changed after registration")
        except RepertoireError as exc:
            exc.effects = {"repertoire_written": True, "source_bytes_modified": False,
                           "repertoire_locus": "project/dpf/REPERTOIRE.yaml",
                           "entry_identity": [entry["source_id"], entry["edition_id"]],
                           "dependent_use_blocked": True}
            raise
        return {"status": "registered", "entry": entry,
                "effects": {"repertoire_written": True, "source_bytes_modified": False,
                            "repertoire_locus": "project/dpf/REPERTOIRE.yaml"},
                "limit": "Discoverable source candidate only; no source authority or applicability is granted."}


def unregister(root, source_id, edition_id, registration_basis, commit_guard=None):
    _text(registration_basis, "registration_basis")
    with _project_lock(root) as fd:
        index, raw = _load_index(fd, "project")
        entry = _find_entry(index, source_id, edition_id)
        if entry is None:
            return {"status": "not_registered", "effects": {
                "repertoire_written": False, "source_bytes_modified": False}}
        index["entries"] = [e for e in index["entries"] if e is not entry]
        _check_project_directory_binding(root, fd)
        if commit_guard is not None and not commit_guard():
            _fail("current_basis_changed", "Current governance/configuration no longer supports this effect")
        _write_index(fd, raw, index)
        try:
            _check_project_directory_binding(root, fd)
        except RepertoireError as exc:
            exc.effects = {"repertoire_written": True, "source_bytes_modified": False,
                           "repertoire_locus": "project/dpf/REPERTOIRE.yaml",
                           "dependent_use_blocked": True}
            raise
        return {"status": "unregistered", "removed_entry": entry,
                "registration_basis": registration_basis,
                "effects": {"repertoire_written": True, "source_bytes_modified": False,
                            "repertoire_locus": "project/dpf/REPERTOIRE.yaml"},
                "limit": "Future project discovery removed; source bytes and historical decisions are untouched."}








