# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) Anatman Project Contributors

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "negative_criterion.py"
VALID_FIXTURE = ROOT / "tests" / "fixtures" / "negative_criterion" / "valid.yaml"
INVALID_FIXTURE = ROOT / "tests" / "fixtures" / "negative_criterion" / "invalid_missing_lobha.yaml"


def _run(path: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(SCRIPT), str(path)],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )


def test_negative_criterion_valid_fixture_passes():
    result = _run(VALID_FIXTURE)
    assert result.returncode == 0
    assert "PASS" in result.stdout
    assert "FAIL" not in result.stdout


def test_negative_criterion_invalid_fixture_fails_expected_checks():
    result = _run(INVALID_FIXTURE)
    assert result.returncode != 0
    assert "FAIL" in result.stdout
    assert "missing negative_criterion.declaration" in result.stdout
    assert "kleshas.monitors must include lobha" in result.stdout


def test_negative_criterion_rejects_non_mapping_yaml_without_traceback(tmp_path: Path):
    invalid = tmp_path / "list.yaml"
    invalid.write_text("- not-a-soul\n", encoding="utf-8")

    result = _run(invalid)

    assert result.returncode != 0
    assert "soul YAML must be a mapping/object" in result.stdout
    assert "Traceback" not in result.stderr
