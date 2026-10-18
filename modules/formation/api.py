"""F owns use/Method basis; supplied exact substitution is a bounded Method use."""
from dataclasses import dataclass
from hashlib import sha256
from modules.sources.api import Binding
from modules.reliance.api import UseAssessment


@dataclass(frozen=True)
class EditBasis:
    target: str
    before: str
    after: str
    performer: str
    receiving_use: str
    method: Binding
    request: Binding


@dataclass(frozen=True)
class FormationResult:
    disposition: str
    reason: str
    basis: EditBasis | None


def form_next_result_basis(basis: EditBasis, available: UseAssessment) -> FormationResult:
    if (available.target, available.receiving_use, available.expected_sha256) != (
            basis.target, basis.receiving_use, sha256(basis.after.encode("utf-8")).hexdigest()):
        return FormationResult("hold", "available_evidence_use_mismatch", None)
    if available.reason in ("material_effect_unresolved", "receipt_binding_mismatch"):
        return FormationResult("hold", available.reason, None)
    if available.sufficient:
        return FormationResult("reuse", "requested_result_already_adequate", basis)
    if not basis.receiving_use or not basis.performer or basis.method.role != "method_description":
        return FormationResult("hold", "missing_method_or_use_basis", None)
    if basis.before == basis.after or not basis.before:
        return FormationResult("hold", "no_bounded_change", None)
    return FormationResult("direct", "supplied_exact_replacement_basis", basis)
