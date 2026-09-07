"""I: role-aware human content; all material disclosures survive any renderer."""
from dataclasses import dataclass
import re


@dataclass(frozen=True)
class Span:
    text: str
    role: str
    meaning: str = ""
    needed_for_choice: bool = False


@dataclass(frozen=True)
class Presentation:
    action: Span
    subject: Span
    effects: tuple[str, ...]
    conditions: tuple[str, ...]
    limits: tuple[str, ...]
    alternatives: tuple[str, ...]
    engineering: tuple[str, ...] = ()
    audit_refs: tuple[str, ...] = ()


def ordinary_span(span, is_action=False):
    if span.role == "internal_reference":
        if not span.meaning:
            raise ValueError("internal_identifier_replaces_human_meaning")
        return span.meaning
    if span.role == "domain_identifier":
        if is_action or not span.needed_for_choice or not span.meaning:
            raise ValueError("identifier_is_not_an_action_or_necessary_subject")
        return span.meaning + " " + span.text
    if span.role not in ("action", "subject") or not span.text.strip():
        raise ValueError("missing_human_action_or_subject")
    # Prefix-independent lexical backstop. Role and meaning remain the main discriminator.
    if re.fullmatch(r"[\w.:/\-]*\d[\w.:/\-]*", span.text.strip()) or re.fullmatch(r"[a-fA-F0-9]{32,}", span.text.strip()):
        raise ValueError("opaque_token_requires_explicit_domain_role_and_meaning")
    return span.text


def present(content: Presentation, preferences, depth="ordinary", renderer=None):
    if depth not in ("ordinary", "engineering", "decision", "runtime-audit"):
        raise ValueError("unsupported_presentation_depth")
    action, subject = ordinary_span(content.action, True), ordinary_span(content.subject)
    if not content.effects or not content.limits:
        raise ValueError("material_effect_or_limit_missing")
    text = action + ": " + subject + "."
    for label, values in (("Последствия", content.effects), ("Условия", content.conditions),
                          ("Ограничения", content.limits), ("Варианты", content.alternatives)):
        if values:
            text += "\n" + label + ": " + "; ".join(values) + "."
    if depth == "engineering" and content.engineering:
        text += "\n" + "; ".join(content.engineering)
    if depth == "runtime-audit" and content.audit_refs:
        text += "\nОснования: " + "; ".join(content.audit_refs)
    # Questions and choices come from supplied content, never from guidance mode alone.
    # Progress frequency is consumed by host publication requests, not a scheduler here.
    try:
        rendered = renderer.render(text) if renderer else text
        return rendered if isinstance(rendered, str) and text in rendered else text
    except Exception:
        return text


def addressed_feedback(element_ref, basis_digest, observed_digest, text):
    if not element_ref or not text or basis_digest != observed_digest:
        return {"outcome": "hold", "reason": "feedback_subject_or_basis_unresolved"}
    return {"outcome": "return_to_owner", "element_ref": element_ref, "basis_digest": basis_digest, "text": text}
