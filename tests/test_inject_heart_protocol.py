# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) Anatman Project Contributors

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "inject_heart_protocol.py"
HEART_FIXTURE = ROOT / "tests" / "fixtures" / "inject_heart_protocol" / "heart.yaml"


def test_inject_heart_protocol_with_prompt_text():
    result = subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--prompt-text",
            "Base prompt.",
            "--heart",
            str(HEART_FIXTURE),
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 0
    assert "## Deliberative Preamble: Heart Protocol" in result.stdout
    assert "1. pause: Pause before acting." in result.stdout
    assert "2. harm_scan: Identify potential harms." in result.stdout
    assert "---" in result.stdout
    assert "Base prompt." in result.stdout


def test_inject_heart_protocol_missing_file_fails():
    result = subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--prompt-text",
            "Base prompt.",
            "--heart",
            "does/not/exist.yaml",
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode != 0
    assert "Heart protocol not found" in result.stderr
