"""Read-only selected configuration/digest verification; no semantic admission."""
import argparse
import ast
from hashlib import sha256
import json
from pathlib import Path
import re


def verify(root):
    root = Path(root).absolute()
    index_path = root / "app/bootstrap/CONFIGURATION.json"
    index = json.loads(index_path.read_text(encoding="utf-8"))
    if index.get("schema") != 1 or index.get("activation_entry") != "AGENTS.md":
        raise ValueError("unsupported_configuration")
    failures = []
    for locus, expected in index["files"].items():
        parts = Path(locus).parts
        if Path(locus).is_absolute() or any(p in (".", "..") for p in parts):
            raise ValueError("unsafe_configuration_locus")
        path = root
        for part in parts:
            path = path / part
            if path.is_symlink():
                failures.append(locus + ":symlink")
        if not path.is_file() or sha256(path.read_bytes()).hexdigest() != expected:
            failures.append(locus + ":digest")
    allowed = {"sources":set(), "governance":{"sources"}, "effects":{"governance"},
               "reliance":{"sources","governance","effects"}, "formation":{"sources","reliance"},
               "execution":{"formation","governance","effects"}, "recovery":{"sources","formation","governance","execution","effects","reliance"},
               "coordination":{"sources","formation","governance","execution","effects","reliance","recovery"}, "interaction":{"coordination"}}
    for path in (root/"modules").glob("*/*.py"):
        owner=path.parent.name
        for node in ast.walk(ast.parse(path.read_text(encoding="utf-8"))):
            names = [node.module] if isinstance(node,ast.ImportFrom) else [n.name for n in node.names] if isinstance(node,ast.Import) else []
            for name in names:
                if name.startswith(("adapters.","app.","tools.")) or name.startswith("modules.") and name.split(".")[1] not in allowed[owner]|{owner}:
                    failures.append(str(path.relative_to(root))+":forbidden_import:"+name)
    if failures:
        raise ValueError("; ".join(failures))
    return {"configuration_sha256":sha256(index_path.read_bytes()).hexdigest(), "files":len(index["files"]),
            "status":"exact_selected_bytes_and_import_DAG", "limit":"not_agent_behavior_or_authority_or_distribution_admission"}


if __name__ == "__main__":
    parser=argparse.ArgumentParser();parser.add_argument("--root",required=True);args=parser.parse_args()
    print(json.dumps(verify(args.root),ensure_ascii=False,indent=2))
