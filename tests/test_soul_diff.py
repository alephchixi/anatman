# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) Anatman Project Contributors

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "soul_diff.py"
SOUL_A = ROOT / "tests" / "fixtures" / "soul_diff" / "a.yaml"
SOUL_B = ROOT / "tests" / "fixtures" / "soul_diff" / "b.yaml"


def test_soul_diff_reports_key_sections_and_divergences():
    result = subprocess.run(
        [sys.executable, str(SCRIPT), str(SOUL_A), str(SOUL_B)],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 0
    output = result.stdout

    assert "# Soul Diff: alpha_soul vs beta_soul" in output
    assert "## Ontological Mode" in output
    assert "## Primary Values" in output
    assert "Only in A:" in output
    assert "Only in B:" in output
    assert "## Institutional Role" in output
