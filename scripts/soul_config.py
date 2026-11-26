"""Resolve the declarations shared by Anātman prompt consumers."""

from pathlib import Path

import yaml
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]


def load_yaml(path):
    try:
        return yaml.safe_load(Path(path).read_text(encoding="utf-8"))
    except yaml.YAMLError as exc:
        raise ValueError(f"{path}: invalid YAML: {exc}") from exc


def schema_errors(value, schema):
    errors = Draft202012Validator(schema).iter_errors(value)
    return sorted(
        f"{'.'.join(map(str, error.absolute_path)) or '<root>'}: {error.message}"
        for error in errors
    )


def silence_sources(soul):
    conditions = {}
    for field, values in (
        ("silence.conditions", soul.get("silence", {}).get("conditions")),
        (
            "heart_protocol.silence_conditions",
            soul.get("heart_protocol", {}).get("silence_conditions"),
        ),
    ):
        for condition in values or []:
            sources = conditions.setdefault(condition, [])
            if field not in sources:
                sources.append(field)
    return conditions


def load_pack(name, root=ROOT):
    if not isinstance(name, str) or not name or Path(name).name != name or name in (".", ".."):
        raise ValueError(f"Invalid ethics pack identifier: {name!r}")
    path = root / "packs" / name / "pack.yaml"
    if not path.is_file():
        raise ValueError(f"Unresolved ethics pack: {name}")
    pack = load_yaml(path)
    if errors := schema_errors(pack, load_yaml(root / "specs" / "pack.schema.yaml")):
        raise ValueError(f"Pack {name}: {'; '.join(errors)}")
    if pack["name"] != name:
        raise ValueError(f"Pack {name}: name must match its identifier")
    return pack


def resolve(soul, *, context="ordinary", root=ROOT):
    if not isinstance(soul, dict):
        raise TypeError("soul YAML must be a mapping/object")
    if context not in ("ordinary", "risk"):
        raise ValueError(f"Unknown deliberation context: {context}")
    heart = soul.get("heart_protocol", {})
    protocol_dir = root / "protocols" / "heart"
    steps = load_yaml(protocol_dir / "heart_protocol.yaml")["steps"]
    silence_protocol = load_yaml(protocol_dir / "silence_protocol.yaml")["silence_protocol"]
    by_name = {step["name"]: step for step in steps}
    active = list(dict.fromkeys(heart.get("active_steps", [])))
    if unknown := [name for name in active if name not in by_name]:
        raise ValueError(f"Unknown heart steps: {', '.join(unknown)}")
    required = [step["name"] for step in steps if step["required"]]
    additions = [name for name in required if name not in active]
    if context == "risk":
        # A high-impact case runs the required protocol in its declared order.
        effective = [step["name"] for step in steps if step["name"] in active or step["required"]]
    else:
        effective = active
    packs = {
        name: load_pack(name, root)
        for name in dict.fromkeys(soul.get("ethics_pack", {}).get("packs", []))
    }
    return {
        "context": context,
        "steps": [by_name[name] for name in effective],
        "risk_additions": additions,
        "silence": silence_sources(soul),
        "silence_protocol": silence_protocol,
        "packs": packs,
    }
