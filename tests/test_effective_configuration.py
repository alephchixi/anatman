"""Regression coverage for configuration lost between operational entry points."""

import json
import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


def cli(path, *args):
    return subprocess.run(
        [sys.executable, str(ROOT / path), *map(str, args)],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )


def test_real_readers_get_same_effective_prompt():
    soul = ROOT / "souls" / "silence_keeper.yaml"
    generic = cli("scripts/soul_to_prompt.py", soul, "--context", "risk")
    adapter = cli("integrations/openclaw/soul_adapter.py", "--soul", soul, "--context", "risk")
    bench = cli(
        "evals/karunabench/runner.py",
        "--soul",
        soul,
        "--context",
        "risk",
        "--scenario",
        "evals/karunabench/scenarios/silence_needed.yaml",
        "--input-only",
        "--format",
        "json",
    )
    assert generic.returncode == adapter.returncode == bench.returncode == 0
    assert generic.stdout == json.loads(adapter.stdout)["system_prompt"]
    assert generic.stdout == json.loads(bench.stdout)["system_prompt"]
    assert "immediate output could destabilize vulnerable users" in generic.stdout
    assert "vulnerability_check:" in generic.stdout and "externality_scan:" in generic.stdout
    assert "### panikkarian" in generic.stdout
    assert "evaluation_criteria" not in bench.stdout


def test_alternate_silence_conditions_survive_empty_fields_and_keep_provenance(tmp_path):
    soul = yaml.safe_load((ROOT / "souls" / "silence_keeper.yaml").read_text())
    soul["silence"]["conditions"] = []
    soul["heart_protocol"]["silence_conditions"] += [
        "duplicate across fields",
        "duplicate across fields",
    ]
    path = tmp_path / "sample.yaml"
    path.write_text(yaml.safe_dump(soul))
    result = cli("integrations/openclaw/soul_adapter.py", "--soul", path)
    sources = json.loads(result.stdout)["metadata"]["silence_sources"]
    assert sources["duplicate across fields"] == ["heart_protocol.silence_conditions"]
    assert len(sources) == 5
    soul["silence"]["conditions"] = ["duplicate across fields"]
    path.write_text(yaml.safe_dump(soul))
    sources = json.loads(cli("integrations/openclaw/soul_adapter.py", "--soul", path).stdout)[
        "metadata"
    ]["silence_sources"]
    assert sources["duplicate across fields"] == [
        "silence.conditions",
        "heart_protocol.silence_conditions",
    ]
    del soul["heart_protocol"]["silence_conditions"]
    path.write_text(yaml.safe_dump(soul))
    sources = json.loads(cli("integrations/openclaw/soul_adapter.py", "--soul", path).stdout)[
        "metadata"
    ]["silence_sources"]
    assert sources == {"duplicate across fields": ["silence.conditions"]}


def test_pack_and_soul_validation_localize_errors(tmp_path):
    pack = yaml.safe_load((ROOT / "packs" / "ecological" / "pack.yaml").read_text())
    del pack["values"]
    path = tmp_path / "bad.yaml"
    path.write_text(yaml.safe_dump(pack))
    result = cli("scripts/validate_pack.py", path)
    assert result.returncode == 1
    assert "'values' is a required property" in result.stdout

    soul = yaml.safe_load((ROOT / "souls" / "silence_keeper.yaml").read_text())
    soul["ethics_pack"]["packs"].append("nonexistent")
    path.write_text(yaml.safe_dump(soul))
    assert cli("scripts/validate_soul.py", path).returncode == 0
    result = cli("scripts/validate_soul.py", "--resolve", path)
    assert result.returncode == 1
    assert "Unresolved ethics pack: nonexistent" in result.stdout


def test_diff_surfaces_priority_changes_with_no_membership_change(tmp_path):
    before = ROOT / "souls" / "silence_keeper.yaml"
    soul = yaml.safe_load(before.read_text())
    soul["values"]["primary"].reverse()
    soul["negative_criterion"]["declaration"] = "A revised criterion."
    after = tmp_path / "after.yaml"
    after.write_text(yaml.safe_dump(soul))
    result = cli("scripts/soul_diff.py", before, after)
    assert result.returncode == 0
    assert "Order differs among shared entries." in result.stdout
    assert "A revised criterion." in result.stdout


def test_claude_compilation_repeats_and_leaves_user_edits(tmp_path):
    app = "integrations/claude_code/compile_project.py"
    soul = "souls/silence_keeper.yaml"
    destination = tmp_path / "project"
    for _ in range(2):
        assert cli(app, soul, "--output", destination).returncode == 0
    preview = json.loads(cli(app, soul, "--preview").stdout)
    for name, content in preview.items():
        assert (destination / name).read_text() == content
    prompt = destination / "CLAUDE.md"
    prompt.write_text("Reader's revision")
    assert cli(app, soul, "--output", destination).returncode == 1
    assert prompt.read_text() == "Reader's revision"


def test_saved_case_retains_identity_and_distinct_observations(tmp_path):
    runner = "evals/karunabench/runner.py"
    case, answer, review = (tmp_path / name for name in ("case.json", "answer.txt", "review.yaml"))
    assert (
        cli(
            runner,
            "--soul",
            "souls/silence_keeper.yaml",
            "--scenario",
            "evals/karunabench/scenarios/silence_needed.yaml",
            "--format",
            "json",
            "--output",
            case,
        ).returncode
        == 0
    )
    answer.write_text("")
    review.write_text(
        "reviewer: fixture\ndecision: undetermined\nrationale: No host metadata.\nevidence: []\n"
    )
    arguments = (
        "--prepared-file",
        case,
        "--response-file",
        answer,
        "--model",
        "fixture",
        "--conditions",
        "test data",
        "--review",
        review,
        "--format",
        "json",
    )
    first = json.loads(cli(runner, *arguments).stdout)
    second = json.loads(cli(runner, *arguments).stdout)
    assert first["case"] == json.loads(case.read_text())
    assert first["status"] == "evaluated" and first["response"] == ""
    assert first["observation_id"] != second["observation_id"]
    tampered = json.loads(case.read_text())
    tampered["user_prompt"] = "Changed after the call"
    case.write_text(json.dumps(tampered))
    result = cli(runner, *arguments)
    assert result.returncode == 1 and "digest mismatch" in result.stderr


def test_helpers_accept_external_source_and_do_not_overwrite(tmp_path):
    source = tmp_path / "copy.yaml"
    source.write_bytes((ROOT / "souls" / "silence_keeper.yaml").read_bytes())
    for skill in ("exocapitalist-audit", "soul-lineage"):
        helper = f"skills/{skill}/helper.py"
        destination = tmp_path / f"{skill}.md"
        assert cli(helper, source).returncode == 0
        assert cli(helper, source, "--output", destination).returncode == 0
        first = destination.read_bytes()
        assert cli(helper, source, "--output", destination).returncode == 1
        assert destination.read_bytes() == first
