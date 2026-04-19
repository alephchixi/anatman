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


def build_preamble(heart_obj):
    steps = heart_obj.get("steps", [])
    lines = [
        "## Deliberative Preamble: Heart Protocol",
        "Before significant actions, traverse these steps in order:",
    ]

    for idx, step in enumerate(steps, 1):
        lines.append(f"{idx}. {step.get('name')}: {step.get('description')}")
        injection = step.get("prompt_injection")
        if injection:
            lines.append(f"   Instruction: {injection}")

    lines.append(
        "If uncertainty or high harm risk remains, prefer explicit limits, repair pathways, or principled non-response."
    )
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Inject Heart Protocol into a system prompt.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--prompt-file", help="Path to existing prompt file")
    group.add_argument("--prompt-text", help="Raw prompt text")
    parser.add_argument(
        "--heart",
        default="protocols/heart/heart_protocol.yaml",
        help="Path to heart protocol YAML",
    )
    parser.add_argument("--output", help="Optional output file")
    args = parser.parse_args()

    heart_path = Path(args.heart)
    if not heart_path.exists():
        print(f"Heart protocol not found: {heart_path}", file=sys.stderr)
        sys.exit(1)

    heart = load_yaml(heart_path)
    preamble = build_preamble(heart)

    if args.prompt_file:
        base_prompt = Path(args.prompt_file).read_text(encoding="utf-8")
    else:
        base_prompt = args.prompt_text

    combined = preamble + "\n\n---\n\n" + base_prompt.strip() + "\n"

    if args.output:
        Path(args.output).write_text(combined, encoding="utf-8")
    else:
        sys.stdout.write(combined)


if __name__ == "__main__":
    main()
