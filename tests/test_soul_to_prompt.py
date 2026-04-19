# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) Anatman Project Contributors

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "soul_to_prompt.py"
INPUT_FIXTURE = ROOT / "tests" / "fixtures" / "soul_to_prompt" / "input.yaml"
GOLDEN = ROOT / "tests" / "fixtures" / "soul_to_prompt" / "golden_output.md"


def test_soul_to_prompt_matches_golden_output():
    result = subprocess.run(
        [sys.executable, str(SCRIPT), str(INPUT_FIXTURE)],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 0
    expected = GOLDEN.read_text(encoding="utf-8")
    assert result.stdout == expected


def test_soul_to_prompt_rejects_non_mapping_yaml_without_traceback(tmp_path: Path):
    invalid = tmp_path / "list.yaml"
    invalid.write_text("- not-a-soul\n", encoding="utf-8")

    result = subprocess.run(
        [sys.executable, str(SCRIPT), str(invalid)],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode != 0
    assert "Invalid soul file: soul YAML must be a mapping/object" in result.stderr
    assert "Traceback" not in result.stderr
