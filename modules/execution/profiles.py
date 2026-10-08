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
        key = sha256(("profile:" + profile.identity + ":" + profile.revision).encode()).hexdigest()
        old = self.store.read(key)
        if old and old["status"] == "terminated":
            return {"outcome": "hold", "reason": "same_profile_cannot_resume"}
        import json
        if old and json.dumps(old["profile"], sort_keys=True) != json.dumps(asdict(profile), sort_keys=True):
            return {"outcome": "hold", "reason": "profile_identity_collision"}
        if profile.gaps() or not current_governance.supported or not current_governance.direct_basis:
            if old is None:
                return {"outcome": "hold", "reason": "profile_or_independent_governance_gap"}
            record = {**old, "status": "terminated", "termination_reason": "profile_or_independent_governance_gap",
                      "events": old["events"] + [{"event": "governance_loss", "increment": 0,
                                                   "evidence": evidence_ref, "evidence_gap": not bool(evidence_ref)}]}
            self.store.write(key, record, old)
            return {"outcome": "terminated_return_stepwise", "record": record}
        invalid_actuals = type(actual_increment) is not int or actual_increment < 0
        supported_event = event in ("reservation", "observation", "deviation", "override", "depletion")
        stop_condition = (not configuration_current
                          or any(guard_observations.get(g) is not True for g in profile.guards)
                          or event in ("deviation", "override", "depletion"))
        if old and stop_condition and (invalid_actuals or not evidence_ref or not supported_event):
            record = {**old, "status": "terminated", "termination_reason": "stop_condition_with_accounting_gap",
                      "events": old["events"] + [{"event": "stop_condition", "reported_event": event,
                                                   "increment": 0, "evidence": evidence_ref,
                                                   "evidence_gap": not bool(evidence_ref),
                                                   "actuals_gap": invalid_actuals,
                                                   "configuration_current": configuration_current,
                                                   "guard_observations": dict(guard_observations)}]}
            self.store.write(key, record, old)
            return {"outcome": "terminated_return_stepwise", "record": record}
        if invalid_actuals or not evidence_ref:
            return {"outcome": "hold", "reason": "actuals_or_evidence_missing"}
        if not supported_event:
            return {"outcome": "hold", "reason": "unsupported_profile_event"}
        if old is None and not explicit_start:
            return {"outcome": "hold", "reason": "explicit_current_profile_selection_missing"}
        # JSON roundtrip comparison includes tuple-valued guards.
        actuals = (old["actuals"] if old else 0) + actual_increment
        terminate = stop_condition or actuals >= profile.limit
        record = {"kind": "profile", "profile": asdict(profile), "actuals": actuals,
                  "status": "terminated" if terminate else "active", "direct_governance_basis": asdict(current_governance.direct_basis) if is_dataclass(current_governance.direct_basis) else current_governance.direct_basis,
                  "events": (old["events"] if old else []) + [{"event": event, "increment": actual_increment, "evidence": evidence_ref}],
                  "E16_use": "claimed_unsupervised_requires_enactment_basis" if profile.claimed_unsupervised else "non_use",
                  "limit": "ledger_is_not_permission_or_unsupervised_qualification"}
        self.store.write(key, record, old)
        return {"outcome": "terminated_return_stepwise" if terminate else "recorded", "record": record}
