"""R: derived accounts from bounded owner queries. No mutation or actuation port."""
from dataclasses import dataclass
import json
from typing import Protocol


class AccountQuery(Protocol):
    def read(self) -> str: ...


@dataclass(frozen=True)
class RecoveryResult:
    selection: str
    governance_json: str
    basis_json: str
    facts_json: str
    holds: tuple[str, ...]
    demands: tuple[str, ...]
    limits: tuple[str, ...]


def discover(initiatives, selected=None, index=None, unsearched=()):
    """Only direct candidate records select; an index is never an authority."""
    eligible = tuple(sorted(set(initiatives)))
    if selected is not None and selected not in eligible:
        return "hold:selection_not_in_direct_records", tuple(unsearched)
    if selected is not None:
        return selected, tuple(unsearched)
    if len(eligible) > 1:
        return "hold:Human_initiative_selection", tuple(unsearched)
    if unsearched:
        return "hold:discovery_coverage", tuple(unsearched)
    return (eligible[0] if eligible else "no_initiative"), ()


def impact(changed_claim, receivers, unsearched):
    """Owner judgments are inputs, not deductions from textual mention."""
    found = []
    for receiver, relation, owner_basis in receivers:
        if relation not in ("depends", "mentions only", "unresolved") or not owner_basis:
            relation = "unresolved"
        found.append((receiver, relation, owner_basis))
    return {"changed_claim": changed_claim, "receivers": tuple(found),
            "unsearched": tuple(unsearched), "complete": not unsearched and all(r[1] != "unresolved" for r in found)}


class Recovery:
    def __init__(self, governance: AccountQuery, basis: AccountQuery, facts: AccountQuery):
        self.queries = (governance, basis, facts)

    def reconstruct(self, selection):
        values, holds, demands = [], [], []
        for name, query in zip(("G", "basis", "facts"), self.queries):
            try:
                first = query.read()
                parsed = json.loads(first)
                if not isinstance(parsed, dict) or parsed.get("schema") != 1:
                    raise ValueError("unsupported_account_projection")
                # Bounded consistency check, not a claim of an atomic global snapshot.
                if first != query.read():
                    raise ValueError("owner_changed_during_read")
                values.append(first)
            except (OSError, ValueError, TypeError) as error:
                holds.append(name + ":" + str(error))
                values.append("{}")
        g, basis, facts = map(json.loads, values)
        if selection != "no_initiative":
            if not g.get("relations"):
                holds.append("G:direct_relations_missing")
            if not basis.get("bindings"):
                holds.append("basis:relied_bindings_missing")
        for relation in g.get("relations", []):
            if relation.get("current") is not True or not relation.get("direct_basis"):
                holds.append("G:" + relation.get("subject", "unknown_relation"))
        for binding in basis.get("bindings", []):
            if not binding.get("relied_digest") or binding.get("relied_digest") != binding.get("observed_digest"):
                holds.append("basis:" + binding.get("locus", "unknown_binding"))
        for record in facts.get("records", []):
            if record.get("kind") == "profile":
                if record.get("status") == "terminated":
                    demands.append("X_ordinary_stepwise_basis_not_same_profile_resume")
                continue
            status = record.get("outcome", record.get("status"))
            if record.get("owner") not in ("X", "E") or status not in ("applied", "not_performed", "reconciled"):
                target = record.get("target", record.get("operation_id", "unknown_target"))
                holds.append("effect_or_attempt:" + target)
                demands.append("E_reconciliation_via_separate_X_basis:" + target)
        for gap in facts.get("unsearched", []):
            holds.append("unobserved_SoR:" + gap)
            demands.append("separate_bounded_observation:" + gap)
        if selection.startswith("hold:"):
            holds.append(selection)
        return RecoveryResult(selection, *values, tuple(dict.fromkeys(holds)), tuple(dict.fromkeys(demands)),
                              ("derived_owner_views_not_global_atomic_snapshot", "no_retry_or_activation_grant"))

    @staticmethod
    def select_successor(previous_digest, next_digest, current_observed_digest, safe_boundary, selection_basis):
        if not previous_digest or not next_digest or next_digest != current_observed_digest:
            return {"outcome": "hold", "reason": "successor_binding_unresolved"}
        if not safe_boundary or not selection_basis:
            return {"outcome": "hold", "reason": "safe_boundary_or_selection_missing"}
        return {"outcome": "selected", "historical": previous_digest, "next": next_digest,
                "selection_basis": selection_basis, "limit": "selection_only_no_activation_or_rewrite"}
