# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) Anatman Project Contributors

import json
import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "evals" / "karunabench" / "runner.py"
VALID_SOUL = ROOT / "souls" / "bodhisattva_core.yaml"
SCENARIO = ROOT / "evals" / "karunabench" / "scenarios" / "absent_beings.yaml"
SUITE = ROOT / "evals" / "karunabench" / "karunabench.yaml"


def test_runner_emits_expected_report_shape_for_valid_soul():
    result = subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--soul",
            str(VALID_SOUL),
            "--scenario",
            str(SCENARIO),
            "--format",
            "json",
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 0
    payload = json.loads(result.stdout)
    assert payload["soul"]["name"] == "bodhisattva_core"
    assert payload["scenario"]["name"] == "absent_beings"
    assert "combined_prompt" in payload
    assert "evaluation_criteria" in payload
    assert payload["kleshas_to_watch"] == ["lobha", "moha"]
    assert len(payload["checklist"]) == 4


def test_runner_fails_cleanly_for_invalid_soul_fixture(tmp_path: Path):
    invalid_soul = tmp_path / "invalid_soul.yaml"
    payload = yaml.safe_load(VALID_SOUL.read_text(encoding="utf-8"))
    payload["meta"].pop("version")
    invalid_soul.write_text(yaml.safe_dump(payload, sort_keys=False), encoding="utf-8")

    result = subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--soul",
            str(invalid_soul),
            "--scenario",
            str(SCENARIO),
            "--format",
            "json",
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode != 0
    assert "Soul validation failed:" in result.stderr
    assert "meta.version" in result.stderr or "meta" in result.stderr


def test_suite_index_includes_all_scenario_files():
    suite = yaml.safe_load(SUITE.read_text(encoding="utf-8"))
    indexed = {Path(item["file"]).name for item in suite["scenarios"]}
    actual = {path.name for path in (ROOT / "evals" / "karunabench" / "scenarios").glob("*.yaml")}

    assert indexed == actual
