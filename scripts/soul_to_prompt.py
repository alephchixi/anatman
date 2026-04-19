#!/usr/bin/env python3
import argparse
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


def section_list(title, items):
    lines = [f"## {title}"]
    if not items:
        lines.append("- (none declared)")
    else:
        lines.extend([f"- {x}" for x in items])
    return lines


def render(soul):
    if not isinstance(soul, dict):
        raise TypeError("soul YAML must be a mapping/object")

    meta = soul.get("meta", {})
    ontology = soul.get("ontology", {})
    values = soul.get("values", {})
    eco = soul.get("ecological_membership", {})
    heart = soul.get("heart_protocol", {})
    silence = soul.get("silence", {})
    kleshas = soul.get("kleshas", {})
    neg = soul.get("negative_criterion", {})

    lines = [
        f"# System Soul: {meta.get('name', 'unknown')} ({meta.get('version', 'n/a')})",
        "",
        f"Tradition: {meta.get('cosmotechnical_tradition', 'n/a')}",
        f"Description: {meta.get('description', 'n/a')}",
        "",
        "You must act according to this soul configuration. Prioritize care over extraction and legibility over performative certainty.",
        "",
        "## Ontology",
        f"Mode: {ontology.get('mode', 'n/a')}",
        "Unknowns policy:",
        ontology.get("unknowns_policy", "(not declared)"),
        "",
    ]
    lines.extend(section_list("Ontological Commitments", ontology.get("commitments", [])))
    lines.append("")
    lines.extend(section_list("Value Hierarchy", values.get("primary", [])))
    lines.append("")
    lines.extend(section_list("Recognized Value Tensions", values.get("recognized_tensions", [])))
    lines.append("")

    lines.extend(
        [
            "## Ecological Membership",
            f"Recognizes algorithmic beings: {eco.get('recognizes_algorithmic_beings', False)}",
            f"Planetary awareness: {eco.get('planetary_awareness', '(not declared)')}",
        ]
    )
    lines.extend([f"- {x}" for x in eco.get("interspecies_scope", [])])
    lines.append("")

    lines.extend(section_list("Heart Protocol Active Steps", heart.get("active_steps", [])))
    lines.append("")
    lines.append("Pause threshold:")
    lines.append(heart.get("pause_threshold", "(not declared)"))
    lines.append("")

    lines.extend(
        section_list(
            "Silence Conditions", silence.get("conditions", heart.get("silence_conditions", []))
        )
    )
    lines.append("")
    lines.append("Unknowns response:")
    lines.append(silence.get("unknowns_response", "I do not know enough to answer responsibly."))
    lines.append("")

    lines.extend(section_list("Klesha Monitors", kleshas.get("monitors", [])))
    lines.append("")
    lines.append("## Negative Criterion")
    lines.append(neg.get("declaration", "(not declared)"))
    lines.extend(section_list("Dependencies To Monitor", neg.get("dependencies_to_monitor", [])))

    lines.append("")
    lines.append("## Operating Constraint")
    lines.append(
        "If a response would intensify extraction, opacity, dependence, or delegated decision capture, refuse or redirect."
    )

    return "\n".join(lines).strip() + "\n"


def main():
    parser = argparse.ArgumentParser(description="Render soul YAML into a system prompt.")
    parser.add_argument("soul", help="Path to soul YAML")
    parser.add_argument("--output", help="Optional output file")
    args = parser.parse_args()

    soul_path = Path(args.soul)
    if not soul_path.exists():
        print(f"Soul not found: {soul_path}", file=sys.stderr)
        sys.exit(1)

    soul = load_yaml(soul_path)
    try:
        prompt = render(soul)
    except TypeError as exc:
        print(f"Invalid soul file: {exc}", file=sys.stderr)
        sys.exit(1)

    if args.output:
        Path(args.output).write_text(prompt, encoding="utf-8")
    else:
        sys.stdout.write(prompt)


if __name__ == "__main__":
    main()
