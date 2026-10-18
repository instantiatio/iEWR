"""Optional local FPF access. No source execution, implicit connection or authority.

Python 3.10+, standard library. Cooperative single-writer filesystem support;
path checks and a lock are not a hostile-writer sandbox. Host/G grounds remain
independent. Only fetch uses the network, against the public author's repository.
"""
import argparse
from contextlib import contextmanager
from datetime import datetime, timezone
from hashlib import sha256, sha1
import json
import os
from pathlib import Path
import re
import shutil
import tempfile
import urllib.request
import uuid


REPOSITORY = "https://github.com/ailev/FPF"
API = "https://api.github.com/repos/ailev/FPF"
RAW = "https://raw.githubusercontent.com/ailev/FPF"
FILES = ("FPF-Spec.md", "Readme.md", "LICENSE", "LICENSING.md")
LIMIT = 32 * 1024 * 1024
CORE = "docs/EWR_CORE_ARCHITECTURE_CONTRACT.md"


def digest(raw):
    return sha256(raw).hexdigest()


def now():
    return datetime.now(timezone.utc).isoformat()


def edition_name(value):
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_-]{0,95}", value):
        raise ValueError("invalid_edition_name")
    if re.fullmatch(r"(?i)(con|prn|aux|nul|com[1-9]|lpt[1-9])", value):
        raise ValueError("reserved_edition_name")
    return value


def safe(path):
    path = Path(os.path.abspath(path))
    for part in [*reversed(path.parents), path]:
        if part.is_symlink() or (part.exists() and
                getattr(part.stat(), "st_file_attributes", 0) & 0x400):
            raise ValueError("linked_path:" + str(part))
    return path


def read_bytes(path, limit=LIMIT):
    path = safe(path)
    before = path.stat()
    if not path.is_file() or before.st_size > limit:
        raise ValueError("unsupported_file:" + str(path))
    with path.open("rb") as stream:
        raw = stream.read(limit + 1)
    after = path.stat()
    if len(raw) > limit or (before.st_ino, before.st_size, before.st_mtime_ns) != (
            after.st_ino, after.st_size, after.st_mtime_ns) or len(raw) != after.st_size:
        raise ValueError("source_changed_during_read")
    return raw


def decode(raw):
    return json.loads(raw.decode("utf-8"))


def encoded(value):
    return (json.dumps(value, ensure_ascii=False, indent=2) + "\n").encode("utf-8")


def base(root):
    root = safe(root)
    return root, safe(root / "external-sources/fpf")


