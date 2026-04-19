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


def listify(value):
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]


def compare_list(label, a_list, b_list):
    a_set = set(a_list)
    b_set = set(b_list)
    only_a = sorted(a_set - b_set)
    only_b = sorted(b_set - a_set)

    lines = [f"## {label}"]
    if not only_a and not only_b:
        lines.append("No differences.")
        return lines

    if only_a:
        lines.append("Only in A:")
        lines.extend([f"- {x}" for x in only_a])
    if only_b:
        lines.append("Only in B:")
        lines.extend([f"- {x}" for x in only_b])
    return lines


def main():
    parser = argparse.ArgumentParser(description="Compare two Anatman soul YAML files.")
    parser.add_argument("a", help="First soul YAML")
    parser.add_argument("b", help="Second soul YAML")
    args = parser.parse_args()

    a_path = Path(args.a)
    b_path = Path(args.b)

    if not a_path.exists() or not b_path.exists():
        print("Both files must exist.", file=sys.stderr)
        sys.exit(1)

    a = load_yaml(a_path)
    b = load_yaml(b_path)

    a_meta = a.get("meta", {})
    b_meta = b.get("meta", {})

    out = [
        f"# Soul Diff: {a_meta.get('name', a_path.name)} vs {b_meta.get('name', b_path.name)}",
        "",
        "## Ontological Mode",
        f"A: {a.get('ontology', {}).get('mode', 'n/a')}",
        f"B: {b.get('ontology', {}).get('mode', 'n/a')}",
        "",
    ]

    out.extend(
        compare_list(
            "Ontological Commitments",
            listify(a.get("ontology", {}).get("commitments")),
            listify(b.get("ontology", {}).get("commitments")),
        )
    )
    out.append("")
    out.extend(
        compare_list(
            "Primary Values",
            listify(a.get("values", {}).get("primary")),
            listify(b.get("values", {}).get("primary")),
        )
    )
    out.append("")
    out.extend(
        compare_list(
            "Recognized Tensions",
            listify(a.get("values", {}).get("recognized_tensions")),
            listify(b.get("values", {}).get("recognized_tensions")),
        )
    )
    out.append("")
    out.extend(
        compare_list(
            "Heart Active Steps",
            listify(a.get("heart_protocol", {}).get("active_steps")),
            listify(b.get("heart_protocol", {}).get("active_steps")),
        )
    )
    out.append("")
    out.extend(
        compare_list(
            "Silence Conditions",
            listify(
                a.get("silence", {}).get(
                    "conditions", a.get("heart_protocol", {}).get("silence_conditions")
                )
            ),
            listify(
                b.get("silence", {}).get(
                    "conditions", b.get("heart_protocol", {}).get("silence_conditions")
                )
            ),
        )
    )
    out.append("")
    out.extend(
        compare_list(
            "Klesha Monitors",
            listify(a.get("kleshas", {}).get("monitors")),
            listify(b.get("kleshas", {}).get("monitors")),
        )
    )
    out.append("")

    out.append("## Institutional Role")
    out.append(f"A: {a.get('institutional_role', {}).get('role', 'n/a')}")
    out.append(f"B: {b.get('institutional_role', {}).get('role', 'n/a')}")
    out.append("")

    out.extend(
        compare_list(
            "Ethics Packs",
            listify(a.get("ethics_pack", {}).get("packs")),
            listify(b.get("ethics_pack", {}).get("packs")),
        )
    )

    print("\n".join(out))


if __name__ == "__main__":
    main()
