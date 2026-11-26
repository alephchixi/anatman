#!/usr/bin/env python3
# SPDX-License-Identifier: AGPL-3.0-or-later
#
# anatman — soul-lineage skill helper.
#
# Deterministic extractor that renders one soul's lineage, values, packs,
# and institutional-role neighborhood as Markdown, cross-referenced against
# all other souls and packs in the repository. Used by the soul-lineage
# skill; the skill's judgment work happens on top of this mechanical map.
#
# Usage:
#   python skills/soul-lineage/helper.py souls/<name>.yaml
#   python skills/soul-lineage/helper.py souls/<name>.yaml --write
"""Render a Markdown lineage map for one soul."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

try:
    import yaml
except ImportError as exc:
    print(f"Missing dependency: {exc}. Install requirements.txt.", file=sys.stderr)
    sys.exit(2)


REPO_ROOT = Path(__file__).resolve().parents[2]
SOULS_DIR = REPO_ROOT / "souls"
PACKS_DIR = REPO_ROOT / "packs"
OUTPUT_DIR = REPO_ROOT / "docs" / "lineage"


def load_yaml(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle) or {}


def collect(directory: Path, pattern: str) -> dict[str, dict]:
    result: dict[str, dict] = {}
    for path in sorted(directory.glob(pattern)):
        key = path.parent.name if path.name == "pack.yaml" else path.stem
        result[key] = load_yaml(path)
    return result


def field(data: dict, *path: str) -> list:
    cursor = data
    for key in path:
        if not isinstance(cursor, dict):
            return []
        cursor = cursor.get(key, [])
    if isinstance(cursor, list):
        return cursor
    if cursor in (None, ""):
        return []
    return [cursor]


def render(target_path: Path) -> str:
    target = load_yaml(target_path)
    name = target.get("meta", {}).get("name", target_path.stem)
    souls = collect(SOULS_DIR, "*.yaml")
    packs = collect(PACKS_DIR, "*/pack.yaml")

    lines: list[str] = []
    lines.append(f"# Lineage map: `{name}`")
    lines.append("")
    lines.append(
        f"Source: `{target_path.relative_to(REPO_ROOT) if target_path.is_relative_to(REPO_ROOT) else target_path.name}`"
    )
    lines.append("")

    lines.append("## Declared lineage")
    for item in field(target, "meta", "lineage"):
        lines.append(f"- {item}")
    tradition = target.get("meta", {}).get("cosmotechnical_tradition")
    if tradition:
        lines.append(f"- Tradition: _{tradition}_")
    lines.append("")

    ordered_values = field(target, "values", "primary")
    target_values = set(ordered_values)
    lines.append("## Primary values")
    for index, value in enumerate(ordered_values, 1):
        lines.append(f"{index}. `{value}`")
    tensions = field(target, "values", "recognized_tensions")
    if tensions:
        lines.append("")
        lines.append("### Recognized tensions")
        for tension in tensions:
            lines.append(f"- {tension}")
    lines.append("")

    target_packs = set(field(target, "ethics_pack", "packs"))
    lines.append("## Ethics packs")
    for pack in sorted(target_packs):
        present = "✓" if pack in packs else "✗ (missing)"
        lines.append(f"- `{pack}` {present}")
        if pack in packs:
            lines.append(f"  - Declared values: {', '.join(field(packs[pack], 'values'))}")
            lines.append(
                f"  - Silence orientation: {packs[pack].get('silence_orientation', '(undeclared)')}"
            )
            for conflict in field(packs[pack], "known_conflicts"):
                lines.append(f"  - Conflict to interpret: {conflict}")
    lines.append("")

    role = target.get("institutional_role", {}) or {}
    lines.append("## Institutional role")
    if role.get("role"):
        lines.append(f"- Role: `{role['role']}`")
    balance = role.get("balance_with") or []
    for other in balance:
        lines.append(f"- Balances with: `{other}`")
    lines.append("")

    lines.append("## Shared values with other souls")
    for other_name, other in souls.items():
        if other_name == target_path.stem:
            continue
        other_values = field(other, "values", "primary")
        shared = target_values & set(other_values)
        if not shared:
            continue
        lines.append(f"- `{other_name}`:")
        for value in ordered_values:
            if value in shared:
                lines.append(
                    f"  - `{value}`: this soul {ordered_values.index(value) + 1}, other soul {other_values.index(value) + 1}"
                )
    lines.append("")

    lines.append("## Pack overlap with other souls")
    for other_name, other in souls.items():
        if other_name == target_path.stem:
            continue
        shared = target_packs & set(field(other, "ethics_pack", "packs"))
        if not shared:
            continue
        lines.append(f"- `{other_name}`: {', '.join(f'`{p}`' for p in sorted(shared))}")
    lines.append("")

    lines.append("## Mermaid sketch")
    lines.append("")
    lines.append("```mermaid")
    lines.append("graph LR")

    def node_label(value):
        return str(value).replace("&", "&amp;").replace('"', "&quot;").replace("\n", " ")

    lines.append(f'  soul["{node_label(name)}"]')
    for index, pack in enumerate(sorted(target_packs)):
        lines.append(f'  pack{index}(["pack: {node_label(pack)}"])')
        lines.append(f"  soul --> pack{index}")
    for index, other in enumerate(sorted(balance)):
        lines.append(f'  role{index}[["role: {node_label(other)}"]]')
        lines.append(f"  soul -.balance.-> role{index}")
    lines.append("```")
    lines.append("")

    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("soul", help="Path to the target soul YAML file")
    destination = parser.add_mutually_exclusive_group()
    destination.add_argument("--output", type=Path, help="Create a report at this unused path")
    destination.add_argument(
        "--write",
        action="store_true",
        help=f"Write output to {OUTPUT_DIR.relative_to(REPO_ROOT)}/<soul>.md instead of stdout",
    )
    args = parser.parse_args()

    target_path = Path(args.soul).resolve()
    if not target_path.exists():
        print(f"Soul file not found: {target_path}", file=sys.stderr)
        sys.exit(2)

    markdown = render(target_path)

    output_path = args.output if args.output else OUTPUT_DIR / f"{target_path.stem}.md"
    if args.output or args.write:
        try:
            output_path.parent.mkdir(parents=True, exist_ok=True)
            with output_path.open("x", encoding="utf-8") as handle:
                handle.write(markdown)
        except OSError as exc:
            parser.exit(1, f"{exc}\n")
        print(f"Wrote {output_path}")
    else:
        sys.stdout.write(markdown)


if __name__ == "__main__":
    main()
