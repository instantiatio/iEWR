"""S: exact source identity only; no discovery/registration route in B1."""
from dataclasses import dataclass
from hashlib import sha256
from typing import Protocol


@dataclass(frozen=True)
class Binding:
    locus: str
    sha256: str
    role: str


class SourceReader(Protocol):
    def read_source(self, locus: str) -> bytes: ...


def inspect_binding(reader: SourceReader, binding: Binding) -> bytes:
    value = reader.read_source(binding.locus)
    if sha256(value).hexdigest() != binding.sha256:
        raise ValueError("source_binding_changed")
    return value
