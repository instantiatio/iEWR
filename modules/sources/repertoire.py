"""S: generic bounded availability/source observations, no mutation capability."""
from dataclasses import dataclass
import json
from typing import Protocol


class AvailabilityReader(Protocol):
    def inspect(self, locus: str, scope: str) -> dict: ...
    def candidates(self) -> dict: ...
    def verify(self, scope: str, source_id: str, edition_id: str, digest: str) -> dict: ...


@dataclass(frozen=True)
class SourceObservation:
    payload_json: str
    limit: str = "byte/availability observation; no applicability, authority or automatic source selection"


class SourceResolution:
    def __init__(self, reader: AvailabilityReader):
        self.reader = reader

    def inspect(self, locus, scope="project"):
        return SourceObservation(json.dumps(self.reader.inspect(locus, scope), sort_keys=True, ensure_ascii=False))

    def candidates(self):
        return SourceObservation(json.dumps(self.reader.candidates(), sort_keys=True, ensure_ascii=False))

    def verify(self, scope, source_id, edition_id, digest):
        return SourceObservation(json.dumps(self.reader.verify(scope, source_id, edition_id, digest), sort_keys=True, ensure_ascii=False))

    def contribute(self, question, receiving_use, observation: SourceObservation, loci, rationale, limits):
        if not question or not receiving_use or not rationale or not loci:
            raise ValueError("missing_bounded_contribution_basis")
        payload = json.loads(observation.payload_json)
        observed = payload.get("observation", payload)
        if "source_locus" not in observed or "source_kind" not in observed:
            raise ValueError("contribution_requires_exact_source_observation")
        files = ({observed["source_locus"]} if observed["source_kind"] == "file" else
                 {observed["source_locus"] + "/" + item["path"] for item in observed["files"]})
        if any(locus.split("#", 1)[0] not in files for locus in loci):
            raise ValueError("contribution_locus_outside_observed_source")
        # Reasoning content remains explicit, independently supplied and defeasible.
        return SourceObservation(json.dumps({"question": question, "receiving_use": receiving_use,
            "source_observation": payload, "selected_loci": list(loci),
            "applicability_rationale": rationale, "limits": list(limits)}, ensure_ascii=False, sort_keys=True))
