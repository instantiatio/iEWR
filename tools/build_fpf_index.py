#!/usr/bin/env python3
"""Generate structural navigation for the exact supplied FPF, without interpreting it."""
import argparse
import hashlib
import json
from pathlib import Path
import re

SOURCE = "external-sources/fpf/FPF-Spec.md"
PROVENANCE = "external-sources/fpf/SOURCE.json"
OUTPUT = "navigation/fpf-index.yaml"
SCHEMA = 1
HEADING = re.compile(r"^ {0,3}(#{1,6})(?:[ \t]+(.*)|[ \t]*)$")
FENCE = re.compile(r"^ {0,3}(`{3,}|~{3,})(.*)$")
SOURCE_ID = re.compile(
    r"^`?((?:[A-Z]|FPF)(?:\.[A-Za-z0-9_-]+)+(?:\:Annex [A-Z]|\:[A-Za-z0-9_.-]+)?)`?(?=\s|$)"
)
FIELD = re.compile(
    r"^\s*(?:>\s*)?(?:[-*]\s+)?(?:\*\*)?(Type|Status)"
    r"(?:\*\*)?\s*:\s*(?:\*\*)?\s*(.+?)\s*$", re.I
)


def source_id(title):
    match = SOURCE_ID.match(title)
    return match.group(1) if match else None


def visible_lines(lines):
    """Yield source lines outside fenced code and HTML comments, retaining line numbers."""
    fence = None
    comment = False
    for number, raw in enumerate(lines, 1):
        if fence:
            close = re.match(r"^ {0,3}(" + re.escape(fence[0]) + r"{" + str(fence[1]) + r",})\s*$", raw)
            if close:
                fence = None
            continue
        if comment:
            if "-->" in raw:
                comment = False
            continue
        if "<!--" in raw:
            if "-->" not in raw.split("<!--", 1)[1]:
                comment = True
            continue
        match = FENCE.match(raw)
        if match:
            fence = (match.group(1)[0], len(match.group(1)))
            continue
        yield number, raw


def table_cells(line):
    if not line.lstrip().startswith("|"):
        return None
    return [cell.strip() for cell in re.split(r"(?<!\\)\|", line.strip().strip("|"))]


def parse_structure(text):
    lines = text.splitlines()
    visible = list(visible_lines(lines))
    sections = []
    stack = []
    current = None
    for number, raw in visible:
        heading = HEADING.match(raw)
        if heading:
            level = len(heading.group(1))
            title = heading.group(2) or ""
            # ATX closing markers are Markdown syntax, not part of the title.
            title = re.sub(r"\s+#+\s*$", "", title).rstrip()
            while stack and stack[-1]["level"] >= level:
                stack.pop()["location"]["end_line"] = number - 1
            current = {
                "key": f"line-{number}",
                "id": source_id(title),
                "title": title,
                "level": level,
                "parent": stack[-1]["key"] if stack else None,
                "location": {"start_line": number, "end_line": len(lines)},
                "declared_type": [],
                "declared_status": [],
            }
            sections.append(current)
            stack.append(current)
        elif current:
            field = FIELD.match(raw)
            if field:
                current["declared_" + field.group(1).lower()].append({
                    "value": field.group(2), "line": number, "origin": "section_text"
                })

    # ToC declarations are retained separately from section-local declarations.
    # A type/status is never inherited from a parent or inferred from its name.
    toc_ranges = [s["location"] for s in sections if s["title"] == "Table of Contents"]
    by_id = {}
    for section in sections:
        if section["id"]:
            by_id.setdefault(section["id"], []).append(section)
    columns = None
    unmatched = []
    toc_only = []
    for number, raw in visible:
        if not any(r["start_line"] < number <= r["end_line"] for r in toc_ranges):
            continue
        cells = table_cells(raw)
        if cells is None:
            columns = None
            continue
        normalized = [c.casefold() for c in cells]
        if "status" in normalized or "type" in normalized:
            columns = normalized
            continue
        if not columns or all(re.fullmatch(r":?-+:?", c) for c in cells):
            continue
        # The original ToC identifies patterns in its first column.
        declared_id = re.sub(r"[*`]", "", cells[0]).strip()
        if source_id(declared_id) != declared_id:
            # Decorative cluster rows declare neither a pattern ID nor metadata.
            continue
        required_columns = [columns.index(name) for name in ["type", "status"] if name in columns]
        # Pipes in later prose/code cells do not affect the earlier explicit fields.
        if len(cells) <= max(required_columns):
            unmatched.append({"line": number, "reason": "table_column_count", "id_cell": cells[0]})
            continue
        if declared_id not in by_id:
            item = {"id": declared_id, "title": cells[1], "toc_line": number,
                    "location": None, "declared_type": [], "declared_status": []}
            toc_only.append(item)
            targets = [item]
        else:
            targets = by_id[declared_id]
        for name in ["type", "status"]:
            if name in columns:
                value = cells[columns.index(name)]
                if value:
                    for section in targets:
                        section["declared_" + name].append({
                            "value": value, "line": number, "origin": "table_of_contents"
                        })
    return sections, toc_only, unmatched


