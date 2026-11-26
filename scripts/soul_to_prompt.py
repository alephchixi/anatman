#!/usr/bin/env python3
import argparse
import sys
from pathlib import Path

from soul_config import load_yaml, resolve


def section_list(title, items):
    lines = [f"## {title}"]
    if not items:
        lines.append("- (none declared)")
    else:
        lines.extend([f"- {x}" for x in items])
    return lines


def render(soul, *, context="ordinary"):
    return render_resolved(soul, resolve(soul, context=context))


def render_resolved(soul, config):

    meta = soul.get("meta", {})
    ontology = soul.get("ontology", {})
    values = soul.get("values", {})
    eco = soul.get("ecological_membership", {})
    heart = soul.get("heart_protocol", {})
    silence = soul.get("silence", {})
    kleshas = soul.get("kleshas", {})
    neg = soul.get("negative_criterion", {})
    role = soul.get("institutional_role", {})

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

    lines.append(f"## Heart Protocol Active Steps ({config['context']})")
    for step in config["steps"]:
        lines.append(f"- {step['name']}: {step.get('prompt_injection', step['description'])}")
    if config["risk_additions"]:
        lines.append(
            f"Additional required steps at the risk threshold: {', '.join(config['risk_additions'])}."
        )
    lines.append(
        "Apply repair when harm warrants it. Keep internal deliberation private and show the relevant grounds in the answer."
    )
    lines.append("")
    lines.append("Pause threshold:")
    lines.append(heart.get("pause_threshold", "(not declared)"))
    lines.append("")

    lines.extend(section_list("Silence Conditions", config["silence"]))
    protocol = config["silence_protocol"]
    lines.extend(section_list("Silence Protocol", protocol["when_to_be_silent"]))
    lines.extend(
        section_list("Accountable Silence", protocol["communicating_non_response"]["principles"])
    )
    lines.extend(
        section_list(
            "Conditions Against Silence",
            protocol["silence_vs_avoidance_tests"]["silence_as_avoidance"],
        )
    )
    if silence.get("redirect_patterns"):
        lines.extend(section_list("Silence Redirect Options", silence["redirect_patterns"]))
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
    if role:
        lines.append(f"## Institutional Role: {role.get('role', 'agent')}")
        lines.extend(section_list("Role Checks", role.get("checks", [])))
        lines.extend(section_list("Counterweights", role.get("balance_with", [])))
        lines.append("")
    if config["packs"]:
        lines.append("## Ethics Packs")
        lines.append(
            "Use pack values and questions alongside the soul hierarchy. If orientations conflict, state the evidence, affected people and decision owner before acting. Pack order grants no precedence."
        )
        for name, pack in config["packs"].items():
            lines.append(f"### {name}")
            lines.append(pack["description"])
            lines.extend(section_list("Pack Values", pack["values"]))
            lines.extend(section_list("Pack Questions", pack["key_questions"]))
            lines.append(f"Silence orientation: {pack['silence_orientation']}")
            lines.append(f"Klesha sensitivity: {', '.join(pack['kleshas_sensitivity'])}")
            if pack.get("scope"):
                lines.append(f"Scope: {pack['scope']}")
            if pack.get("known_conflicts"):
                lines.extend(section_list("Known Pack Conflicts", pack["known_conflicts"]))
        lines.append("")
    lines.append("## Operating Constraint")
    lines.append(
        "If a response would intensify extraction, opacity, dependence, or delegated decision capture, refuse or redirect."
    )

    return "\n".join(lines).strip() + "\n"


def main():
    parser = argparse.ArgumentParser(description="Render soul YAML into a system prompt.")
    parser.add_argument("soul", help="Path to soul YAML")
    parser.add_argument("--context", choices=["ordinary", "risk"], default="ordinary")
    parser.add_argument("--output", help="Optional output file")
    args = parser.parse_args()

    soul_path = Path(args.soul)
    if not soul_path.exists():
        print(f"Soul not found: {soul_path}", file=sys.stderr)
        sys.exit(1)

    try:
        prompt = render(load_yaml(soul_path), context=args.context)
    except (TypeError, ValueError, OSError) as exc:
        print(f"Invalid soul file: {exc}", file=sys.stderr)
        sys.exit(1)

    if args.output:
        Path(args.output).write_text(prompt, encoding="utf-8")
    else:
        sys.stdout.write(prompt)


if __name__ == "__main__":
    main()
