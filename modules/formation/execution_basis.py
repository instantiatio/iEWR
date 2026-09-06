"""F intended coordination and bounded external contribution classification."""
from dataclasses import dataclass


def plan_need(coordination_question, intended_items):
    return {"workplan_use": bool(coordination_question and intended_items),
            "question": coordination_question, "limit": "intention_does_not_grant_or_admit_Work"}


def readiness_use(plan_ref=None, item_ref=None):
    return "applicable_PlanItem_readiness" if plan_ref and item_ref else "direct_relations_no_A15_5_gate"


def external_contribution(capability_basis, foreign_process=None, mapping=None):
    if not capability_basis:
        return {"outcome": "hold", "reason": "observed_capability_basis_missing"}
    if foreign_process is None:
        kind = "capability_only"
    elif mapping and all(mapping.get(k) for k in ("question", "method_contribution", "limits")) and mapping.get("imports_foreign_authority") is False:
        kind = "process_bearing_mappable"
    else:
        kind = "process_incompatible"
    return {"classification": kind, "capability_basis": capability_basis,
            "continuation": "bounded_fallback_or_stop" if kind == "process_incompatible" else "explicit_current_Work_basis_required"}


@dataclass(frozen=True)
class Profile:
    identity: str
    revision: str
    scope_ref: str
    limit: int
    guards: tuple[str, ...]
    override_ref: str
    recovery_ref: str
    claimed_unsupervised: bool = False
    enactment_budget_ref: str = ""
    separation_of_duties_ref: str = ""

    def gaps(self):
        missing = [name for name in ("identity", "revision", "scope_ref", "guards", "override_ref", "recovery_ref") if not getattr(self, name)]
        if type(self.limit) is not int or self.limit <= 0:
            missing.append("budget")
        if self.claimed_unsupervised:
            missing.extend(name for name in ("enactment_budget_ref", "separation_of_duties_ref") if not getattr(self, name))
        return tuple(missing)
