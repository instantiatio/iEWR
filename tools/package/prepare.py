"""Portable maintainer packaging; cooperative local reads, no authority grants.

Explicit manifest only. No source execution, network, registration or hash refresh.
This compensated consumer does not replace the POSIX filesystem adapter controls.
"""
import argparse
from hashlib import sha256
import json
import os
from pathlib import Path, PurePosixPath
import re
import stat
import sys
import unicodedata
import zipfile

from verify_configuration import verify

SCAFFOLD = {"project/README.md", "project/source/.gitkeep",
            "project/handoff/.gitkeep", "project/artifacts/.gitkeep"}
LEGACY_SCAFFOLD = (SCAFFOLD - {"project/handoff/.gitkeep"}) | {"project/reference/.gitkeep"}
TREES = {"modules", "adapters", "app", "tools", "docs", "catalog",
         "frameworks", "templates"}
EXTERNAL = "source/external-dpf/.gitkeep"
ROW = re.compile(r"^\|\s*`([^`]+)`\s*\|[^|]*\|\s*([a-fA-F0-9]{64})\s*\|\s*$")
LIMIT = 32 * 1024 * 1024


def safe_name(name):
    parts = name.split("/")
    if (not name or name.startswith("/") or "\\" in name or
            any(p in ("", ".", "..") or p[-1:] in (".", " ") or
                any(ord(c) < 32 or c in ':*?"<>|' for c in p) or
                re.fullmatch(r"(?i)(con|prn|aux|nul|com[1-9]|lpt[1-9])(?:\..*)?", p)
                for p in parts)):
        raise ValueError("unsafe_path:" + name)
    return unicodedata.normalize("NFC", name).casefold()


def selected_path(name, *, legacy=False):
    safe_name(name)
    first = name.split("/")[0]
    if first == "project":
        return name in SCAFFOLD or legacy and name in LEGACY_SCAFFOLD
    if first == "source":
        return name == EXTERNAL
    return first in TREES or "/" not in name and not name.startswith(".")


def read_file(root, name):
    safe_name(name)
    path = root
    for part in name.split("/"):
        path = path / part
        info = path.lstat()
        if (stat.S_ISLNK(info.st_mode) or
                getattr(info, "st_file_attributes", 0) & 0x400):
            raise ValueError("linked_path:" + name)
    before = path.stat()
    if not stat.S_ISREG(before.st_mode) or before.st_size > LIMIT:
        raise ValueError("unsupported_file:" + name)
    raw = path.read_bytes()
    after = path.stat()
    if (before.st_ino, before.st_size, before.st_mtime_ns) != (
            after.st_ino, after.st_size, after.st_mtime_ns) or len(raw) != before.st_size:
        raise ValueError("concurrent_change:" + name)
    return raw


def inventory(raw, *, legacy=False):
    rows, seen = {}, set()
    for line in raw.decode("utf-8").splitlines():
        match = ROW.fullmatch(line)
        if not match:
            continue
        name, digest = match.groups()
        key = safe_name(name)
        if key in seen or name == "PACKAGE_MANIFEST.md" or not selected_path(name, legacy=legacy):
            raise ValueError("invalid_selected_path:" + name)
        rows[name] = digest.lower()
        seen.add(key)
    if not rows:
        raise ValueError("empty_inventory")
    return rows


