"""P: bounded read-only recovery projections; no source/frozen history discovery."""
from hashlib import sha256
import json
import os
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
        pass
    return tuple(results)
