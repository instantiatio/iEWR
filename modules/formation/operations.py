"""F: immutable intended basis. A declaration is not actual assignment or Work."""
from dataclasses import dataclass
from modules.sources.api import Binding


@dataclass(frozen=True)
class OperationBasis:
    operation_id: str
    capability: str
    targets: tuple[str, ...]
    parameters_json: str
    performer: str
    receiving_use: str
    method: Binding
    request: Binding

    def __post_init__(self):
        # Immutable transport values retain tuple semantics after JSON arrays.
        object.__setattr__(self, "targets", tuple(self.targets))

    def validate_intended(self):
        if not all((self.operation_id, self.capability, self.targets, self.performer, self.receiving_use)):
            raise ValueError("incomplete_intended_operation")
        if self.method.role != "method_description":
            raise ValueError("missing_method_description_basis")
