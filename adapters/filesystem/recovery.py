"""P: bounded read-only recovery projections; no source/frozen history discovery."""
from hashlib import sha256
import json
import os
from pathlib import Path, PurePosixPath
import stat
from modules.recovery.api import AccountQuery


class OwnerFacts(AccountQuery):
    def __init__(self, execution_query, effects_query, unsearched=()):
        self.execution_query, self.effects_query, self.unsearched = execution_query, effects_query, unsearched

    def read(self):
        records = []
        for owner, query in (("X", self.execution_query), ("E", self.effects_query)):
            for key, value in query():
                raw = json.loads(value)
                records.append({**raw, "owner": owner, "record_ref": key, "record_digest": sha256(value.encode()).hexdigest()})
        return json.dumps({"schema": 1, "records": records, "unsearched": self.unsearched}, sort_keys=True)


class BoundProjection(AccountQuery):
    def __init__(self, query):
        self.query = query

    def read(self):
        return json.dumps(self.query(), sort_keys=True)


def historical_carrier(raw, locus):
    """A finite compatibility reader; it does not upgrade old status meanings."""
    digest = sha256(raw).hexdigest()
    try:
        value = json.loads(raw)
    except (ValueError, UnicodeError):
        return {"locus": locus, "digest": digest, "kind": "opaque_historical_text",
                "text": raw.decode("utf-8"), "limit": "explicit_owner_interpretation_required"}
    if not isinstance(value, dict) or value.get("schema") not in (1, 2):
        raise ValueError("unsupported_historical_carrier_version")
    if "owner" in value:
        if value["owner"] not in ("execution", "effects") or not isinstance(value.get("record"), dict):
            raise ValueError("unsupported_historical_owner")
        return {"locus": locus, "digest": digest, "kind": "B1_B2_owner_record", "historical_value": value}
    return {"locus": locus, "digest": digest, "kind": "navigation_or_legacy_carrier", "historical_value": value,
            "limit": "IDs_and_named_use_only_no_authority_Work_or_reliance_conversion"}


def discover_history(tree):
    results = []
    # Only explicitly bound project's process directory, never arbitrary workspace recursion.
    try:
        with tree.parent("project/process/probe") as (fd, _):
            names = sorted(os.listdir(fd))
            if len(names) > 100:
                raise ValueError("discovery_budget")
            for name in names:
                if name.endswith(".json") and "/" not in name:
                    locus = "project/process/" + name
                    raw = tree.read(locus)
                    obj = json.loads(raw)
                    if obj.get("schema") != 1:
                        raise ValueError("unsupported_initiative_record")
                    if obj.get("initiative") and obj.get("receiving_use") and obj.get("direct_assignment_ref"):
                        results.append((obj["initiative"], locus, sha256(raw).hexdigest()))
    except FileNotFoundError:
        raise ValueError("discovery_coverage:project/process_missing")
    return tuple(results)


def canonical(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")


class ReentryReader:
    """Portable cooperative reader, not a hostile-writer filesystem boundary.

    Host observations and channel_basis MUST come from a qualified host consumer,
    not model arguments. Files are never interpreted as direct Human messages.
    """
    LIMIT = 4 * 1024 * 1024

    def __init__(self, root, context, observations=(), channel_basis=None):
        self.root = Path(root).absolute()
        if str(self.root.resolve()) != str(self.root):
            raise ValueError("linked_workspace")
        self.context = dict(context)
        if Path(context.get("workspace", "")).absolute() != self.root:
            raise ValueError("workspace_identity_mismatch")
        self.channel_basis = channel_basis
        self.observations = {}
        if len(observations) > 10000:
            raise ValueError("host_observation_budget")
        for obj in observations:
            seq = obj.get("seq")
            if type(seq) is not int or seq < 0 or seq > context.get("through_seq", -1) or seq in self.observations:
                raise ValueError("invalid_host_observation_identity")
            if obj.get("session") != context.get("session") or obj.get("workspace") != context.get("workspace"):
                raise ValueError("foreign_host_observation")
            self.observations[seq] = canonical(obj)
        self.current_request_seq = max((obj["seq"] for obj in observations
                                        if obj.get("kind") == "human_message" and obj.get("source") == "user"), default=-1)

    def local(self, locus):
        if not isinstance(locus, str) or not locus or "\\" in locus or ":" in locus:
            raise ValueError("unsafe_recovery_locus")
        parts = PurePosixPath(locus).parts
        if PurePosixPath(locus).is_absolute() or any(p in ("", ".", "..") or p.endswith((".", " ")) for p in locus.split("/")):
            raise ValueError("unsafe_recovery_locus")
        path = self.root
        for part in parts:
            path /= part
            info = path.lstat()
            if stat.S_ISLNK(info.st_mode) or getattr(info, "st_file_attributes", 0) & 0x400:
                raise ValueError("linked_recovery_locus")
        before = path.stat()
        if not stat.S_ISREG(before.st_mode) or before.st_size > self.LIMIT:
            raise ValueError("unsupported_recovery_file")
        raw = path.read_bytes()
        after = path.stat()
        if (before.st_ino, before.st_size, before.st_mtime_ns) != (after.st_ino, after.st_size, after.st_mtime_ns) or len(raw) != before.st_size:
            raise ValueError("recovery_file_changed_during_read")
        return raw

    def read(self, ref):
        if set(ref) == {"locus", "sha256"}:
            raw = self.local(ref["locus"])
        elif set(ref) == {"host_event", "sha256"} and type(ref["host_event"]) is int:
            if not self.channel_basis:
                raise ValueError("direct_channel_basis_missing")
            raw = self.observations[ref["host_event"]]
        else:
            raise ValueError("unsupported_exact_ref")
        if sha256(raw).hexdigest() != ref["sha256"]:
            raise ValueError("changed_or_unavailable_ref")
        return raw

    def direct(self, ref):
        if "host_event" not in ref or not self.channel_basis:
            raise ValueError("file_is_not_a_direct_channel")
        obj = json.loads(self.read(ref))
        if obj.get("kind") != "human_message" or obj.get("source") != "user":
            raise ValueError("not_direct_human_message")
        return obj


def discover_reentry(reader, loci):
    """Explicit project carriers only. Coverage is bounded by supplied surfaces."""
    if not isinstance(loci, list) or len(loci) > 100:
        raise ValueError("discovery_budget")
    candidates, unsearched = [], []
    for locus in loci:
        try:
            if not locus.startswith(("project/artifacts/", "project/process/", "project/handoff/")):
                raise ValueError("not_project_history")
            raw = reader.local(locus)
            obj = json.loads(raw)
            if not isinstance(obj, dict) or obj.get("schema") != 2 or obj.get("kind") != "initiative":
                raise ValueError("owner_interpretation_required")
            candidates.append({"locus": locus, "sha256": sha256(raw).hexdigest()})
        except (OSError, ValueError, TypeError, AttributeError) as error:
            unsearched.append({"locus": locus, "reason": str(error)})
    return {"candidates": candidates, "unsearched": unsearched,
            "limit": "explicit_surfaces_only_not_proof_of_workspace_history_completeness"}
