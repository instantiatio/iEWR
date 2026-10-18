"""P: explicit pinned direct channel, not authentication inferred from prose."""
from hashlib import sha256
import json
from modules.governance.responses import ResponseSource


class PinnedResponses(ResponseSource):
    def __init__(self, read_bytes, trusted_refs):
        self.read_bytes, self.trusted_refs = read_bytes, dict(trusted_refs)

    def read_direct_response(self, reference, digest):
        trust = self.trusted_refs.get(reference)
        if trust is None or trust["digest"] != digest or not trust["channel_basis"]:
            raise ValueError("response_not_bound_to_direct_channel")
        raw = self.read_bytes(reference)
        if sha256(raw).hexdigest() != digest:
            raise ValueError("response_source_changed")
        value = json.loads(raw)
        if value.get("principal") != trust["principal"]:
            raise ValueError("response_principal_mismatch")
        return raw.decode("utf-8")
