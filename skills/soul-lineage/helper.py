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
    lines.append(f"Source: `{target_path.relative_to(REPO_ROOT)}`")
    lines.append("")

    lines.append("## Declared lineage")
    for item in field(target, "meta", "lineage"):
        lines.append(f"- {item}")
    tradition = target.get("meta", {}).get("cosmotechnical_tradition")
    if tradition:
        lines.append(f"- Tradition: _{tradition}_")
    lines.append("")

    target_values = set(field(target, "values", "primary"))
    lines.append("## Primary values")
    for value in sorted(target_values):
        lines.append(f"- `{value}`")
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
        shared = target_values & set(field(other, "values", "primary"))
        if not shared:
            continue
        lines.append(f"- `{other_name}`: {', '.join(f'`{v}`' for v in sorted(shared))}")
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
    safe_name = name.replace("-", "_")
    lines.append(f"  {safe_name}[{name}]")
    for pack in sorted(target_packs):
        safe_pack = f"pack_{pack}"
        lines.append(f"  {safe_pack}([pack: {pack}])")
        lines.append(f"  {safe_name} --> {safe_pack}")
    for other in sorted(balance):
        safe_other = f"role_{other}"
        lines.append(f"  {safe_other}[[role: {other}]]")
        lines.append(f"  {safe_name} -.balance.-> {safe_other}")
    lines.append("```")
    lines.append("")

    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("soul", help="Path to the target soul YAML file")
    parser.add_argument(
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

    if args.write:
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        output_path = OUTPUT_DIR / f"{target_path.stem}.md"
        output_path.write_text(markdown, encoding="utf-8")
        print(f"Wrote {output_path.relative_to(REPO_ROOT)}")
    else:
        sys.stdout.write(markdown)


if __name__ == "__main__":
    main()
