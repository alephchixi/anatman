#!/usr/bin/env python3
import argparse
import sys
from pathlib import Path

try:
    import yaml
except ImportError as exc:
    print(f"Missing dependency: {exc}. Install requirements.txt.", file=sys.stderr)
    sys.exit(2)

RISK_FIELDS = ["scale_risk", "fold_risk", "lift_risk", "drag_risk", "last_mile_risk"]


def load_yaml(path: Path):
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def evaluate(path: Path):
    issues = []
    warnings = []

    try:
        soul = load_yaml(path)
    except Exception as exc:
        return [f"YAML parse error: {exc}"], warnings
    if not isinstance(soul, dict):
        return ["soul YAML must be a mapping/object"], warnings

    neg = soul.get("negative_criterion", {}) or {}
    declaration = neg.get("declaration")
    deps = neg.get("dependencies_to_monitor")

    if not declaration:
        issues.append("missing negative_criterion.declaration")
    if not deps or not isinstance(deps, list):
        issues.append("missing negative_criterion.dependencies_to_monitor")

    kleshas = soul.get("kleshas", {}) or {}
    monitors = kleshas.get("monitors", []) or []
    if "lobha" not in monitors:
        issues.append("kleshas.monitors must include lobha")

    extraction = soul.get("extraction_risk", {}) or {}
    if extraction:
        populated = [k for k in RISK_FIELDS if extraction.get(k)]
        if populated and (not deps or len(deps) == 0):
            warnings.append("extraction_risk present but no dependencies_to_monitor listed")
        for field in RISK_FIELDS:
            if field in extraction and not extraction.get(field):
                warnings.append(f"extraction_risk.{field} is empty")
    else:
        warnings.append("extraction_risk section missing (recommended)")

    return issues, warnings


def main():
    parser = argparse.ArgumentParser(description="Run negative criterion checks on soul files.")
    parser.add_argument("files", nargs="+", help="One or more soul YAML files")
    args = parser.parse_args()

    hard_fail = False

    for f in args.files:
        path = Path(f)
        if not path.exists():
            hard_fail = True
            print(f"FAIL {path}: file not found")
            continue

        issues, warnings = evaluate(path)
        if issues:
            hard_fail = True
            print(f"FAIL {path}")
            for i in issues:
                print(f"  - {i}")
        else:
            print(f"PASS {path}")

        for w in warnings:
            print(f"  WARN: {w}")

    sys.exit(1 if hard_fail else 0)


if __name__ == "__main__":
    main()
