"""P implements separate read-only S and write-capable E ports."""
from hashlib import sha256
import json
from pathlib import Path
import sys
from adapters.filesystem import repertoire_engine as engine
from modules.effects.operations import OperationReceipt


class RepertoireReader:
    def __init__(self, root):
        self.root = root

    def inspect(self, locus, scope):
        return engine.inspect_source(self.root, locus, scope)

    def candidates(self):
        return engine.list_repertoire(self.root, "both")

    def verify(self, scope, source_id, edition_id, digest):
        return engine.verify_binding(self.root, scope, source_id, edition_id, digest)


class RepertoireActuator:
    def __init__(self, tree):
        # Tree has independently constrained root to the authorized fixture space.
        self.tree = tree

    def configuration(self):
        return {"status": "compensated", "python": sys.version,
                "engine_sha256": sha256(Path(engine.__file__).read_bytes()).hexdigest(),
                "limit": "POSIX no-follow/locking and exact source checks; single cooperative writer; no host sandbox"}

    def perform(self, scope, guard):
        try:
            if scope.targets != ("project/dpf/REPERTOIRE.yaml",):
                raise ValueError("unsupported_effect_targets")
            args = engine._decode_json(scope.parameters_json.encode("utf-8"))
            current = lambda: self.tree.current_parent("project/dpf/REPERTOIRE.yaml", parent) and guard()
            with self.tree.parent("project/dpf/REPERTOIRE.yaml") as (parent, _):
                if not current():
                    raise ValueError("current_basis_changed")
                if scope.capability == "register_source":
                    if set(args) != {"source_locus", "metadata", "expected_digest", "registration_basis"}:
                        raise ValueError("unsupported_registration_parameters")
                    if not isinstance(args["expected_digest"], str) or not engine.HEX.fullmatch(args["expected_digest"]):
                        raise ValueError("missing_exact_source_digest")
                    result = engine.register(self.tree.root, args["source_locus"], args["metadata"],
                                             args["registration_basis"], args["expected_digest"], current)
                elif scope.capability == "unregister_source":
                    if set(args) != {"source_id", "edition_id", "registration_basis"}:
                        raise ValueError("unsupported_unregistration_parameters")
                    result = engine.unregister(self.tree.root, **args, commit_guard=current)
                else:
                    raise ValueError("unsupported_capability")
            return OperationReceipt("applied", json.dumps(result, ensure_ascii=False, sort_keys=True),
                                    json.dumps(result["effects"], sort_keys=True), result["status"])
        except engine.RepertoireError as error:
            effects = error.effects
            disposition = "partial" if effects.get("repertoire_written") or effects.get("unresolved_temporary_locus") else "not_performed"
            return OperationReceipt(disposition, "{}", json.dumps(effects, sort_keys=True), error.code)
        except ValueError as error:
            return OperationReceipt("not_performed", "{}", '{"repertoire_written": false}', str(error))


class PinnedSourceReader:
    """Trusted input channel supplied by the current host, never inferred from file metadata."""
    def __init__(self, sources, direct_binding, authority_basis_ref):
        self.sources, self.direct_binding = dict(sources), direct_binding
        self.authority_basis_ref = authority_basis_ref

    def read_source(self, locus):
        path = self.sources.get(locus)
        if path is None:
            raise ValueError("source_not_in_current_read_scope")
        path = Path(path)
        try:
            with engine._root_fd(path.parent) as fd:
                return engine._read_file(fd, path.name)
        except engine.RepertoireError as error:
            raise ValueError("source_read_failed: " + error.code) from error

    def is_direct_source(self, binding):
        if binding != self.direct_binding or binding.role != "direct_decision" or not self.authority_basis_ref:
            return False
        try:
            data = engine._decode_json(self.read_source(binding.locus))
        except engine.RepertoireError as error:
            raise ValueError("source_decode_failed: " + error.code) from error
        return data.get("authority_basis_ref") == self.authority_basis_ref
