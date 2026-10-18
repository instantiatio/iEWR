"""G: current direct grounds for an exact operation; no authority minting."""
from dataclasses import asdict, dataclass
import json
from modules.sources.api import Binding, inspect_binding


@dataclass(frozen=True)
class OperationScope:
    capability: str
    targets: tuple[str, ...]
    parameters_json: str
    performer: str
    receiving_use: str
    method: Binding


@dataclass(frozen=True)
class RelationAssessment:
    supported: bool
    direct_basis: Binding
    reason: str


def strict_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("ambiguous_duplicate_decision_field")
        result[key] = value
    return result


class OperationGovernance:
    def __init__(self, reader, clock):
        self.reader, self.clock = reader, clock

    def assess(self, scope: OperationScope, binding: Binding):
        try:
            if not self.reader.is_direct_source(binding):
                raise ValueError("direct_source_not_established")
            decision = json.loads(inspect_binding(self.reader, binding), object_pairs_hook=strict_object)
            allowed_fields = {"schema", "scope", "permission", "prohibitions", "conditions", "valid_from", "valid_until", "authority_basis_ref"}
            if set(decision) != allowed_fields or decision["schema"] != 2:
                raise ValueError("unsupported_decision_shape")
            expected = {**asdict(scope), "targets": list(scope.targets)}
            if decision["scope"] != expected:
                raise ValueError("decision_scope_mismatch")
            inspect_binding(self.reader, scope.method)
            if decision["permission"] is not True or decision["prohibitions"] != []:
                raise ValueError("permission_not_established")
            if decision["conditions"] != []:
                raise ValueError("condition_unresolved")
            if not decision["authority_basis_ref"]:
                raise ValueError("missing_authority_source")
            if not decision["valid_from"] <= self.clock() < decision["valid_until"]:
                raise ValueError("decision_outside_window")
            return RelationAssessment(True, binding, "exact_direct_basis_current")
        except (ValueError, OSError, TypeError, KeyError) as error:
            return RelationAssessment(False, binding, str(error))
