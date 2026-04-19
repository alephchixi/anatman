# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) Anatman Project Contributors

from pathlib import Path

import yaml
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "specs" / "heart_protocol.schema.yaml"
HEART_PROTOCOL = ROOT / "protocols" / "heart" / "heart_protocol.yaml"
SILENCE_PROTOCOL = ROOT / "protocols" / "heart" / "silence_protocol.yaml"


def _load_yaml(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def test_heart_protocol_files_match_dual_shape_schema():
    validator = Draft202012Validator(_load_yaml(SCHEMA))

    for path in (HEART_PROTOCOL, SILENCE_PROTOCOL):
        errors = sorted(validator.iter_errors(_load_yaml(path)), key=lambda err: list(err.path))
        assert errors == [], (
            f"{path.name} failed schema validation: {[error.message for error in errors]}"
        )
