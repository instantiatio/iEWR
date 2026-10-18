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


def discover(initiatives, selected=None, index=None, unsearched=(), selection_basis=None):
    """Only direct candidate records select; an index is never an authority."""
    eligible = tuple(sorted(set(initiatives)))
    if unsearched:
        return "hold:discovery_coverage", tuple(unsearched)
    if selected is not None and selected not in eligible:
        return "hold:selection_not_in_direct_records", tuple(unsearched)
    if selected is not None:
        if not isinstance(selection_basis, dict) or selection_basis.get("initiative") != selected or not selection_basis.get("direct_ref"):
            return "hold:selection_provenance", ()
        return selected, tuple(unsearched)
    if len(eligible) > 1:
        return "hold:Human_initiative_selection", tuple(unsearched)
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
        # Legacy projections remain readable, but cannot silently qualify re-entry.
        for name, account in zip(("G", "basis", "facts"), (g, basis, facts)):
            if selection != "no_initiative" and account.get("initiative") != selection:
                holds.append(name + ":initiative_binding_missing_or_mismatched")
        if facts.get("complete") is not True:
            holds.append("facts:coverage_unestablished")
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


class ReentryEvidence(Protocol):
    """Qualified P supplies bytes and direct-channel identity, never permission."""
    context: dict
    current_request_seq: int

    def read(self, ref: dict) -> bytes: ...
    def direct(self, ref: dict) -> dict: ...


