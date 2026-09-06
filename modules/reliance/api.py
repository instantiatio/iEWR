"""L: receiving-use-relative direct byte evidence, no automatic Verification."""
from dataclasses import dataclass
from hashlib import sha256
from modules.effects.api import Observation, Receipt


@dataclass(frozen=True)
class UseAssessment:
    target: str
    receiving_use: str
    expected_sha256: str
    sufficient: bool
    reason: str


def assess_use(target: str, receiving_use: str, expected: str, observed: Observation,
               receipt: Receipt | None = None, unresolved: bool = False) -> UseAssessment:
    digest = sha256(expected.encode("utf-8")).hexdigest()
    if unresolved or (receipt is not None and receipt.outcome == "unknown"):
        return UseAssessment(target, receiving_use, digest, False, "material_effect_unresolved")
    if receipt is not None and (receipt.target != target or
            (receipt.outcome == "applied" and receipt.observed_sha256 != digest)):
        return UseAssessment(target, receiving_use, digest, False, "receipt_binding_mismatch")
    good = bool(receiving_use) and observed.target == target and observed.content == expected.encode("utf-8")
    return UseAssessment(target, receiving_use, digest, good,
                         "exact_bytes_for_named_use" if good else observed.reason or "requested_bytes_not_observed")
