"""One supplied, independently governed operation. No request authoring or queue."""
import argparse
from dataclasses import asdict
from hashlib import sha256
import json
from pathlib import Path
import sys
import time

if not (sys.flags.isolated and sys.flags.no_site and sys.dont_write_bytecode):
    raise SystemExit("Use python -I -S -B")
PACKAGE = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PACKAGE))
from modules.coordination.api import Coordination
from modules.interaction.api import Interaction
from adapters.filesystem.local import Tree, OwnerStore, LocalEffects
from adapters.filesystem.repertoire import PinnedSourceReader, RepertoireReader, RepertoireActuator
from adapters.filesystem.artifacts import ArtifactActuator
from adapters.presentation.text import TextRenderer
from adapters.agent_host.channel import decode, encode


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workspace", required=True)
    parser.add_argument("--decision", required=True)
    parser.add_argument("--decision-sha256", required=True)
    parser.add_argument("--direct-channel-basis", required=True)
    parser.add_argument("--method", required=True)
    parser.add_argument("--adapter", choices=("repertoire", "artifact"), required=True)
    args = parser.parse_args()
    # Values select qualified ports; the bootstrap never writes a decision or grants authority.
    tree = None
    try:
        basis = decode(json.loads(sys.stdin.buffer.read(1024*1024)))
        if not hasattr(basis, "request") or basis.request.sha256 != args.decision_sha256:
            raise ValueError("exact_direct_decision_binding_required")
        reader = PinnedSourceReader({basis.request.locus: Path(args.decision), basis.method.locus: Path(args.method)},
                                   basis.request, args.direct_channel_basis)
        root = Path(args.workspace).absolute()
        tree = Tree(root, root.parent)
        e = OwnerStore(tree, "effects", "project/process/ewr")
        x = OwnerStore(tree, "execution", "project/process/ewr")
        c = Coordination(reader, reader, time.time, LocalEffects(tree), e, x)
        actuator = RepertoireActuator(tree) if args.adapter == "repertoire" else ArtifactActuator(tree)
        c.attach_operations(RepertoireReader(root), reader, time.time, actuator, e, x)
        i = Interaction(c, TextRenderer())
        result = i.submit("X", "attempt_operation", basis=basis)
        print(json.dumps({"result": encode(result), "limit": "direct_channel_basis_must_be_established_by_actual_host_not_by_this_parameter"}, ensure_ascii=False))
        return 0 if result.outcome in ("done", "reuse") else 2
    except (OSError, ValueError, TypeError, KeyError, AttributeError) as error:
        print(json.dumps({"outcome": "hold", "reason": str(error)}, ensure_ascii=False))
        return 2
    finally:
        if tree is not None:
            tree.close()


if __name__ == "__main__":
    raise SystemExit(main())
