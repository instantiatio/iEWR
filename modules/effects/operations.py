"""E owns effect observations. One invocation only; no scheduler or repair."""
from dataclasses import asdict, dataclass
from hashlib import sha256
from modules.governance.operations import OperationScope


@dataclass(frozen=True)
class OperationReceipt:
    outcome: str
    result_json: str
    effects_json: str
    reason: str


class OperationEffects:
    def __init__(self, governance, actuator, store):
        self.governance, self.actuator, self.store = governance, actuator, store

    def perform(self, operation_id, scope: OperationScope, direct_basis, initiation):
        if not initiation:
            return OperationReceipt("not_performed", "{}", "{}", "missing_X_initiation")
        governed = self.governance.assess(scope, direct_basis)
        if not governed.supported:
            return OperationReceipt("not_performed", "{}", "{}", governed.reason)
        key = sha256(("operation:" + operation_id).encode()).hexdigest()
        record = {"kind": "operation", "operation_id": operation_id, "targets": list(scope.targets),
                  "scope": asdict(scope), "direct_basis": asdict(direct_basis), "initiation": initiation,
                  "outcome": "unknown", "configuration": self.actuator.configuration()}
        old = self.store.read(key)
        if old and old.get("outcome") not in ("applied", "not_performed"):
            return OperationReceipt("unknown", "{}", "{}", "prior_material_effect_unresolved")
        self.store.write(key, record, old)
        try:
            receipt = self.actuator.perform(scope, lambda: self.governance.assess(scope, direct_basis).supported)
            self.store.write(key, {**record, **asdict(receipt)}, record)
            return receipt
        except (OSError, ValueError) as error:
            return OperationReceipt("unknown", "{}", "{}", "outcome_or_storage_unresolved: " + str(error))

    def records(self):
        return self.store.snapshot()
