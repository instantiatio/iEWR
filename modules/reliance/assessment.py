"""L assesses exact receiving use. No universal verification job or status ladder."""
from dataclasses import dataclass, asdict
from hashlib import sha256


@dataclass(frozen=True)
class Use:
    subject: str
    digest: str
    receiving_use: str
    criterion: str


def assess(use: Use, evidence=(), requirements=(), decision=None, effects=()):
    needs, gaps = [], []
    supported = [e for e in evidence if e.get("subject") == use.subject and e.get("digest") == use.digest
                 and e.get("receiving_use") == use.receiving_use and e.get("criterion") == use.criterion
                 and e.get("direct_basis") and e.get("current") is True and e.get("supports") is True]
    for requirement in requirements:
        if requirement.get("receiving_use") != use.receiving_use:
            continue
        if not requirement.get("owner_basis"):
            gaps.append("requirement_basis_missing")
        elif requirement.get("kind") == "verification":
            if not any(e.get("kind") == "verification_result" and e.get("method") == requirement.get("method") for e in supported):
                needs.append({"question": use.criterion, "subject": use.subject, "digest": use.digest,
                              "receiving_use": use.receiving_use, "method": requirement.get("method"),
                              "owner_basis": requirement["owner_basis"], "route": "return_demand_to_C_no_actuation"})
        elif requirement.get("kind") == "authority_decision":
            if not decision or not all(decision.get(k) == getattr(use, k) for k in ("subject", "digest", "receiving_use")) or not decision.get("direct_basis") or decision.get("effective") is not True:
                gaps.append("exact_use_authority_decision_missing")
        else:
            gaps.append("unsupported_requirement")
    for effect in effects:
        if use.receiving_use in effect.get("dependent_uses", ()) and effect.get("disposition") not in (
                "represented_in_result", "authoritative_external_SoR", "disposable_no_downstream_reliance"):
            gaps.append("unresolved_dependent_effect:" + effect.get("reference", "unknown"))
    if not supported:
        gaps.append("criterion_evidence_missing")
    return {"use": asdict(use), "sufficient": not needs and not gaps, "verification_demands": tuple(needs),
            "gaps": tuple(gaps), "evidence_refs": tuple(e["direct_basis"] for e in supported),
            "decision_ref": decision.get("direct_basis") if decision else None,
            "limit": "assessment_not_observed_reliance_or_permanent_artifact_status"}


class RelianceRecords:
    def __init__(self, store):
        self.store = store

    def observe_reliance(self, use: Use, observation_ref, receiver, observed_at):
        if not observation_ref or not receiver or observed_at is None:
            raise ValueError("actual_receiving_use_observation_missing")
        key = sha256(("reliance:" + observation_ref).encode()).hexdigest()
        record = {"kind": "observed_reliance", "use": asdict(use), "observation_ref": observation_ref,
                  "receiver": receiver, "observed_at": observed_at, "limit": "fact_of_use_not_adequacy_or_authority"}
        old = self.store.read(key)
        if old and old != record:
            raise ValueError("reliance_observation_identity_collision")
        if old is None:
            self.store.write(key, record, None)
        return record