def snapshot(root):
    root = Path(root).absolute()
    if root.resolve() != root:
        raise ValueError("linked_root")
    manifest = read_file(root, "PACKAGE_MANIFEST.md")
    rows = inventory(manifest)
    if not SCAFFOLD | {EXTERNAL, "app/bootstrap/CONFIGURATION.json"} <= rows.keys():
        raise ValueError("missing_scaffold_or_configuration")
    payload = {name: read_file(root, name) for name in rows}
    for name, digest in rows.items():
        if sha256(payload[name]).hexdigest() != digest:
            raise ValueError("manifest_digest:" + name)
        if name.endswith("/.gitkeep") and payload[name]:
            raise ValueError("nonempty_scaffold:" + name)
    config = json.loads(payload["app/bootstrap/CONFIGURATION.json"])
    if set(config["files"]) != set(rows) - {"app/bootstrap/CONFIGURATION.json"}:
        raise ValueError("configuration_inventory_disagreement")
    core = "docs/EWR_CORE_ARCHITECTURE_CONTRACT.md"
    if config["architecture_sha256"] != sha256(payload[core]).hexdigest():
        raise ValueError("architecture_binding_mismatch")
    verify(root)
    repertoire = json.loads(payload["frameworks/dpf/REPERTOIRE.yaml"])
    slots = [e.get("required_slot") for e in repertoire["entries"]]
    if sorted(slots) != sorted(["SYSE", "ME", "OCE", "PSD", "OPS", "SDLC"]):
        raise ValueError("package_slots")
    for entry in repertoire["entries"]:
        locus = entry["source_locus"]
        if locus not in payload or sha256(payload[locus]).hexdigest() != entry["edition_manifest_sha256"]:
            raise ValueError("source_binding:" + locus)
        # This selected package uses file editions. Other source shapes need
        # their own explicit maintainer profile; do not silently flatten them.
        if entry["files"] != [{"path": PurePosixPath(locus).name,
                               "sha256": entry["edition_manifest_sha256"]}]:
            raise ValueError("unsupported_source_inventory:" + locus)
    for tree in sorted(TREES):
        if not (root / tree).exists():
            continue
        for directory, dirs, files in os.walk(root / tree, followlinks=False):
            dirs[:] = [d for d in dirs if d != "__pycache__"]
            for child in dirs:
                p = Path(directory) / child
                if p.is_symlink() or getattr(p.lstat(), "st_file_attributes", 0) & 0x400:
                    raise ValueError("linked_tree:" + str(p))
            for child in files:
                name = (Path(directory) / child).relative_to(root).as_posix()
                if child != ".DS_Store" and name not in rows:
                    raise ValueError("unselected_product_file:" + name)
    for path in root.iterdir():
        if path.name in TREES | {"project", "source", ".git", ".agents", ".codex", ".gitignore", ".DS_Store"}:
            continue
        if path.name != "PACKAGE_MANIFEST.md" and path.name not in rows:
            raise ValueError("unselected_root_path:" + path.name)
    for name, raw in payload.items():
        if read_file(root, name) != raw:
            raise ValueError("changed_during_check:" + name)
    if read_file(root, "PACKAGE_MANIFEST.md") != manifest:
        raise ValueError("manifest_changed_during_check")
    payload["PACKAGE_MANIFEST.md"] = manifest
    return payload


def digest_map(payload):
    return {name: sha256(raw).hexdigest() for name, raw in sorted(payload.items())}


def compare(old_payload, new_payload):
    locus = "frameworks/dpf/REPERTOIRE.yaml"
    old_entries = {(e["source_id"], e["edition_id"]): e for e in json.loads(old_payload[locus])["entries"]}
    for entry in json.loads(new_payload[locus])["entries"]:
        prior = old_entries.get((entry["source_id"], entry["edition_id"]))
        if prior and prior["edition_manifest_sha256"] != entry["edition_manifest_sha256"]:
            raise ValueError("same_edition_drift:" + entry["source_id"] + ":" + entry["edition_id"])
    old, new = digest_map(old_payload), digest_map(new_payload)
    return {"added": sorted(new.keys() - old.keys()), "removed": sorted(old.keys() - new.keys()),
            "changed": {n: {"before": old[n], "after": new[n]}
                        for n in sorted(new.keys() & old.keys()) if old[n] != new[n]}}