@contextmanager
def mutation(root):
    root, folder = base(root)
    folder.mkdir(parents=True, exist_ok=True)
    lock = safe(folder / ".access.lock")
    # An abandoned lock is reported; never guess that another writer is dead.
    fd = os.open(lock, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    try:
        with os.fdopen(fd, "wb") as stream:
            stream.write(str(os.getpid()).encode("ascii"))
        yield root, folder
    finally:
        lock.unlink()


def write_new(path, raw):
    path = safe(path)
    with path.open("xb") as stream:
        stream.write(raw)
        stream.flush()
        os.fsync(stream.fileno())


def save_connection(folder, value):
    path = safe(folder / "connection.json")
    previous = read_bytes(path, 1024 * 1024) if path.exists() else None
    # Old decisions survive updates and disconnect. These are local records,
    # never part of the distribution and never independent permission grants.
    if previous is not None:
        history = safe(folder / "history")
        history.mkdir(exist_ok=True)
        write_new(history / (uuid.uuid4().hex + ".json"), previous)
    temporary = folder / (".connection-" + uuid.uuid4().hex + ".tmp")
    write_new(temporary, encoded(value))
    try:
        if (read_bytes(path, 1024 * 1024) if path.exists() else None) != previous:
            raise ValueError("connection_changed_during_write")
        os.replace(temporary, path)
        if read_bytes(path, 1024 * 1024) != encoded(value):
            raise ValueError("connection_readback_failed")
    finally:
        if temporary.exists():
            temporary.unlink()


def get_public(url, limit=LIMIT):
    request = urllib.request.Request(url, headers={"User-Agent": "iEWR-FPF-access"})
    with urllib.request.urlopen(request, timeout=45) as response:
        if not response.geturl().startswith((API + "/", RAW + "/")):
            raise ValueError("unexpected_download_location")
        raw = response.read(limit + 1)
    if len(raw) > limit:
        raise ValueError("download_too_large")
    return raw


def fetch(root, revision="main"):
    if revision != "main" and not re.fullmatch(r"[0-9a-f]{40}", revision):
        raise ValueError("expected_main_or_full_commit")
    # Pin once before fetching any file; never combine mutable main responses.
    commit = (decode(get_public(API + "/commits/main", 4 * 1024 * 1024))["sha"]
              if revision == "main" else revision)
    if not re.fullmatch(r"[0-9a-f]{40}", commit) or revision != "main" and commit != revision:
        raise ValueError("invalid_upstream_commit")
    tree = decode(get_public(API + "/git/trees/" + commit, 4 * 1024 * 1024))
    if tree.get("truncated"):
        raise ValueError("incomplete_upstream_tree")
    blobs = {i["path"]: i for i in tree["tree"] if i["type"] == "blob"}
    payload = {}
    for name in FILES:
        if name not in blobs or blobs[name].get("mode") != "100644":
            raise ValueError("missing_regular_upstream_file:" + name)
        raw = get_public(RAW + "/" + commit + "/" + name)
        blob = sha1(b"blob " + str(len(raw)).encode("ascii") + b"\0" + raw).hexdigest()
        if blob != blobs[name]["sha"]:
            raise ValueError("download_blob_mismatch:" + name)
        payload[name] = raw
    payload["FPF-Spec.md"].decode("utf-8")
    info = {"schema": 1, "edition": commit, "origin": REPOSITORY,
            "commit": commit, "obtained_at": now(),
            "files": {n: digest(b) for n, b in payload.items()}}
    with mutation(root) as (_, folder):
        target = safe(folder / commit)
        if target.exists():
            existing = decode(read_bytes(target / "source.json", 1024 * 1024))
            if existing.get("files") != info["files"] or any(
                    digest(read_bytes(target / n)) != h for n, h in info["files"].items()):
                raise ValueError("existing_edition_drift")
        else:
            stage = Path(tempfile.mkdtemp(prefix=".download-", dir=folder))
            try:
                for name, raw in payload.items():
                    write_new(stage / name, raw)
                write_new(stage / "source.json", encoded(info))
                # A complete edition is published at once; connection unchanged.
                os.rename(stage, target)
            finally:
                if stage.exists():
                    shutil.rmtree(stage)
    return {"status": "downloaded", "edition": commit,
            "path": str(target), "connection_changed": False}


def connect(root, edition, scope, basis):
    edition_name(edition)
    if not scope.strip() or not basis.strip():
        raise ValueError("scope_and_direct_basis_required")
    with mutation(root) as (root, folder):
        source = safe(folder / edition / "FPF-Spec.md")
        raw = read_bytes(source)
        if not raw.decode("utf-8").strip():
            raise ValueError("empty_source")
        metadata = safe(source.parent / "source.json")
        if metadata.exists():
            info = decode(read_bytes(metadata, 1024 * 1024))
            if info.get("schema") != 1 or info.get("edition") != edition or info.get(
                    "files", {}).get("FPF-Spec.md") != digest(raw):
                raise ValueError("edition_drift")
        else:
            info = {"schema": 1, "edition": edition, "origin": "user-supplied",
                    "obtained_at": now(), "files": {"FPF-Spec.md": digest(raw)}}
            write_new(metadata, encoded(info))
        value = {"schema": 1, "enabled": True, "edition": edition,
                 "source_sha256": digest(raw), "scope": scope, "direct_basis": basis,
                 "connected_at": now(), "core_contract_sha256": digest(read_bytes(root / CORE))}
        save_connection(folder, value)
    return {"status": "connected", **value,
            "limit": "Recorded basis is not independently established permission or FPF conformance."}


def disconnect(root, basis):
    if not basis.strip():
        raise ValueError("direct_basis_required")
    with mutation(root) as (_, folder):
        path = folder / "connection.json"
        if not path.exists():
            return {"status": "disabled", "changed": False}
        value = decode(read_bytes(path, 1024 * 1024))
        value.update(enabled=False, disconnected_at=now(), disconnect_basis=basis)
        save_connection(folder, value)
    return {"status": "disabled", "sources_preserved": True}


def active_source(root, expected=None):
    root, folder = base(root)
    path = folder / "connection.json"
    if not path.exists():
        return None, None
    value = decode(read_bytes(path, 1024 * 1024))
    if value.get("schema") != 1 or not isinstance(value.get("enabled"), bool):
        raise ValueError("invalid_connection")
    if not value["enabled"]:
        return None, None
    if not value.get("scope", "").strip() or not value.get("direct_basis", "").strip():
        raise ValueError("missing_connection_basis")
    edition_name(value["edition"])
    if digest(read_bytes(root / CORE)) != value["core_contract_sha256"]:
        raise ValueError("core_contract_changed_reassess_connection")
    source = safe(folder / value["edition"] / "FPF-Spec.md")
    raw = read_bytes(source)
    actual = digest(raw)
    if actual != value["source_sha256"] or expected is not None and expected != actual:
        raise ValueError("source_edition_changed")
    return value, raw


def query(root, operation, term="", offset=0, length=6000, end=None, expected=None, limit=20):
    if offset < 0 or not 1 <= length <= 12000 or not 1 <= limit <= 50:
        raise ValueError("invalid_query_bounds")
    if offset and not expected:
        raise ValueError("continuation_requires_expected_sha256")
    value, raw = active_source(root, expected)
    if value is None:
        if operation == "status":
            return {"status": "disabled", "network_used": False}
        raise ValueError("fpf_not_connected")
    result = {"status": "connected", "edition": value["edition"],
              "sha256": value["source_sha256"], "scope": value["scope"],
              "source": "external-sources/fpf/" + value["edition"] + "/FPF-Spec.md"}
    if operation == "status":
        return result
    text = raw.decode("utf-8")
    if operation == "read":
        stop = len(text) if end is None else end
        if not 0 <= offset <= stop <= len(text):
            raise ValueError("invalid_read_extent")
        reached = min(offset + length, stop)
        return {**result, "offset": offset, "end": stop, "offset_unit": "unicode_character",
                "text": text[offset:reached], "next_offset": reached if reached < stop else None,
                "complete": reached == stop, "total_characters": len(text)}
    if operation not in ("toc", "search"):
        raise ValueError("unsupported_operation")
    if operation == "search" and not term.strip():
        raise ValueError("search_term_required")
    hits, pos = [], 0
    # Scan original text on demand; no lossy persistent index or source execution.
    # The text remains reachable even when a heading/query does not match.
    fence = None
    for number, line in enumerate(text.splitlines(keepends=True), 1):
        stripped = line.lstrip()
        marker = re.match(r"^(`{3,}|~{3,})(.*)$", stripped)
        if marker:
            token, suffix = marker.groups()
            if fence is None:
                fence = token
            elif token[0] == fence[0] and len(token) >= len(fence) and not suffix.strip():
                fence = None
        heading = re.match(r"^(#{1,6})\s+(.+?)\s*$", line) if fence is None else None
        matches = heading is not None if operation == "toc" else term.casefold() in line.casefold()
        if operation == "toc" and term:
            matches = matches and term.casefold() in line.casefold()
        if matches and pos >= offset:
            hits.append({"line": number, "offset": pos, "text": line.rstrip()[:300]})
            if len(hits) > limit:
                break
        pos += len(line)
    more = len(hits) > limit
    return {**result, "hits": hits[:limit], "next_offset": hits[-1]["offset"] if more else None,
            "complete": not more, "limit": "Navigation matches, not sufficient source reading or exhaustive semantic retrieval."}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=".", help="iEWR root")
    sub = parser.add_subparsers(dest="command", required=True)
    download = sub.add_parser("fetch", help="Download a pinned edition; does not connect")
    download.add_argument("--revision", default="main", help="main or full commit SHA")
    connection = sub.add_parser("connect", help="Record deliberate connection after direct user choice")
    connection.add_argument("--edition", required=True)
    connection.add_argument("--scope", required=True)
    connection.add_argument("--basis", required=True, help="Actual user instruction/reference, not an invented grant")
    off = sub.add_parser("disconnect")
    off.add_argument("--basis", required=True)
    for name in ("status", "toc", "search", "read"):
        reader = sub.add_parser(name)
        reader.add_argument("--query", default="")
        reader.add_argument("--offset", type=int, default=0)
        reader.add_argument("--length", type=int, default=6000)
        reader.add_argument("--end", type=int)
        reader.add_argument("--expected-sha256")
        reader.add_argument("--limit", type=int, default=20)
    args = parser.parse_args()
    try:
        if args.command == "fetch":
            result = fetch(args.root, args.revision)
        elif args.command == "connect":
            result = connect(args.root, args.edition, args.scope, args.basis)
        elif args.command == "disconnect":
            result = disconnect(args.root, args.basis)
        else:
            result = query(args.root, args.command, args.query, args.offset, args.length,
                           args.end, args.expected_sha256, args.limit)
        print(json.dumps(result, ensure_ascii=False, indent=2))
    except (ValueError, KeyError, TypeError, AttributeError, OSError) as exc:
        print(json.dumps({"status": "blocked", "reason": str(exc)}, ensure_ascii=False))
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
