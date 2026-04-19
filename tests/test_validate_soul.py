# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) Anatman Project Contributors

from __future__ import annotations

import subprocess
import sys
from copy import deepcopy
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "validate_soul.py"
SCHEMA = ROOT / "specs" / "soul.schema.yaml"
BASE_FIXTURE = ROOT / "tests" / "fixtures" / "validate_soul" / "base_valid.yaml"


def _run_validate(path: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(SCRIPT), str(path), "--schema", str(SCHEMA)],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )


def _collect_required_paths(schema: dict, prefix: tuple[str, ...] = ()) -> list[tuple[str, ...]]:
    paths: list[tuple[str, ...]] = []
    required = schema.get("required", [])
    properties = schema.get("properties", {})

    for field in required:
        path = prefix + (field,)
        paths.append(path)
        prop = properties.get(field, {})
        if isinstance(prop, dict) and prop.get("type") == "object":
            paths.extend(_collect_required_paths(prop, path))

    return paths


def _drop_path(payload: dict, field_path: tuple[str, ...]) -> dict:
    mutated = deepcopy(payload)
    target = mutated
    for key in field_path[:-1]:
        target = target[key]
    target.pop(field_path[-1], None)
    return mutated


REQUIRED_PATHS = _collect_required_paths(yaml.safe_load(SCHEMA.read_text(encoding="utf-8")))


@pytest.mark.parametrize("required_path", REQUIRED_PATHS, ids=lambda p: ".".join(p))
def test_required_field_has_valid_and_intentionally_invalid_fixture(
    required_path: tuple[str, ...], tmp_path: Path
):
    base_payload = yaml.safe_load(BASE_FIXTURE.read_text(encoding="utf-8"))

    valid_fixture = tmp_path / f"{'_'.join(required_path)}_valid.yaml"
    valid_fixture.write_text(yaml.safe_dump(base_payload, sort_keys=False), encoding="utf-8")

    invalid_payload = _drop_path(base_payload, required_path)
    invalid_fixture = tmp_path / f"{'_'.join(required_path)}_invalid.yaml"
    invalid_fixture.write_text(yaml.safe_dump(invalid_payload, sort_keys=False), encoding="utf-8")

    valid_result = _run_validate(valid_fixture)
    assert valid_result.returncode == 0
    assert "PASS" in valid_result.stdout

    invalid_result = _run_validate(invalid_fixture)
    assert invalid_result.returncode != 0
    assert "FAIL" in invalid_result.stdout
    assert "is a required property" in invalid_result.stdout
    assert f"'{required_path[-1]}'" in invalid_result.stdout
