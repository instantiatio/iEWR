"""Read-only re-entry entry. A pinned caller supplies qualified host observations."""
import argparse
from hashlib import sha256
import json
from pathlib import Path
import sys

if not (sys.flags.isolated and sys.flags.no_site and sys.dont_write_bytecode):
    raise SystemExit("Use python -I -S -B")
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from adapters.filesystem.recovery import ReentryReader
from modules.coordination.api import Coordination


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workspace", required=True)
    parser.add_argument("--binding", required=True, help="relative project carrier, not model JSON")
    parser.add_argument("--binding-sha256", required=True)
    parser.add_argument("--direct-channel-basis", required=True)
    args = parser.parse_args()
    try:
        raw = sys.stdin.buffer.read(16 * 1024 * 1024 + 1)
        if len(raw) > 16 * 1024 * 1024:
            raise ValueError("host_input_budget")
        host = json.loads(raw)
        reader = ReentryReader(args.workspace, host["context"], host["observations"], args.direct_channel_basis)
        if not args.binding.startswith(("project/artifacts/", "project/process/", "project/handoff/")):
            raise ValueError("binding_must_be_project_carrier")
        binding = reader.local(args.binding)
        if sha256(binding).hexdigest() != args.binding_sha256:
            raise ValueError("binding_digest_mismatch")
        result = Coordination.recover_reentry(json.loads(binding), reader)
        # Detect drift in the navigation carrier as well as the owner refs.
        if reader.local(args.binding) != binding:
            raise ValueError("binding_changed_during_assessment")
        print(json.dumps(result, ensure_ascii=False))
        return 2 if result["disposition"] == "hold" else 0
    except (OSError, ValueError, TypeError, KeyError, AttributeError) as error:
        print(json.dumps({"schema": 2, "disposition": "hold", "holds": [str(error)],
                          "actuation_grant": False}, ensure_ascii=False))
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
