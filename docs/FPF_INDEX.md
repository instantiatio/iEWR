# FPF structural index

`navigation/fpf-index.yaml` is the automatically extracted structure of the exact original `external-sources/fpf/FPF-Spec.md`. Paths resolve from the installed project root. Edition, provenance, and SHA-256 appear in the index and are checked against `external-sources/fpf/SOURCE.json`.

## Contents

- `source`: original path, repository/commit, declared version, bytes, SHA-256, and SOURCE.json path/hash.
- `sections`: all Markdown ATX headings outside fenced code and HTML comments, in original order. Each retains its original title, level, parent, an ID from the heading if explicitly recognized, and the full section's location. Lists and tables within a section remain available in its full text; they do not become new sections.
- `location.start_line/end_line`: original line numbers, starting at 1, both endpoints inclusive. The range includes subsections and ends before the next heading of equal or higher level. It is valid only while the original's SHA-256 matches.
- `key`: line address within this exact edition. It is a technical key, not an invented FPF ID. An unnumbered heading has `id: null`; its original title is preserved.
- `declared_type` and `declared_status`: explicitly stated values only, with declaration line and location. Declarations in section text and the table of contents are retained separately, including discrepancies; type/status are not inherited from a parent. An empty list means no declaration was extracted.
- `toc_entries_without_body`: table-of-contents items without a full-section heading. `location: null` indicates no full-text address; the declared status, such as Planned, is preserved.
- `unmatched_toc_metadata`: explicit table-of-contents metadata lines that could not be parsed. If nonempty, check the indicated original lines; the index does not invent the missing result.

A table-of-contents item does not prove that a complete method exists. Title, type, and status do not replace reading the original. The index neither summarizes conditions/dependencies nor recommends selections or local procedures. Task entries and MethodPack are maintained separately.

## Updating FPF with a prepared pair

Current work uses the exact pair already supplied. Reading and applying it require neither running a generator nor Python. Changing the FPF edition is maintenance of the methodological basis under a direct instruction; a new link or file does not itself switch the effective basis.

The main update path is to obtain a **prepared, coherent pair of the original FPF and its structural index**. It must include the exact edition and provenance (`SOURCE.json`), preserved licenses/terms, and sufficient verification grounds for that particular pair. These can be the preparing supplier's inventory and check result with exact bytes/hashes and check scope; a supplier's name or the claim “the index is ready” alone is insufficient. Format and paths must be compatible with the installed iEWR. No new mandatory file or registry is introduced for this purpose.

1. Preserve the previously used original, index, provenance, and necessary grounds, or verify their exact availability. Prepare the new pair separately from the effective one; do not edit the author's original text.
2. With available ADE means, compare the actual bytes/SHA-256 of the original, SOURCE.json, and index against the received package's exact inventory. Check the index's edition, source hash, binding to SOURCE.json, format, and paths. Establish sufficient grounds for structural correctness for these source bytes. A matching source hash in the header does not itself prove that all entries/ranges are correct. If the grounds are unknown or there is incompatibility or a mismatch, hold activation of the new pair; the old suitable pair remains available.
3. Under IE-M004 and A.10.1, check genuinely dependent addresses, pinned hashes/editions, and conditions of use in navigation, MP, and environment metadata. Repair affected items within scope and perform sufficient checks. Previous uses retain their grounds; a new edition does not silently rewrite them.
4. Connect the checked package only within the authorized scope and agreed writing/reading conditions. Read back the result and check actual consistency of original/provenance/index and dependent current entries. Switching several files is not itself an atomic transaction. After interruption, establish actual state first; do not present mixed editions as a ready pair. Apply IE-M004 for environment operations; no separate user mode is needed.

If the prepared pair and grounds are sufficient, **local generation is unnecessary**. A new original without a coherent index does not complete the update. Missing ADE capabilities hold the dependent change of basis, not all independent work using the previous pair.

## Local preparation and checking when Python is available

The supplied generator is a ready tool for package preparation/maintenance. It requires Python; this distribution implements no alternative generator. Its presence does not make Python mandatory for iEWR work or MP updates.

From the installed project root:

```sh
python3 -B tools/build_fpf_index.py
python3 -B tools/build_fpf_index.py --check
```

The generator uses Python's standard library. Specify another working directory with `--root /absolute/project/path`. `--check` writes nothing: it re-extracts the structure and compares the entire index with the current exact source. A mismatch between the original and SOURCE.json stops both commands. There is no automatic FPF download or switch.

When suitable Python is available, use the supplied `--check` for the necessary check of the received pair. This check does not write; do not silently regenerate and replace the received index. Local generation is performed as assigned preparation/maintenance after preserving the previous basis. Generation and structural checking do not establish the new edition's semantic suitability or absence of effects on previous results.

## Reading by address

Find the needed entry by original ID or title words. Check SHA-256/edition, open the indicated line range in the **original**, and read material conditions and necessary specific dependencies. For a structural item such as `C.43:4.2`, also open its parent method `C.43` when needed. Table-of-contents metadata are source information, not a separate suitability judgment.

Example using ordinary ADE tools:

```sh
rg -n 'id: "C.43:4.2"' navigation/fpf-index.yaml
sed -n '89668,89677p' external-sources/fpf/FPF-Spec.md
```

The example numbers refer to the supplied edition `c3b34de07a6bd2df85c7081a4c367fd09978079c`; for another edition, take the range from its index.
