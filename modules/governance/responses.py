"""G: exact direct-channel responses. Assessments are never authority grants."""
from dataclasses import asdict, dataclass
from hashlib import sha256
import json
import re
from typing import Protocol


@dataclass(frozen=True)
class Question:
    identity: str
    action: str
    subject_digest: str
    receiving_use: str
    decider: str
    authority_basis_ref: str
    presented_ref: str
    delivered_at: int
    valid_until: int
    effect_group: str = ""


@dataclass(frozen=True)
class AnswerDraft:
    question: str
    disposition: str
    exact_span: str
    conditions: tuple[tuple[str, str], ...] = ()
    interpretation: str = "unresolved"


class ResponseSource(Protocol):
    def read_direct_response(self, reference: str, digest: str) -> str: ...


class DecisionResponses:
    def __init__(self, source: ResponseSource, store, clock):
        self.source, self.store, self.clock = source, store, clock

    def records(self):
        return self.store.snapshot()

    def assess(self, questions, reference, digest, drafts=(), current_subjects=None, condition_evidence=()):
        try:
            raw = self.source.read_direct_response(reference, digest)
            source = json.loads(raw)
            required = ("identity", "principal", "time", "text", "presented_refs")
            if source.get("schema") != 1 or any(k not in source for k in required):
                raise ValueError("unsupported_direct_response")
            current_subjects = current_subjects or {}
            if len({q.identity for q in questions}) != len(questions):
                raise ValueError("duplicate_question")
            drafts = tuple(drafts)
            # The narrow shorthand is valid only after exactly one presented question.
            if not drafts and len(questions) == 1 and source["text"].strip().lower() in ("да", "нет"):
                drafts = (AnswerDraft(questions[0].identity, "accept" if source["text"].strip().lower() == "да" else "deny",
                                      source["text"].strip(), (), "unambiguous"),)
            if len({d.question for d in drafts}) != len(drafts):
                raise ValueError("duplicate_draft_question")
            key = sha256(("response:" + source["identity"]).encode()).hexdigest()
            old = self.store.read(key)
            input_basis = {"reference": reference, "digest": digest, "questions": [asdict(q) for q in questions],
                           "drafts": [asdict(d) for d in drafts]}
            # Same delivery can be assessed for current effectiveness; immutable historical source is reused.
            if old and json.dumps(old["input_basis"], sort_keys=True) != json.dumps(input_basis, sort_keys=True):
                raise ValueError("response_identity_collision")
            results = []
            for q in questions:
                draft = next((d for d in drafts if d.question == q.identity), None)
                reasons = []
                if not q.action or not q.authority_basis_ref:
                    reasons.append("direct_authority_or_subject_missing")
                if source["principal"] != q.decider:
                    reasons.append("different_decider")
                if not q.presented_ref or q.presented_ref not in source["presented_refs"] or source["time"] < q.delivered_at:
                    reasons.append("early_or_unpresented_response")
                if source["time"] > q.valid_until or self.clock() > q.valid_until:
                    reasons.append("expired_window")
                if current_subjects.get(q.identity) != q.subject_digest:
                    reasons.append("material_basis_drift")
                if draft is None or draft.interpretation != "unambiguous" or not draft.exact_span or draft.exact_span not in source["text"]:
                    reasons.append("ambiguous_or_unsupported_interpretation")
                if draft and draft.disposition not in ("accept", "deny", "conditional", "unresolved"):
                    reasons.append("unsupported_disposition")
                if draft and draft.disposition == "unresolved":
                    reasons.append("unresolved_subject")
                if draft:
                    text = draft.exact_span.lower()
                    negative = bool(re.search(r"\b(не|нет|запрещ\w*|стоп)\b", text))
                    conditional = bool(re.search(r"\b(после|если|при условии)\b", text))
                    positive = bool(re.search(r"\b(да|принима\w*|подходит|соглас\w*|разреш\w*)\b", text))
                    # A conservative language subset, not authority from an agent's confidence label.
                    if (draft.disposition == "accept" and (negative or conditional or not positive)
                        or draft.disposition == "deny" and not negative
                        or draft.disposition == "conditional" and (negative or not conditional or not positive)):
                        reasons.append("draft_meaning_not_supported_by_bounded_response_reader")
                if draft and draft.disposition == "conditional" and not draft.conditions:
                    reasons.append("condition_owner_criterion_missing")
                if draft and draft.disposition != "conditional" and draft.conditions:
                    reasons.append("condition_cannot_be_erased")
                unmet = []
                for owner, criterion in (draft.conditions if draft else ()):
                    matches = [e for e in condition_evidence if e.get("owner") == owner and e.get("criterion") == criterion
                               and e.get("question") == q.identity and e.get("subject_digest") == q.subject_digest
                               and e.get("direct_basis") and e.get("current") is True and e.get("satisfied") is True]
                    if not matches:
                        unmet.append((owner, criterion))
                results.append({"question": q.identity, "receiving_use": q.receiving_use,
                                "disposition": draft.disposition if draft and not reasons else "unresolved",
                                "effective_for_named_use": not reasons and not unmet and draft is not None and draft.disposition in ("accept", "conditional"),
                                "reasons": reasons, "unmet_conditions": unmet, "authority_basis_ref": q.authority_basis_ref,
                                "source_ref": reference, "limit": "assessment_of_direct_response_not_a_grant"})
            # Aggregate wording cannot silently collapse differing owners/windows/conditions.
            if len(questions) > 1 and source["text"].strip().lower() in ("да", "согласен со всеми"):
                homogeneous = (len({(q.decider, q.delivered_at, q.valid_until, q.effect_group) for q in questions}) == 1
                               and bool(questions[0].effect_group) and all(d.disposition == "accept" and not d.conditions for d in drafts)
                               and len(drafts) == len(questions))
                if not homogeneous:
                    for row in results:
                        row.update(disposition="unresolved", effective_for_named_use=False,
                                   reasons=row["reasons"] + ["aggregate_not_one_presented_action"])
            record = {"kind": "response_evidence", "input_basis": input_basis, "source_text": source["text"],
                      "initial_assessment": results, "limit": "historical_response_not_permanent_effectiveness"}
            if old is None:
                self.store.write(key, record, None)
            return {"outcome": "assessed", "delivery": "reused" if old else "recorded", "items": tuple(results)}
        except (OSError, ValueError, TypeError, KeyError) as error:
            return {"outcome": "hold", "reason": str(error)}
