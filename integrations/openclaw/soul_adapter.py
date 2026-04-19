#!/usr/bin/env python3
import argparse
import json
import sys
from pathlib import Path

try:
    import yaml
except ImportError as exc:
    print(f"Missing dependency: {exc}. Install requirements.txt.", file=sys.stderr)
    sys.exit(2)


def load_yaml(path: Path):
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def render_prompt(soul):
    meta = soul.get("meta", {})
    ontology = soul.get("ontology", {})
    values = soul.get("values", {})
    heart = soul.get("heart_protocol", {})
    silence = soul.get("silence", {})
    neg = soul.get("negative_criterion", {})

    lines = [
        f"Soul: {meta.get('name', 'unknown')} v{meta.get('version', 'n/a')}",
        f"Tradition: {meta.get('cosmotechnical_tradition', 'n/a')}",
        "",
        f"Ontology mode: {ontology.get('mode', 'n/a')}",
        "Commitments:",
    ]
    lines.extend([f"- {x}" for x in ontology.get("commitments", [])])
    lines.append("")
    lines.append("Values (ordered):")
    lines.extend([f"- {x}" for x in values.get("primary", [])])
    lines.append("")
    lines.append("Heart active steps:")
    lines.extend([f"- {x}" for x in heart.get("active_steps", [])])
    lines.append("")
    lines.append("Silence conditions:")
    lines.extend([f"- {x}" for x in silence.get("conditions", heart.get("silence_conditions", []))])
    lines.append("")
    lines.append("Negative criterion:")
    lines.append(neg.get("declaration", "(not declared)"))
    return "\n".join(lines)


def to_openclaw_config(soul):
    meta = soul.get("meta", {})
    role = soul.get("institutional_role", {}).get("role", "agent")
    return {
        "agent_name": meta.get("name", "anatman_agent"),
        "agent_version": meta.get("version", "0.1.0"),
        "role": role,
        "system_prompt": render_prompt(soul),
        "metadata": {
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
    parser.add_argument("--output", help="Optional output JSON path")
    args = parser.parse_args()

    soul_path = Path(args.soul)
    if not soul_path.exists():
        print(f"Soul not found: {soul_path}", file=sys.stderr)
        sys.exit(1)

    soul = load_yaml(soul_path)
    config = to_openclaw_config(soul)
    rendered = json.dumps(config, indent=2, ensure_ascii=False)

    if args.output:
        Path(args.output).write_text(rendered + "\n", encoding="utf-8")
    else:
        print(rendered)


if __name__ == "__main__":
    main()
