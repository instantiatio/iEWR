"""X owns entry, one actual attempt and pending hold. Full R is not implemented."""
from dataclasses import asdict, dataclass
from hashlib import sha256
from typing import Protocol
from modules.formation.api import EditBasis
from modules.governance.api import ActionScope, Governance
from modules.effects.api import Effects, Receipt


class ExecutionStore(Protocol):
    def read(self, key: str) -> dict | None: ...
    def write(self, key: str, value: dict, previous: dict | None) -> None: ...


@dataclass(frozen=True)
class ExecutionResult:
    target: str
    outcome: str
    reason: str
    receipt: Receipt | None = None


class Execution:
    def __init__(self, governance: Governance, effects: Effects, store: ExecutionStore):
        self.governance, self.effects, self.store = governance, effects, store

    def read_execution(self, target: str) -> dict | None:
        record = self.store.read(sha256(target.encode()).hexdigest())
        if record is not None and (record.get("target") != target or record.get("status") not in
                ("pending", "unknown", "applied", "not_performed")):
            raise ValueError("unsupported_execution_record")
        return record

    def attempt_action(self, basis: EditBasis) -> ExecutionResult:
        try:
            prior = self.read_execution(basis.target)
        except (OSError, ValueError) as error:
            return ExecutionResult(basis.target, "hold", "execution_state_unreadable: " + str(error))
        if prior and prior.get("status") in ("pending", "unknown"):
            return ExecutionResult(basis.target, "hold", "prior_action_unresolved_no_replay")
        if basis.method.role != "method_description" or not basis.before or basis.before == basis.after:
            return ExecutionResult(basis.target, "hold", "missing_direct_method_basis")
        scope = ActionScope(basis.target, basis.before, basis.after, basis.performer, basis.receiving_use, basis.method)
        governed = self.governance.resolve_relations(scope, basis.request)
        if not governed.supported:
            return ExecutionResult(basis.target, "hold", governed.reason)
        if self.effects.assess_boundary().status not in ("enforced", "compensated"):
            return ExecutionResult(basis.target, "hold", "required_control_unsupported")
        observed = self.effects.observe_effect(basis.target)
        if observed.content == basis.after.encode("utf-8"):
            return ExecutionResult(basis.target, "reuse", "requested_bytes_already_present")
        if observed.content != basis.before.encode("utf-8"):
            return ExecutionResult(basis.target, "hold", observed.reason or "input_bytes_changed")
        key = sha256(basis.target.encode()).hexdigest()
        pending = {"status": "pending", "basis": asdict(basis), "target": basis.target,
                   "formal_work_claim": "not_asserted", "request_basis": asdict(governed.direct_basis)}
        try:
            self.store.write(key, pending, prior)
        except (OSError, ValueError) as error:
            return ExecutionResult(basis.target, "hold", "pending_storage_unresolved: " + str(error))
        receipt = self.effects.perform_bounded_effect(scope, basis.request, "execution:" + key)
        final = {**pending, "status": receipt.outcome, "receipt": asdict(receipt)}
        try:
            self.store.write(key, final, pending)
        except (OSError, ValueError) as error:
            return ExecutionResult(basis.target, "hold", "completion_storage_unresolved: " + str(error), receipt)
        return ExecutionResult(basis.target, "done" if receipt.outcome == "applied" else "hold", receipt.reason, receipt)