def build(root):
    provenance_bytes = (root / PROVENANCE).read_bytes()
    provenance = json.loads(provenance_bytes)
    source_bytes = (root / SOURCE).read_bytes()
    digest = hashlib.sha256(source_bytes).hexdigest()
    entries = [v for v in provenance["files"] if v["path"] == "FPF-Spec.md"]
    if len(entries) != 1 or entries[0]["sha256"] != digest or entries[0]["bytes"] != len(source_bytes):
        raise ValueError("FPF bytes do not match SOURCE.json; index generation held")
    sections, toc_only, unmatched = parse_structure(source_bytes.decode("utf-8"))
    return {
        "schema_version": SCHEMA,
        "kind": "source_structure_index",
        "path_base": "project_root",
        "source": {
            "path": SOURCE,
            "repository": provenance["repository"],
            "edition": provenance["commit"],
            "declared_version": provenance.get("declared_version"),
            "sha256": digest,
            "bytes": len(source_bytes),
            "provenance": PROVENANCE,
            "provenance_sha256": hashlib.sha256(provenance_bytes).hexdigest(),
        },
        "generator": "tools/build_fpf_index.py",
        "addressing": "One-based inclusive source line range; includes subordinate headings. Valid only for exact source sha256. key is edition-local, id is null when no explicit source ID was recognized. Metadata keeps literal values and declaration lines; empty lists mean no extracted declaration, not an inferred status/type.",
        "section_count": len(sections),
        "toc_entries_without_body": toc_only,
        "unmatched_toc_metadata": unmatched,
        "sections": sections,
    }


def yaml_text(document):
    """Emit standard YAML with JSON-quoted scalars, using only the Python standard library."""
    def scalar(value):
        return json.dumps(value, ensure_ascii=False)

    def emit(value, indent=0):
        prefix = " " * indent
        if isinstance(value, dict):
            for key, item in value.items():
                if isinstance(item, (dict, list)) and item:
                    yield prefix + key + ":"
                    yield from emit(item, indent + 2)
                else:
                    yield prefix + key + ": " + scalar(item)
        elif isinstance(value, list):
            for item in value:
                if isinstance(item, (dict, list)) and item:
                    yield prefix + "-"
                    yield from emit(item, indent + 2)
                else:
                    yield prefix + "- " + scalar(item)
    return "\n".join(emit(document)) + "\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--check", action="store_true", help="Read-only: compare the index with current exact inputs")
    args = parser.parse_args()
    root = args.root.resolve()
    try:
        document = build(root)
        rendered = yaml_text(document)
        output = root / OUTPUT
        if args.check:
            if output.read_text(encoding="utf-8") != rendered:
                raise ValueError("Index differs from exact current source/generation; regenerate")
        else:
            output.parent.mkdir(parents=True, exist_ok=True)
            # No source mutation. Deterministic derived output can be regenerated.
            temporary = output.with_suffix(".yaml.tmp")
            temporary.write_text(rendered, encoding="utf-8")
            temporary.replace(output)
        print(json.dumps({"passed": True, "mode": "check" if args.check else "generate",
                          "sections": len(document["sections"]),
                          "unmatched_toc_metadata": len(document["unmatched_toc_metadata"]),
                          "source_sha256": document["source"]["sha256"]}))
    except (OSError, ValueError, KeyError, TypeError) as exc:
        parser.exit(1, str(exc) + "\n")


if __name__ == "__main__":
    main()
