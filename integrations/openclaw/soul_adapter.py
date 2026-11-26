#!/usr/bin/env python3
import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "scripts"))

from soul_config import load_yaml, resolve  # noqa: E402
from soul_to_prompt import render_resolved  # noqa: E402


def render_prompt(soul, *, context="ordinary"):
    return render_resolved(soul, resolve(soul, context=context))


def to_openclaw_config(soul, *, context="ordinary"):
    effective = resolve(soul, context=context)
    meta = soul.get("meta", {})
    role = soul.get("institutional_role", {}).get("role", "agent")
    return {
        "agent_name": meta.get("name", "anatman_agent"),
        "agent_version": meta.get("version", "0.1.0"),
        "role": role,
        "system_prompt": render_resolved(soul, effective),
        "metadata": {
            "context": effective["context"],
            "silence_sources": effective["silence"],
            "license": meta.get("license", "AGPL-3.0"),
            "tradition": meta.get("cosmotechnical_tradition"),
            "ethics_packs": soul.get("ethics_pack", {}).get("packs", []),
            "klesha_monitors": soul.get("kleshas", {}).get("monitors", []),
        },
    }


def main():
    parser = argparse.ArgumentParser(
        description="Convert Anatman soul YAML to OpenClaw-like config JSON."
    )
    parser.add_argument("--soul", required=True, help="Path to soul YAML")
    parser.add_argument("--context", choices=["ordinary", "risk"], default="ordinary")
    parser.add_argument("--output", help="Optional output JSON path")
    args = parser.parse_args()

    soul_path = Path(args.soul)
    if not soul_path.exists():
        print(f"Soul not found: {soul_path}", file=sys.stderr)
        sys.exit(1)

    try:
        config = to_openclaw_config(load_yaml(soul_path), context=args.context)
    except (TypeError, ValueError, OSError) as exc:
        parser.exit(1, f"{exc}\n")
    rendered = json.dumps(config, indent=2, ensure_ascii=False)

    if args.output:
        Path(args.output).write_text(rendered + "\n", encoding="utf-8")
    else:
        print(rendered)


if __name__ == "__main__":
    main()
