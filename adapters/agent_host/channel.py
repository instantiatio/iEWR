"""P: explicit synthetic request source and one-call transport, no successor calls."""
import base64
from dataclasses import fields, is_dataclass
import json
from pathlib import Path
from modules.interaction.api import INPUT_VALUES
from modules.sources.api import Binding


OUTER_BASIS = "Human:B1-only:plan-sections-4-5"


class FixtureSources:
    def __init__(self, tree, candidate: Path, trusted_request_sha256: str):
        self.tree, self.candidate = tree, candidate
        self.trusted_request_sha256 = trusted_request_sha256

    def read_source(self, locus):
        if locus == "fixture:inputs/request.json":
            return self.tree.read("inputs/request.json")
        if locus == "candidate:modules/formation/CONTRACT.md":
            # Candidate byte identity is additionally pinned in execution evidence.
            path = self.candidate / "modules/formation/CONTRACT.md"
            if path.is_symlink():
                raise ValueError("unsafe_method_source")
            return path.read_bytes()
        raise ValueError("source_not_in_b1_read_scope")

    def is_direct_source(self, binding: Binding):
        if (binding.locus, binding.role, binding.sha256) != (
                "fixture:inputs/request.json", "synthetic_direct_request", self.trusted_request_sha256):
            return False
        data = json.loads(self.read_source(binding.locus))
        # Not authentication for real users. The CLI host explicitly supplies a
        # pinned test request within the outer Human-authorized synthetic scope.
        return data.get("authority_basis_ref") == OUTER_BASIS


def encode(value):
    if is_dataclass(value):
        return {"$type": type(value).__name__, **{f.name: encode(getattr(value, f.name)) for f in fields(value)}}
    if isinstance(value, bytes):
        return {"$bytes": base64.b64encode(value).decode("ascii")}
    if isinstance(value, dict):
        return {k: encode(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [encode(v) for v in value]
    return value


def decode(value):
    if isinstance(value, list):
        return [decode(v) for v in value]
    if not isinstance(value, dict):
        return value
    if "$bytes" in value:
        if set(value) != {"$bytes"}:
            raise ValueError("unknown_transport_fields")
        return base64.b64decode(value["$bytes"], validate=True)
    if "$type" in value:
        cls = INPUT_VALUES.get(value["$type"])
        if cls is None:
            raise ValueError("unsupported_public_value")
        return cls(**{k: decode(v) for k, v in value.items() if k != "$type"})
    return {k: decode(v) for k, v in value.items()}


def serve_one(interaction, message):
    if message.get("version") != 1:
        raise ValueError("unsupported_transport_version")
    if "presentation" in message:
        return interaction.present(**message["presentation"])
    if set(message) != {"version", "owner", "operation", "arguments"}:
        raise ValueError("unsupported_message_fields")
    return interaction.submit(message["owner"], message["operation"], **decode(message["arguments"]))