def assess_reentry(request, evidence: ReentryEvidence):
    """Bounded schema-2 assessment. G interpretations remain supplied owner judgments.

    Missing legacy bindings produce a hold, not an inferred migration. No writes,
    activation, arbitrary-text authority extraction, or automatic successor.
    """
    from hashlib import sha256

    holds, observed, accounts = [], [], {}
    selection = use = None
    disposition = "hold"
    context = {}
    found = {}

    def require(condition, reason):
        if not condition:
            raise ValueError(reason)

    def read(ref):
        require(isinstance(ref, dict), "missing_exact_ref")
        digest = ref.get("sha256")
        require(isinstance(digest, str) and len(digest) == 64 and all(c in "0123456789abcdef" for c in digest), "invalid_digest")
        raw = evidence.read(ref)
        require(sha256(raw).hexdigest() == digest, "changed_or_unavailable_ref")
        require(raw == evidence.read(ref), "evidence_changed_during_read")
        observed.append(dict(ref))
        return raw

    def record(ref):
        obj = json.loads(read(ref))
        require(isinstance(obj, dict) and obj.get("schema") == 2, "unsupported_record_schema")
        return obj

    def direct(ref, exact_text=None):
        read(ref)
        obj = evidence.direct(ref)
        require(obj.get("source") == "user" and obj.get("kind") == "human_message", "direct_human_channel_required")
        require(obj.get("workspace") == context["workspace"] and obj.get("session") == context["session"], "foreign_direct_context")
        require(type(obj.get("seq")) is int and 0 <= obj["seq"] <= context["through_seq"], "direct_outside_prefix")
        require(isinstance(obj.get("text"), str) and bool(obj["text"]), "direct_text_missing")
        if exact_text is not None:
            require(obj["text"] == exact_text, "human_response_text_mismatch")
        return obj

    def bound(obj, owner, historical=False):
        require(obj.get("owner") == owner, "account_owner_mismatch:" + owner)
        require(obj.get("initiative") == selection, "account_subject_mismatch:" + owner)
        if historical:
            previous = obj.get("context", {})
            require(isinstance(obj.get("use"), str) and bool(obj["use"]), "historical_use_missing")
            require(isinstance(previous, dict) and set(previous) == set(context) and
                    all(previous[k] == context[k] for k in context if k != "through_seq") and
                    type(previous["through_seq"]) is int and 0 <= previous["through_seq"] <= context["through_seq"],
                    "foreign_or_future_historical_context:" + owner)
        else:
            require(obj.get("use") == use, "account_subject_mismatch:" + owner)
            require(obj.get("context") == context, "stale_or_foreign_account:" + owner)

    try:
        require(isinstance(request, dict) and request.get("schema") == 2, "unsupported_reentry_schema")
        context = request.get("context", {})
        require(isinstance(context, dict) and set(context) == {"host", "workspace", "session", "lineage", "through_seq"}, "invalid_context")
        require(all(isinstance(context[k], str) and context[k] for k in ("host", "workspace", "session", "lineage")), "missing_context_identity")
        require(type(context["through_seq"]) is int and context["through_seq"] >= 0, "invalid_prefix")
        require(context == evidence.context, "observed_context_mismatch")
        kind = request.get("kind")
        require(kind in ("continuation", "new_question"), "unsupported_request_kind")
        current = direct(request.get("request_ref"))
        require(current["seq"] == evidence.current_request_seq, "not_current_direct_request")
        coverage = request.get("coverage", {})
        require(isinstance(coverage, dict) and coverage.get("complete") is True and coverage.get("unsearched") == [], "discovery_coverage")
        coverage_record = record(coverage.get("ref"))
        require(coverage_record.get("kind") == "coverage" and coverage_record.get("context") == context and coverage_record.get("complete") is True and coverage_record.get("unsearched") == [], "coverage_basis_missing_or_stale")
        candidates = request.get("candidates")
        require(isinstance(candidates, list) and len(candidates) <= 100, "candidate_budget_or_shape")
        found = {}
        for ref in candidates:
            item = record(ref)
            key = item.get("initiative")
            require(item.get("kind") == "initiative" and isinstance(key, str) and bool(key) and isinstance(item.get("use"), str) and bool(item["use"]), "invalid_candidate")
            require(key not in found, "conflicting_candidate_identity")
            direct(item.get("request_ref"))
            found[key] = item
        if not found:
            require(kind == "new_question" and request.get("selection_ref") is None, "continuation_history_or_selection_missing")
            disposition = "new_question"
        else:
            require(request.get("selection_ref") is not None, "Human_initiative_selection" if len(found) > 1 else "direct_selection_basis_missing")
            chosen = record(request["selection_ref"])
            selection, use = chosen.get("initiative"), chosen.get("use")
            require(selection in found and found[selection]["use"] == use, "selection_not_in_direct_candidates")
            bound(chosen, "G")
            require(chosen.get("kind") == "selection", "selection_provenance")
            choice = direct(chosen.get("direct_ref"), chosen.get("exact_text"))
            require(isinstance(chosen.get("exact_text"), str), "selection_exact_text_missing")
            # A generic continuation is not itself an initiative-selection answer.
            require(kind != "continuation" or choice["seq"] != current["seq"], "continuation_is_not_selection")
            for name, owner in (("G", "G"), ("basis", "F"), ("facts", "X/E")):
                obj = record(request.get("accounts", {}).get(name))
                bound(obj, owner)
                accounts[name] = obj
            g, basis, facts = (accounts[k] for k in ("G", "basis", "facts"))
            require(g.get("selection_ref") == request["selection_ref"] and g.get("current") is True, "governance_selection_or_currentness")
            require(isinstance(g.get("direct"), list) and bool(g["direct"]), "governance_direct_grounds_missing")
            for relation in g["direct"]:
                require(isinstance(relation.get("exact_text"), str), "governance_exact_text_missing")
                require(relation.get("kind") in ("request", "answer"), "direct_relation_kind_missing")
                direct(relation.get("ref"), relation["exact_text"])
                if relation["kind"] == "answer":
                    read(relation.get("question_ref"))
            scope = g.get("scope", {})
            require(isinstance(scope.get("allowed"), list) and isinstance(scope.get("prohibited"), list), "scope_and_negative_constraints_missing")
            require(all(isinstance(s, str) for s in scope["allowed"] + scope["prohibited"]), "invalid_scope")
            require(not set(scope["allowed"]) & set(scope["prohibited"]), "conflicting_scope")
            require(isinstance(basis.get("bindings"), list) and bool(basis["bindings"]), "relied_basis_missing")
            for binding in basis["bindings"]:
                require(binding.get("receiving_use") == use, "basis_use_mismatch")
                read(binding.get("ref"))
            require(g.get("relied_refs") == [b["ref"] for b in basis["bindings"]], "governance_relied_revision_mismatch")
            require(facts.get("complete") is True and facts.get("unsearched") == [], "factual_coverage")
            require(isinstance(facts.get("records"), list), "factual_records_missing")
            if not facts["records"]:
                read(facts.get("no_effects_basis_ref"))
            ids = set()
            for fact in facts["records"]:
                action = fact.get("action_id")
                require(isinstance(action, str) and action and action not in ids, "action_identity_missing_or_conflicting")
                ids.add(action)
                require(fact.get("outcome") in ("applied", "not_performed", "reconciled"), "unknown_effect_requires_reconciliation:" + action)
                intent = record(fact.get("intent_ref"))
                bound(intent, "X", historical=True)
                require(intent.get("action_id") == action and intent.get("attempt_ref") == fact.get("attempt_ref"), "intent_attempt_binding_mismatch:" + action)
                read(fact.get("attempt_ref"))
                require(isinstance(fact.get("observation_refs"), list) and bool(fact["observation_refs"]), "effect_observation_missing:" + action)
                for ref in fact["observation_refs"]:
                    observation = record(ref)
                    bound(observation, "E", historical=True)
                    require(observation.get("use") == intent["use"], "historical_action_use_mismatch")
                    require(observation.get("kind") == "effect_observation" and observation.get("action_id") == action and observation.get("attempt_ref") == fact.get("attempt_ref") and observation.get("outcome") == fact["outcome"], "effect_observation_binding_mismatch:" + action)
                    require(isinstance(observation.get("observed_refs"), list) and bool(observation["observed_refs"]), "effect_evidence_missing:" + action)
                    for observed_ref in observation["observed_refs"]:
                        read(observed_ref)
            state = facts.get("disposition")
            if state == "completed":
                require(facts.get("next_action_ref") is None, "completed_has_successor")
                disposition = "completed"
            else:
                require(state == "pending", "factual_disposition_unresolved")
                pending = record(facts.get("next_action_ref"))
                bound(pending, "X")
                require(pending.get("kind") == "intended_action" and pending.get("status") == "not_attempted", "next_action_not_established")
                require(isinstance(pending.get("action_id"), str) and pending["action_id"] and pending["action_id"] not in ids, "no_replay_or_reused_action_identity")
                require(pending.get("governance_ref") == request["accounts"]["G"] and pending.get("basis_ref") == request["accounts"]["basis"], "next_action_accounts_mismatch")
                disposition = "ready_for_current_use"
    except (OSError, ValueError, TypeError, KeyError, AttributeError, RecursionError) as error:
        holds.append(str(error) or type(error).__name__)
        disposition = "hold"
    result = {"schema": 2, "context": context, "selection": None if holds else selection,
              "use": None if holds else use, "candidate_initiatives": list(found),
              "disposition": disposition, "holds": holds, "accounts": accounts,
              "observed_refs": observed, "actuation_grant": False,
              "limits": ["owner_interpretation_and_direct_channel_trust_are_external_premises",
                         "bounded_reads_not_global_atomic_snapshot", "no_retry_or_activation_grant"]}
    result["assessment_id"] = sha256(json.dumps(result, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode()).hexdigest()
    return result
