"""X consumes direct semantic judgments, never infers Work from a full carrier."""
from dataclasses import dataclass


@dataclass(frozen=True)
class WorkBasisAssessment:
    work_supported: bool
    attribution: str
    gaps: tuple[str, ...]
    limit: str = "relies_on_direct_semantic_judgments_not_independent_semantic_verification"


def assess_work_basis(a13_judgments, a151_judgment, precise_attribution_required=False, f6_judgment=None):
    gaps = []
    a13_fields = ("admitted_system", "local_agential_kind", "criterion", "classification", "obtaining_assignment",
                  "action_scope_situation_window", "adequate_core_evidence")
    if not a13_judgments:
        gaps.append("A13:no_actual_performer")
    for judgment in a13_judgments:
        if judgment.get("owner_verdict") != "supported" or not judgment.get("direct_basis"):
            gaps.append("A13:direct_semantic_judgment")
        gaps.extend("A13:" + field for field in a13_fields if not judgment.get(field))
        if judgment.get("profile_consumed") and not judgment.get("characteristic_profile"):
            gaps.append("A13:consumed_profile")
    a151_fields = ("performance_history", "actual_performers", "obtaining_enactsMethod", "temporal_extent",
                   "locally_declared_obtaining_containing_System_relation", "other_required_direct_facts")
    if a151_judgment.get("owner_verdict") != "supported" or not a151_judgment.get("direct_basis"):
        gaps.append("A151:independent_direct_judgment")
    gaps.extend("A151:" + field for field in a151_fields if not a151_judgment.get(field))
    if set(a151_judgment.get("actual_performers", ())) != {j.get("admitted_system") for j in a13_judgments}:
        gaps.append("A151:performer_binding")
    work_supported = not gaps
    attribution = "not_required"
    if precise_attribution_required:
        attribution = "unresolved"
        f6 = f6_judgment or {}
        if work_supported and f6.get("owner_verdict") == "supported" and all(f6.get(k) for k in
            ("direct_basis", "direct_W_to_RA", "species_occurrence_participants_rule", "holder_is_actual_performer", "assignment_throughout_extent")):
            attribution = "supported"
    return WorkBasisAssessment(work_supported, attribution, tuple(gaps))
