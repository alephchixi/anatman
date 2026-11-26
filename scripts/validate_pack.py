#!/usr/bin/env python3
"""Validate ethics packs against the version-compatible pack schema."""

import argparse
from pathlib import Path

from soul_config import ROOT, load_yaml, schema_errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("packs", nargs="+", type=Path)
    args = parser.parse_args()
    schema = load_yaml(ROOT / "specs" / "pack.schema.yaml")
    failed = False
    for path in args.packs:
        try:
            errors = schema_errors(load_yaml(path), schema)
        except (ValueError, OSError) as exc:
            errors = [str(exc)]
        print(f"{'FAIL' if errors else 'PASS'} {path}")
        for error in errors:
            print(f"  - {error}")
        failed |= bool(errors)
    return int(failed)


if __name__ == "__main__":
    raise SystemExit(main())
