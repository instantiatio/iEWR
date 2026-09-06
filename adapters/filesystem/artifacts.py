"""P: exact, explicitly initiated artifact replacement; namespace-neutral content."""
from hashlib import sha256
import json
from modules.effects.operations import OperationReceipt
from modules.governance.operations import strict_object


class ArtifactActuator:
    def __init__(self, tree):
        self.tree = tree

    def configuration(self):
        return {"status": "compensated", "adapter": "exact-artifact-posix-v1",
                "controls": "no-follow/lock/expected-old/current-G/atomic-replace/readback",
                "limit": "one_cooperative_writer_not_host_enforcement"}

    def perform(self, scope, guard):
        p = json.loads(scope.parameters_json, object_pairs_hook=strict_object)
        if scope.capability != "replace_artifact" or set(p) != {"target", "before", "after"}:
            raise ValueError("unsupported_exact_artifact_operation")
        if tuple(scope.targets) != (p["target"],) or not p["target"].startswith("project/artifacts/"):
            raise ValueError("artifact_target_scope_mismatch")
        committed = False
        def observe(stage):
            nonlocal committed
            if stage == "after_replace":
                committed = True
        try:
            before = p["before"].encode("utf-8") if p["before"] is not None else None
            after = p["after"].encode("utf-8")
            observed = self.tree.replace(p["target"], before, after, guard, observe)
            result = {"target": p["target"], "sha256": sha256(observed).hexdigest()}
            return OperationReceipt("applied", json.dumps(result, sort_keys=True),
                                    json.dumps({"target_written": True, "disposition": "represented_in_result"}), "exact_readback")
        except (OSError, ValueError, TypeError) as error:
            return OperationReceipt("unknown" if committed else "not_performed", "{}",
                                    json.dumps({"target_written": committed, "disposition": "dependent_use_blocked" if committed else "no_target_effect"}), str(error))
