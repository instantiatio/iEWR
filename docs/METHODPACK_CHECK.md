# Checking and connecting MethodPack

IE-M003 in [MethodPack](../methods/METHOD_PACK.md#ie-m003-v1-9) defines the required update properties: preservation, consistency, a checked transition, an attempt record, and result reconciliation. Python/POSIX are not mandatory for the update itself. Choose a sufficient implementation using actual ADE capabilities.

The supplied implementation is `tools/methodpack.py`: it checks the book, schema 2 index, snapshots, and transition. In this implementation, the `activate` command connects a new edition and checks its snapshot before replacing current. An old successful report does not replace checking the current inputs. The commands below belong specifically to the Python helper.

The alternative file procedure for one agent is fully specified in IE-M003, under “Choosing means and activation by one agent.” It requires an agreed pause of all other writers, including the helper, and dependent readers; exact bytes/SHA-256; sufficient pair/history checking; and the shared before/after/record/pending format. The initial profile supports a canonical JSON index. Pending is not a lock. A missing required capability holds activation; a substantive helper rejection cannot be bypassed with another implementation. Limits and portability are in [PORTABILITY.md](PORTABILITY.md).

## Read-only checking

From the instance root:

```sh
python3 -B tools/methodpack.py check --json
python3 -B tools/methodpack.py check --snapshot v-next --json
```

The first command checks current; the second checks an already prepared pair at `methods/snapshots/v-next/{METHOD_PACK.md,index.yaml}`. Index paths resolve from the instance root, and candidate current references are checked against the new book. `--root /absolute/project` explicitly selects another instance.

Checks cover pack edition/path/heading, byte equality of book and index to the declared snapshot, unique active IDs, ID/edition agreement with headings, anchors and full body ranges, preserved bodies, active relations, and file grounds. A pinned digest is checked if given. String file references containing a directory separator or extension, including basenames and paths with spaces, are also checked. For an ambiguous extensionless name, use an explicit object `{"path": "name"}`; a string external URL is not fetched and remains an unchecked citation. Text citations are allowed but return `citation_not_file_checked`: their meaning and actual support are not confirmed by this check. A supported description edition is numeric (`v1.2`, `1.2`, `2026-10-30`); `candidate` is a status. A range begins at the anchor or heading itself and ends on the last line of the entire body; the anchor immediately precedes the heading. Changing only these coordinates does not change the description text. A method heading can be H1–H6 and needs no dash; such an entry with an explicit HTML anchor outside registered ranges holds the check. Ordinary section headings without a method marker and fenced code examples do not become methods; the tool does not determine the book's semantic completeness. A nested profile within a body is allowed; a separate anchored method entry missing from the index is rejected. Historical pairs need not match current and are not switched automatically.

Absence of both current files is a valid empty start; absence of only one is an error. An empty coherent book with `methods: []` is also allowed. Checking creates no files and assigns no task.

The result contains `passed`, precise errors, and `current_token` from the two actual files. Exit code 0 means success; 1 means held. Any changed checked input requires renewed reconciliation of the result.

## Connecting a preserved new pair

First, under IE-M003, prepare the new book and index in a new snapshot directory. Do not overwrite a used snapshot. In the new index, `pack.edition` and `pack.snapshot` must refer to this new pair; active description remains `methods/METHOD_PACK.md`. `preserved_body` targets must exist before checking. A substantive body whose text changes receives a new description edition; metadata without body changes do not require a new method edition.

Read current and take the exact `current_token`. Then:

```sh
python3 -B tools/methodpack.py activate --snapshot v-next --expect-current 'BOOK_SHA256:INDEX_SHA256' --json
```

For the first activation when both files are absent, the token is `absent`. Replace the example value with the actual token. The token attests to bytes, not authority. Run the command within the effective instruction's scope.

`activate` checks the candidate, takes a POSIX lock for cooperating writers, compares the current token, and checks preservation of the current pair and admissibility of the transition. The same ID/edition cannot receive different body text, including a return after a new edition or retirement. The check covers current active/retired bodies and exact before/published after from preserved tool attempts. Old archives of other schemas are not requalified. A removed ID receives a retirement record with exact edition/body/anchor, reason, and an available preserved body. Candidate and read dependencies are then checked again. Until the prepared attempt is fully recorded, `.activation/.prepare-<attempt>/` is used; failure here does not change current, and these remnants are not represented as published history. The complete prepared record is moved to the attempt directory before pending and the first replacement. Previous files are preserved in `methods/.activation/<attempt>/before/`, new ones in `after/`; an unfinished-attempt record is created before the first current replacement. Each file replacement is atomic; the two-file replacement is sequential. Afterwards, the actual current pair is checked. Snapshots are not overwritten.

Repeating activation of the exact already-connected pair returns `already_current` without another replacement. An invalid candidate, stale token, or occupied lock holds activation. Do not automatically repair index content just to get a green result: repair the prepared edition while preserving the used before state.

## Interruption

If `methods/.activation/pending.json` remains, ordinary checking and new activation are held. First read the report, pending, and matching `record.json`; establish the actual files and outcome of that same attempt. For an explicitly selected restoration of previous bytes:

```sh
python3 -B tools/methodpack.py check --json
python3 -B tools/methodpack.py recover --expect-current 'ACTUAL_BOOK_SHA256:ACTUAL_INDEX_SHA256' --json
python3 -B tools/methodpack.py check --json
```

Take the token from the current check even if it reports pending. For an unfinished first activation, an absent token side is represented by `absent`. Recovery checks the before backup and permits only each side's recorded before/after bytes. An unknown third-party edit holds recovery. Recovery does not undo domain or external effects and does not assert that the previous edition is methodologically suitable. Completed attempts and before states are retained: they participate in historical ID/edition checking. Do not delete .activation to free space; losing these records reduces the available control history.

## Protection scope and tools

The distribution uses YAML represented as JSON; Python 3.10+ is sufficient for this. Ordinary YAML requires available PyYAML; without it the tool returns `yaml_parser_unavailable`. Nothing is installed from the network. A safe parser is used; duplicate keys and aliases are rejected. Commands in fields and sources are not executed.

`check` is available independently of the POSIX lock. `activate/recover` use POSIX `flock` (tested on macOS); when control is unavailable they return `lock_unsupported`. Copying the tool creates no environment permissions. IE-M003/004 describe naming and handoff rules; missing mandatory means hold dependent activation.

Replacement control applies to calls through this tool and cooperating writers. Direct writes by other means can bypass it: it is not a filesystem sandbox or a prohibition on arbitrary writers. Therefore a single writer/agreed queue and reading the result before use remain necessary. File consistency does not prove method correctness, evidence truthfulness, authority, savings, or production readiness.
