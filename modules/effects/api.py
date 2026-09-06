"""E implements an initiated bounded effect, observes it, and never schedules Work."""
from dataclasses import asdict, dataclass
from hashlib import sha256
from typing import Callable, Protocol
from modules.governance.api import ActionScope, Governance, Binding


@dataclass(frozen=True)
class Boundary:
    status: str
    configuration: str
    limitation: str


@dataclass(frozen=True)
class Observation:
    target: str
    content: bytes | None
    reason: str = ""


@dataclass(frozen=True)
class Receipt:
    target: str
    outcome: str
    reason: str
    observed_sha256: str | None
    material_effect_count: int | None
    disposition: str


class EffectActuator(Protocol):
    def boundary(self) -> Boundary: ...
    def observe(self, target: str) -> Observation: ...
    def replace(self, scope: ActionScope, guard: Callable[[], bool]) -> Receipt: ...


class EffectStore(Protocol):
    def read(self, key: str) -> dict | None: ...
    def write(self, key: str, value: dict, previous: dict | None) -> None: ...


class Effects:
    def __init__(self, governance: Governance, actuator: EffectActuator, store: EffectStore):
        self.governance, self.actuator, self.store = governance, actuator, store

    def assess_boundary(self) -> Boundary:
        return self.actuator.boundary()

    def observe_effect(self, target: str) -> Observation:
        return self.actuator.observe(target)

    def perform_bounded_effect(self, scope: ActionScope, basis: Binding, initiation: str) -> Receipt:
        if not initiation:
            return Receipt(scope.target, "not_performed", "missing_initiation", None, 0, "no_target_effect")
        allowed = self.governance.resolve_relations(scope, basis)
        if not allowed.supported:
            return Receipt(scope.target, "not_performed", allowed.reason, None, 0, "no_target_effect")
        boundary = self.assess_boundary()
        if boundary.status not in ("enforced", "compensated"):
            return Receipt(scope.target, "not_performed", "required_control_unsupported", None, 0, "no_target_effect")
        key = sha256(scope.target.encode()).hexdigest()
        pending = {"target": scope.target, "initiation": initiation, "outcome": "unknown",
                   "direct_basis": asdict(basis), "configuration": asdict(boundary)}
        try:
            old = self.store.read(key)
            if old is not None and (old.get("target") != scope.target or
                    old.get("outcome") not in ("unknown", "applied", "not_performed")):
                raise ValueError("unsupported_effect_record")
            if old and old.get("outcome") == "unknown":
                return Receipt(scope.target, "unknown", "prior_effect_unresolved", None, None, "dependent_use_blocked")
            self.store.write(key, pending, old)
        except (OSError, ValueError) as error:
            return Receipt(scope.target, "not_performed", "effect_intent_storage: " + str(error), None, 0, "no_target_effect")
        try:
            receipt = self.actuator.replace(
                scope, lambda: self.governance.resolve_relations(scope, basis).supported)
            self.store.write(key, {**pending, **asdict(receipt)}, pending)
            return receipt
        except (OSError, ValueError) as error:
            # Target may already have changed; persisted E intent and X pending survive.
            return Receipt(scope.target, "unknown", "effect_outcome_unresolved: " + str(error),
                           None, None, "dependent_use_blocked")
