"""X initiates one operation under F/G/E basis; unknown history never replays."""
from dataclasses import asdict, dataclass
from hashlib import sha256
import json
from modules.formation.operations import OperationBasis
from modules.governance.operations import OperationScope


@dataclass(frozen=True)
class OperationResult:
    outcome: str
    reason: str
    receipt: object = None


class OperationExecution:
    def __init__(self, governance, effects, store):
        self.governance, self.effects, self.store = governance, effects, store

    def records(self):
        return self.store.snapshot()

    def attempt(self, basis: OperationBasis):
        try:
            basis.validate_intended()
            for _, encoded in self.records():
                record = json.loads(encoded)
                targets = record.get("targets", [record.get("target")])
                if set(basis.targets) & set(targets) and record.get("status") not in ("applied", "not_performed", "reconciled"):
                    raise ValueError("prior_target_action_unresolved_no_replay")
            scope = OperationScope(basis.capability, basis.targets, basis.parameters_json,
                                   basis.performer, basis.receiving_use, basis.method)
            governed = self.governance.assess(scope, basis.request)
            if not governed.supported:
                raise ValueError(governed.reason)
            key = sha256(("operation:" + basis.operation_id).encode()).hexdigest()
            previous = self.store.read(key)
            if previous:
                if json.dumps(previous.get("intended_basis"), sort_keys=True) != json.dumps(asdict(basis), sort_keys=True):
                    raise ValueError("operation_identity_collision")
                return OperationResult("reuse", "existing_attempt_requires_result_use_assessment", previous.get("receipt"))
            pending = {"kind": "operation", "operation_id": basis.operation_id, "targets": list(basis.targets),
                       "intended_basis": asdict(basis), "status": "pending", "formal_work_claim": "not_asserted"}
            self.store.write(key, pending, None)
            receipt = self.effects.perform(basis.operation_id, scope, basis.request, "execution:" + key)
            self.store.write(key, {**pending, "status": receipt.outcome, "receipt": asdict(receipt)}, pending)
            return OperationResult("done" if receipt.outcome == "applied" else "hold", receipt.reason, receipt)
        except (OSError, ValueError, TypeError) as error:
            return OperationResult("hold", str(error))
