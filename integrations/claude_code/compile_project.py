#!/usr/bin/env python3
"""Compile an Anātman soul into a native Claude Code project context."""

import argparse
import json
import sys
from hashlib import sha256
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "scripts"))

from soul_config import ROOT, load_yaml, resolve, schema_errors  # noqa: E402
from soul_to_prompt import render_resolved  # noqa: E402


def compile_files(source, context):
    soul = load_yaml(source)
    if errors := schema_errors(soul, load_yaml(ROOT / "specs" / "soul.schema.yaml")):
        raise ValueError("Soul validation failed:\n- " + "\n- ".join(errors))
    config = resolve(soul, context=context)
    prompt = render_resolved(soul, config)
    provenance = {
        "soul": {key: soul["meta"][key] for key in ("name", "version")},
        "soul_sha256": sha256(source.read_bytes()).hexdigest(),
        "context": context,
        "prompt_sha256": sha256(prompt.encode("utf-8")).hexdigest(),
        "steps": [step["name"] for step in config["steps"]],
        "silence_sources": config["silence"],
        "packs": {
            name: sha256((ROOT / "packs" / name / "pack.yaml").read_bytes()).hexdigest()
            for name in config["packs"]
        },
        "protocols": {
            name: sha256((ROOT / "protocols" / "heart" / name).read_bytes()).hexdigest()
            for name in ("heart_protocol.yaml", "silence_protocol.yaml")
        },
    }
    return {
        "CLAUDE.md": prompt,
        "anatman-provenance.json": json.dumps(provenance, indent=2, ensure_ascii=False) + "\n",
    }


def write_project(destination, files):
    for name, content in files.items():
        target = destination / name
        if target.is_symlink() or (
            target.exists()
            and (not target.is_file() or target.read_bytes() != content.encode("utf-8"))
        ):
            raise FileExistsError(f"Project file conflicts with generated content: {target}")
    destination.mkdir(parents=True, exist_ok=True)
    for name, content in files.items():
        target = destination / name
        try:
            with target.open("x", encoding="utf-8") as handle:
                handle.write(content)
        except FileExistsError:
            if target.is_symlink() or target.read_bytes() != content.encode("utf-8"):
                raise


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("soul", type=Path)
    modes = parser.add_mutually_exclusive_group(required=True)
    modes.add_argument("--preview", action="store_true", help="Print the proposed files as JSON")
    modes.add_argument("--output", type=Path, help="Destination project directory")
    parser.add_argument("--context", choices=["ordinary", "risk"], default="ordinary")
    args = parser.parse_args()
    try:
        files = compile_files(args.soul, args.context)
        if args.preview:
            print(json.dumps(files, ensure_ascii=False, indent=2))
        else:
            write_project(args.output, files)
            print(f"Compiled project in {args.output}")
    except (TypeError, ValueError, OSError) as exc:
        parser.exit(1, f"{exc}\n")


if __name__ == "__main__":
    main()
