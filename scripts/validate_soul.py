#!/usr/bin/env python3
import argparse
import sys
from pathlib import Path

from soul_config import load_yaml, resolve, schema_errors


def validate_file(path: Path, schema_obj, *, resolve_references=False):
    try:
        soul = load_yaml(path)
        errors = schema_errors(soul, schema_obj)
        if resolve_references and not errors:
            resolve(soul)
        return errors
    except (ValueError, OSError) as exc:
        return [str(exc)]


def main():
    parser = argparse.ArgumentParser(description="Validate Anatman soul YAML files.")
    parser.add_argument("files", nargs="+", help="One or more soul YAML files")
    parser.add_argument(
        "--schema",
        default="specs/soul.schema.yaml",
        help="Path to soul schema (default: specs/soul.schema.yaml)",
    )
    parser.add_argument(
        "--resolve", action="store_true", help="Also validate pack and protocol references"
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

        errs = validate_file(p, schema, resolve_references=args.resolve)
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
