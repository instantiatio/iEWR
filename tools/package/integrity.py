"""Maintainer-only package inventory. No functional module imports this file."""
import hashlib
import os
import re
import stat
REQUIRED_SLOTS = ("SYSE", "ME", "OCE", "PSD", "OPS", "SDLC")
PACKAGE_TREES = ("catalog", "docs", "examples", "frameworks", "scripts", "source", "templates", "tests", "modules", "adapters", "app", "tools")
ROOT_LOCAL_EXCLUSIONS = {".git", ".gitignore", ".DS_Store", "project", "PACKAGE_MANIFEST.md", "evidence"}
OPTIONAL_PROJECT_SCAFFOLD = {"project/README.md", "project/artifacts/.gitkeep", "project/source/.gitkeep", "project/handoff/.gitkeep"}


def _manifest_inventory(engine, raw):
    RepertoireError = engine.RepertoireError
    _collision_key = engine._collision_key
    _fail = engine._fail
    _relative = engine._relative
    try:
        content = raw.decode("utf-8")
    except UnicodeError as exc:
        raise RepertoireError("invalid_manifest", "Manifest must be UTF-8") from exc
    rows, seen = {}, set()
    pattern = re.compile(r"^\|\s*`([^`]+)`\s*\|[^|]*\|\s*([0-9A-Fa-f]{64})\s*\|\s*$")
    for line in content.splitlines():
        match = pattern.match(line)
        if not match:
            continue
        locus, digest = match.groups()
        _relative(locus)
        if locus == "PACKAGE_MANIFEST.md":
            _fail("invalid_manifest", "Manifest cannot self-hash")
        if _collision_key(locus) in seen:
            _fail("path_collision", "Duplicate/case/NFC-colliding manifest path")
        seen.add(_collision_key(locus))
        rows[locus] = digest.lower()
    if not rows:
        _fail("invalid_manifest", "No exact three-column inventory rows found")
    return rows


def check_package(engine, root, require_distribution_basis=False):
    _directory = engine._directory
    _fail = engine._fail
    _inventory_directory = engine._inventory_directory
    _names = engine._names
    _read_locus = engine._read_locus
    _root_fd = engine._root_fd
    _same_observation = engine._same_observation
    _scope_index = engine._scope_index
    inspect_source = engine.inspect_source
    verify_binding = engine.verify_binding
    SCOPE_ROOTS = engine.SCOPE_ROOTS
    INDEX_NAME = engine.INDEX_NAME
    MAX_INDEX_BYTES = engine.MAX_INDEX_BYTES
    """Check bytes/configuration, not full integration, source admission or release."""
    index, raw = _scope_index(root, "package", missing_ok=False)
    if raw is None:
        _fail("missing_package_repertoire", "Package repertoire is absent")
    slots = [e["required_slot"] for e in index["entries"] if "required_slot" in e]
    if sorted(slots) != sorted(REQUIRED_SLOTS):
        _fail("required_repertoire_missing", "Exactly one edition for each configured package slot is required")
    limits = []
    registered_source_paths = set()
    for entry in index["entries"]:
        verified = verify_binding(root, "package", entry["source_id"], entry["edition_id"], entry["edition_manifest_sha256"])
        observation = verified["observation"]
        registered_source_paths.update(
            [entry["source_locus"]] if observation["source_kind"] == "file" else
            [entry["source_locus"] + "/" + item["path"] for item in observation["files"]])
        basis = entry.get("distribution_basis", {"status": "unresolved"})
        if basis["status"] != "confirmed":
            limits.append({"source_id": entry["source_id"], "edition_id": entry["edition_id"],
                           "status": basis["status"]})
    with _root_fd(root) as rootfd:
        rows = _manifest_inventory(engine, _read_locus(rootfd, "PACKAGE_MANIFEST.md", MAX_INDEX_BYTES))
        actual_paths = set()
        root_names = _names(rootfd)
        for tree in PACKAGE_TREES:
            if tree in root_names:
                with _directory(rootfd, [tree]) as fd:
                    actual_paths.update(tree + "/" + f["path"] for f in _inventory_directory(fd))
        # Preserve every registered source byte, including hidden source files.
        # Only Finder metadata outside those exact source inventories is local
        # workspace noise; its presence does not authorize deletion or shipment.
        excluded_metadata = {path for path in actual_paths
                             if path.rsplit("/", 1)[-1] == ".DS_Store" and
                             path not in registered_source_paths}
        actual_paths.difference_update(excluded_metadata)
        if ".DS_Store" in root_names:
            excluded_metadata.add(".DS_Store")
        for name in root_names:
            if name in ROOT_LOCAL_EXCLUSIONS or name in PACKAGE_TREES:
                continue
            info = os.stat(name, dir_fd=rootfd, follow_symlinks=False)
            if stat.S_ISREG(info.st_mode):
                actual_paths.add(name)
            else:
                _fail("unexpected_package_path", f"Unknown package-root directory or special file: {name}")
        extra = sorted(actual_paths - set(rows))
        if extra:
            _fail("manifest_extra_paths", "Uninventoried package paths: " + ", ".join(extra[:20]))
        nonpackage = sorted(set(rows) - actual_paths - OPTIONAL_PROJECT_SCAFFOLD)
        if nonpackage:
            _fail("manifest_nonpackage_paths", "Manifest names non-package paths: " + ", ".join(nonpackage[:20]))
        # Validate the inventory boundary before reading any named row: a hash
        # must not turn private project/Git data into a distributed component.
        for locus, digest in rows.items():
            actual = hashlib.sha256(_read_locus(rootfd, locus)).hexdigest()
            if actual != digest:
                _fail("manifest_hash_mismatch", f"Manifest digest differs: {locus}")
        required_paths = {SCOPE_ROOTS["package"] + "/" + INDEX_NAME}
        for entry in index["entries"]:
            observation = inspect_source(root, entry["source_locus"], "package")
            if not _same_observation(entry, observation):
                _fail("stale_binding", "Package source changed during package verification")
            required_paths.update([entry["source_locus"]] if observation["source_kind"] == "file" else
                                  [entry["source_locus"] + "/" + f["path"] for f in observation["files"]])
        if required_paths - set(rows):
            _fail("manifest_missing_source", "Package repertoire/source files are missing from manifest")
    if require_distribution_basis and limits:
        _fail("distribution_basis_unresolved", "Technical integrity is not distribution permission; exact confirmation is pending")
    return {"status": "package_integrity_pass", "required_slots": list(REQUIRED_SLOTS),
            "entry_count": len(index["entries"]), "manifest_file_count": len(rows),
            "excluded_workspace_metadata": sorted(excluded_metadata),
            "distribution_ready": not limits, "distribution_limitations": limits,
            "limit": "Byte/configuration check only; not full integration, legal review, applicability, Admission or release."}
