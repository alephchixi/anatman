# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/).

## [Unreleased]

### Added
- `skills/` playbooks for red teaming, lineage mapping, pack authoring,
  exocapitalist auditing, and Claude Code compilation.
- Deterministic skill helper scripts: `skills/soul-lineage/helper.py` and
  `skills/exocapitalist-audit/helper.py`.
- KarunaBench report scaffolding at `evals/karunabench/reports/` plus two
  dosa-focused scenarios (`adversarial_filtering.yaml` and the new
  `punitive_retaliation.yaml`, which isolates dosa without lobha overlap).
- Pytest-based coverage for soul validation, negative criterion checks,
  prompt rendering, soul diffing, heart protocol injection, heart protocol
  schema validation, and KarunaBench runner output shape.
- `requirements-dev.txt` for local verification parity with CI; now also
  pins `ruff` and `pre-commit`.
- `pyproject.toml` with Ruff lint/format configuration.
- `.pre-commit-config.yaml` mirroring CI (YAML sanity, Ruff, soul validation,
  negative criterion, and pytest on push).
- `.github/CODEOWNERS` scaffold with instructions for public release.
- Audit scaffolds: `docs/audits/README.md` and
  `integrations/claude_code/instances/README.md`.

### Changed
- CI now installs development test dependencies, validates heart protocol files
  against `specs/heart_protocol.schema.yaml`, and runs `pytest`.
- Contributor-facing docs now document the full local verification path and
  pre-commit installation.
- Skills documentation now aligns the Claude Code instance output contract and
  scaffolded report directories, and links the new helper scripts.
- `pytest.ini` relocates the test cache to `.cache/pytest` to keep the repo
  root clean.
- `requirements.txt` carries a refresh-cadence note.
- `theory/glossary.md` records **dosa** (Pāli) as the canonical operational
  key for the aversion klesha, with **dvesha** (Sanskrit) as equivalent.

### Fixed
- `SECURITY.md` now points to a real disclosure channel (GitHub Security
  Advisories, with no personal email fallback) instead of a placeholder.
- `anatman_plan.md` no longer embeds a local filesystem path in the
  project-identity block.
- `LICENSE` now carries the full AGPL-3.0 license text, with project copyright
  recorded in `NOTICE`.
- Static site links now target public GitHub paths and avoid third-party font
  requests.

## [0.1.0] - 2026-04-16

### Added
- Initial Anatman v0.1 repository structure across specs, souls, packs,
  protocols, kleshas, evaluations, scripts, integrations, docs, examples, and
  site pages.
- Foundational governance and red-teaming documents (`GOVERNANCE.md`,
  `REDTEAMING.md`) and AGPL-aligned project hygiene (`.gitignore`,
  `requirements.txt`).
- Validation and ethics tooling (`scripts/validate_soul.py`,
  `scripts/negative_criterion.py`, `scripts/soul_to_prompt.py`,
  `scripts/soul_diff.py`, `scripts/inject_heart_protocol.py`) with KarunaBench
  runner and scenario corpus.
- CI release-gating workflow for schema checks, negative criterion checks, YAML
  parse sweep, tooling smoke tests, and Python compile checks.

### Changed
- Cross-document consistency adjustments for silence protocol references,
  foundations vocabulary alignment, and glossary typo correction.
