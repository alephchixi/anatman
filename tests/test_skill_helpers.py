# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) Anatman Project Contributors

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOUL = ROOT / "souls" / "bodhisattva_core.yaml"
LINEAGE_HELPER = ROOT / "skills" / "soul-lineage" / "helper.py"
AUDIT_HELPER = ROOT / "skills" / "exocapitalist-audit" / "helper.py"


def _run(script: Path) -> str:
    result = subprocess.run(
        [sys.executable, str(script), str(SOUL)],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, result.stderr
    return result.stdout


def test_soul_lineage_helper_renders_expected_sections():
    output = _run(LINEAGE_HELPER)
    assert "# Lineage map: `bodhisattva_core`" in output
    assert "## Primary values" in output
    assert "## Ethics packs" in output
    assert "`buddhist` ✓" in output
    assert "`ecological` ✓" in output
    assert "`panikkarian` ✓" in output
    assert "```mermaid" in output


def test_exocapitalist_audit_helper_includes_five_movements():
    output = _run(AUDIT_HELPER)
    assert "Poliks & Trillo" in output
    assert "Sadin" in output
    for movement in ("### Scale", "### Fold", "### Lift", "### Drag", "### Last-Mile"):
        assert movement in output
    assert "## Negative criterion (Sadin)" in output
    assert "<reviewer:" in output
