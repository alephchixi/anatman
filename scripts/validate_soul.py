#!/usr/bin/env python3
import argparse
import sys
from pathlib import Path

try:
    import yaml
except ImportError as exc:
    print(f"Missing dependency: {exc}. Install requirements.txt.", file=sys.stderr)
    sys.exit(2)

try:
    from jsonschema import Draft202012Validator
except ImportError as exc:
    print(f"Missing dependency: {exc}. Install requirements.txt.", file=sys.stderr)
    sys.exit(2)


def load_yaml(path: Path):
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def validate_file(path: Path, schema_obj):
    try:
        soul = load_yaml(path)
    except Exception as exc:
        return [f"YAML parse error: {exc}"]

    validator = Draft202012Validator(schema_obj)
    errors = sorted(validator.iter_errors(soul), key=lambda e: list(e.path))
    formatted = []
    for err in errors:
        where = ".".join([str(p) for p in err.path]) or "<root>"
        formatted.append(f"{where}: {err.message}")
    return formatted


def main():
    parser = argparse.ArgumentParser(description="Validate Anatman soul YAML files.")
    parser.add_argument("files", nargs="+", help="One or more soul YAML files")
    parser.add_argument(
        "--schema",
        default="specs/soul.schema.yaml",
        help="Path to soul schema (default: specs/soul.schema.yaml)",
    )
    args = parser.parse_args()

    schema_path = Path(args.schema)
    if not schema_path.exists():
        print(f"Schema not found: {schema_path}", file=sys.stderr)
        sys.exit(2)

    schema = load_yaml(schema_path)

    any_fail = False
    for file_arg in args.files:
        p = Path(file_arg)
        if not p.exists():
            any_fail = True
            print(f"FAIL {p}: file not found")
            continue

        errs = validate_file(p, schema)
        if errs:
            any_fail = True
            print(f"FAIL {p}")
            for e in errs:
                print(f"  - {e}")
        else:
            print(f"PASS {p}")

    sys.exit(1 if any_fail else 0)


if __name__ == "__main__":
    main()
