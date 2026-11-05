# Choosing means for MethodPack updates

DMG, FPF, and MP methods are applied through the actual agent execution environment (ADE). Python/POSIX are not mandatory for MP updates. IE-M003 defines preservation, consistency, admissible-transition, and recovery requirements; inadequate means hold the dependent write regardless of implementation language.

## Two implementations

| Work | Supplied Python helper | Limited ADE file path |
|---|---|---|
| MP checking | Python 3.10+, schema 2; supplied JSON or safe YAML when PyYAML is available | Sufficient parsing and all material IE-M003 checks; first profile limited to canonical JSON |
| Activation/restoration | activate/recover require POSIX flock; token, before/after, pending, and rechecking | One agreed writer, all other writers (including helper) and dependent readers paused; actual SHA-256, pair/history checks, same log format |
| Multiple writers | flock coordinates cooperating participants; does not block arbitrary writes | Concurrent writes unsupported: agree on a single writer first, otherwise preserve a separate candidate |
| Partial attempt | With intact receipts, exact before/after permits recover; unknown bytes hold restoration | Same known-side rule; a torn non-atomic write with a third hash holds automatic restoration |
| Connecting a new FPF edition | Prepared coherent original-and-index pair with provenance/terms; Python --check is useful when available | Receive a prepared pair; check binding/bytes and sufficient grounds with ADE means under FPF_INDEX.md; no mandatory local generation |
| Local FPF index generation | tools/build_fpf_index.py requires Python; no flock needed | No alternative generator implemented in this distribution; preparation/maintenance of the basis is separate from current work |

Reuse a suitable supplied helper. The alternative path does not mean ignoring a check error: a damaged candidate, stale basis, or unknown effect remains a blocker. Availability of JavaScript or another runtime does not prove sufficient capabilities. Duplicate keys, invalid paths, missing preserved bodies, and incompatible transitions are not accepted.

## What is actually provided

`enforced` means a working mechanism within its scope; `compensated` means organizational compensation with limits; `unsupported` means the necessary support is absent.

- The Python helper provides its programmatic checks (`enforced`), while flock covers only interaction among cooperating writers. The rule against writing through other means remains a coordination condition.
- In the file path, exact checks, hash comparison, and log creation/reading use available APIs (`enforced` within the tested scope). A single writer and paused readers are `compensated`, not a machine lock. Pending records the attempt and holds compliant readers, but it is not a lock and does not stop a helper that has already entered its operation.
- Arbitrary parallel writers, two-file atomicity, universal recovery of a damaged marker/record, and power-loss resilience are not provided by this description (`unsupported` without additional actual means).

IE-M003 in METHOD_PACK.md contains the exact procedure and before/after/record/pending format. The agent performs activation and recovery within the instruction; no separate new user mode is needed. Attempt history and previous snapshots are retained. A file check does not raise a method's suitability status.

## Formats and portability limits

The MP index is supplied as YAML represented in JSON; the supplied helper needs only Python's standard library for it. The first ADE profile accepts only canonical JSON serialization, checking its exact reserialization; plain JSON.parse does not detect duplicates. Other YAML needs a sufficient safe parser or another method, not silent normalization of the original.

The FPF structural index uses ordinary YAML. Current iEWR work and MP development use the supplied prepared pair; changing MP does not require rebuilding an unchanged FPF index. Obtain a new FPF edition as a prepared coherent package under [FPF_INDEX.md](FPF_INDEX.md), checking bytes, binding, and sufficient grounds. Supplied local generation/repeated structural checking use Python's standard library and are preparation/maintenance operations. Receiving a prepared checked pair does not mandate running these commands.

Choose the alternative method according to actual ADE capabilities. A specific trial using file APIs and an embedded REPL's SHA-256 does not make Node.js a new mandatory distribution dependency. Work without Python/shell/flock calls does not prove actual portability to another OS. If necessary means are missing, reading and a separate candidate remain possible; shared replacement is held.
