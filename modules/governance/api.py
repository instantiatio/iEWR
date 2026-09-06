"""G assesses direct fixture decision evidence; G never issues a grant."""
from dataclasses import asdict, dataclass
import json
from typing import Protocol
from modules.sources.api import Binding, inspect_binding


class GovernanceSourceReader(Protocol):
    def read_source(self, locus: str) -> bytes: ...
    def is_direct_source(self, binding: Binding) -> bool: ...


@dataclass(frozen=True)
class ActionScope:
    target: str
    before: str
    after: str
    performer: str
    receiving_use: str
    method: Binding


@dataclass(frozen=True)
class Assessment:
    supported: bool
    reason: str
    direct_basis: Binding


class Governance:
    def __init__(self, reader: GovernanceSourceReader, clock):
        self.reader, self.clock = reader, clock

    def resolve_relations(self, scope: ActionScope, basis: Binding) -> Assessment:
        try:
            if not self.reader.is_direct_source(basis):
                return Assessment(False, "missing_direct_authority_basis", basis)
            data = json.loads(inspect_binding(self.reader, basis))
            if data.get("version") != 1 or data.get("action") != "replace_exact":
                raise ValueError("unsupported_decision_content")
            for name in ("target", "before", "after", "performer", "receiving_use"):
                if data.get(name) != getattr(scope, name):
                    raise ValueError("decision_scope_mismatch")
            if data.get("method") != asdict(scope.method):
                raise ValueError("decision_method_binding_mismatch")
            # Only exact source identity here; G does not select/qualify a Method.
            inspect_binding(self.reader, scope.method)
            if data.get("permission") is not True or data.get("prohibited") is not False:
                raise ValueError("permission_not_established")
            if data.get("conditions") != []:
                raise ValueError("condition_unresolved")
            now = self.clock()
            if not data["valid_from"] <= now < data["valid_until"]:
                raise ValueError("decision_outside_window")
            if not data.get("authority_basis_ref"):
                raise ValueError("missing_direct_authority_basis")
            return Assessment(True, "direct_fixture_basis_current", basis)
        except (OSError, ValueError, TypeError, KeyError) as error:
            return Assessment(False, str(error), basis)
