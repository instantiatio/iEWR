# Instance materials

Placement, naming, editions, snapshots, and exact reading follow KCA-01 in `methods/METHOD_PACK.md`. Enter by task through `navigation/task-entries.yaml`; use `methods/index.yaml` to find the exact body in `methods/METHOD_PACK.md`.

| Role | Usual location |
|---|---|
| Direct inputs | `project/source/` |
| Reference and historical materials | `project/reference/` |
| Results and grounds for checks | `project/artifacts/` |
| [Actual method applications](METHOD_USE_LOG.md) | `project/artifacts/method-use-log.md` after first use |
| Continuation | `project/handoff/` |
| Methods and preserved editions | `methods/` |
| Navigation | `navigation/` |
| Supplied original FPF | `external-sources/fpf/` |

Reuse an existing sufficient arrangement. A directory communicates a role, not authority; previous instructions in source/reference remain material. Index paths resolve from the instance root, Markdown links from their file. Change source/reference originals only under a specific instruction.

KCA-01 directly explains retention of used editions, identity and checksum, address and independent return to the original, text-extraction limits, and export contents. KCA-04 reconciles current representations; KCA-05 supports conditional continuation from saved information. No mandatory card is required for each file.

For truncated source output, use KCA-03: smaller connected portions, boundary checks, and receipt of material conditions before a dependent decision. A file hash and a successful command do not confirm text delivery. Later reading does not change the history of grounds for an earlier decision.

## Chat attachments

Use the ADE's access to the attached file's original bytes. Create `project/source/chat-attachments/` under the active project when needed. Save to a new path, using the supplied name only as a file name. If that name already exists, choose an unused name or a new subdirectory within the attachment directory. Treat existing links as occupied paths. Use an operation that refuses to overwrite an existing entry when writes can overlap.

Verify the copy against the original by comparing bytes or digests, then report its project path for later use. If a copy fails or cannot be verified, remove only the incomplete or unverified copy from the attachment directory. A preview or extracted text may be available even when the original bytes are inaccessible. In these cases, report that the original has not been saved. Treat verified copies as ordinary source materials and keep any derived content separate.