def read_zip(path):
    with zipfile.ZipFile(path) as archive:
        members = archive.infolist()
        if not members or len(members) > 10000:
            raise ValueError("unsupported_archive_inventory")
        payload, seen, wrappers = {}, set(), set()
        total = 0
        for member in members:
            key = safe_name(member.filename)
            if key in seen or member.is_dir() or stat.S_ISLNK(member.external_attr >> 16):
                raise ValueError("duplicate_or_special_archive_entry")
            seen.add(key)
            parts = member.filename.split("/", 1)
            if len(parts) != 2:
                raise ValueError("archive_requires_one_wrapper")
            wrappers.add(parts[0])
            total += member.file_size
            if member.file_size > LIMIT or total > 128 * 1024 * 1024:
                raise ValueError("archive_size_limit")
            payload[parts[1]] = archive.read(member)
        if len(wrappers) != 1 or "PACKAGE_MANIFEST.md" not in payload:
            raise ValueError("archive_wrapper_or_manifest")
        # Old archives remain inspectable; new snapshots/builds use only SCAFFOLD.
        rows = inventory(payload["PACKAGE_MANIFEST.md"], legacy=True)
        if set(rows) | {"PACKAGE_MANIFEST.md"} != set(payload):
            raise ValueError("archive_inventory")
        for name, digest in rows.items():
            if sha256(payload[name]).hexdigest() != digest:
                raise ValueError("archive_digest:" + name)
            if name.endswith("/.gitkeep") and payload[name]:
                raise ValueError("nonempty_scaffold:" + name)
        return payload


def build(root, output, payload):
    output = Path(output).absolute()
    # A caller supplies an existing controlled directory. No implicit mkdir,
    # replacement or write into selected product/source/reference surfaces.
    parent = output.parent
    if not parent.is_dir() or parent.resolve() != parent:
        raise ValueError("output_parent_missing_or_linked")
    root = Path(root).absolute()
    try:
        relative = output.relative_to(root).as_posix()
    except ValueError:
        raise ValueError("output_outside_project_artifacts")
    if not relative.startswith("project/artifacts/") or output.suffix != ".zip":
        raise ValueError("output_requires_project_artifacts_zip")
    safe_name(output.stem)
    with output.open("xb") as handle:
        with zipfile.ZipFile(handle, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
            for name, raw in sorted(payload.items()):
                info = zipfile.ZipInfo(output.stem + "/" + name, (2026, 1, 1, 0, 0, 0))
                info.compress_type = zipfile.ZIP_DEFLATED
                info.external_attr = 0o100644 << 16
                archive.writestr(info, raw)
    if read_zip(output) != payload:
        raise ValueError("output_readback_mismatch; retain artifact for reconciliation")
    return {"path": str(output), "bytes": output.stat().st_size,
            "sha256": sha256(output.read_bytes()).hexdigest()}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("operation", choices=["check", "diff", "build"])
    parser.add_argument("--root", required=True)
    parser.add_argument("--baseline")
    parser.add_argument("--output")
    args = parser.parse_args()
    payload = snapshot(args.root)
    result = {"files": len(payload), "manifest_sha256": sha256(payload["PACKAGE_MANIFEST.md"]).hexdigest(),
              "configuration_sha256": sha256(payload["app/bootstrap/CONFIGURATION.json"]).hexdigest(),
              "limit": "cooperative local byte checks; not behavior, authority, acceptance or host isolation"}
    if args.operation == "diff":
        if not args.baseline:
            parser.error("diff requires --baseline")
        prior = read_zip(args.baseline)
        result["baseline_zip_sha256"] = sha256(Path(args.baseline).read_bytes()).hexdigest()
        result["delta"] = compare(prior, payload)
    elif args.operation == "build":
        if not args.output:
            parser.error("build requires --output")
        result["zip"] = build(args.root, args.output, payload)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    try:
        main()
    except (ValueError, OSError, KeyError, zipfile.BadZipFile) as error:
        print(json.dumps({"error": str(error), "disposition": "hold dependent use; inspect any output before retry"}, ensure_ascii=False))
        sys.exit(1)
