"""X owns conservative profile accounting. No automatic execution or successor."""
from dataclasses import asdict, is_dataclass
from hashlib import sha256
from modules.formation.execution_basis import Profile


class ProfileExecution:
    def __init__(self, store):
        self.store = store

    def inspect(self, profile: Profile):
        return self.store.read(sha256(("profile:" + profile.identity + ":" + profile.revision).encode()).hexdigest())

    def record_step(self, profile: Profile, current_governance, configuration_current, guard_observations,
                    actual_increment, event, evidence_ref, explicit_start=False):
        """Called for an explicitly initiated bounded step, not a runner. Fail-closed ledger."""
        if profile.gaps() or not current_governance.supported or not current_governance.direct_basis:
            return {"outcome": "hold", "reason": "profile_or_independent_governance_gap"}
        if type(actual_increment) is not int or actual_increment < 0 or not evidence_ref:
            return {"outcome": "hold", "reason": "actuals_or_evidence_missing"}
        if event not in ("reservation", "observation", "deviation", "override", "depletion"):
            return {"outcome": "hold", "reason": "unsupported_profile_event"}
        key = sha256(("profile:" + profile.identity + ":" + profile.revision).encode()).hexdigest()
        old = self.store.read(key)
        if old is None and not explicit_start:
            return {"outcome": "hold", "reason": "explicit_current_profile_selection_missing"}
        # JSON roundtrip comparison includes tuple-valued guards.
        import json
        if old and json.dumps(old["profile"], sort_keys=True) != json.dumps(asdict(profile), sort_keys=True):
            return {"outcome": "hold", "reason": "profile_identity_collision"}
        if old and old["status"] == "terminated":
            return {"outcome": "hold", "reason": "same_profile_cannot_resume"}
        actuals = (old["actuals"] if old else 0) + actual_increment
        terminate = (not configuration_current or any(guard_observations.get(g) is not True for g in profile.guards)
                     or actuals >= profile.limit or event in ("deviation", "override", "depletion"))
        record = {"kind": "profile", "profile": asdict(profile), "actuals": actuals,
                  "status": "terminated" if terminate else "active", "direct_governance_basis": asdict(current_governance.direct_basis) if is_dataclass(current_governance.direct_basis) else current_governance.direct_basis,
                  "events": (old["events"] if old else []) + [{"event": event, "increment": actual_increment, "evidence": evidence_ref}],
                  "E16_use": "claimed_unsupervised_requires_enactment_basis" if profile.claimed_unsupervised else "non_use",
                  "limit": "ledger_is_not_permission_or_unsupervised_qualification"}
        self.store.write(key, record, old)
        return {"outcome": "terminated_return_stepwise" if terminate else "recorded", "record": record}
