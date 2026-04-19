# Execution Status

This document tracks implementation status for `anatman_plan.md`.

## Completed Work

1. Repository initialized with git (`main` branch).
2. Required directory scaffold confirmed present:
   - specs, souls, heart protocols, packs, kleshas, evals, scripts, integrations, docs, examples, and site
3. Cross-document consistency fixes applied:
   - `silence_protocol` references aligned to YAML plan target.
   - Foundations vocabulary aligned with planned schema naming.
   - Glossary typo corrected.
4. Missing referenced governance documents added:
   - `GOVERNANCE.md`
   - `REDTEAMING.md`
5. License text normalized to clear AGPL-3.0-or-later declaration.
6. Basic Python dependency file added (`requirements.txt`).
7. Project hygiene baseline added (`.gitignore`).
8. All files marked `[CREATE]` in `anatman_plan.md` have been implemented.
9. Verification commands run successfully for schema validation, negative criterion checks, prompt rendering, soul diff, and KarunaBench runner generation.
10. Release onboarding docs improved with explicit local Python environment setup.
11. CI pipeline added at `.github/workflows/ci.yml` to run validation and smoke checks on push and pull requests.

## Skills

- [x] `soul-redteam` (`skills/soul-redteam/SKILL.md`)
- [x] `soul-lineage` (`skills/soul-lineage/SKILL.md`)
- [x] `pack-builder` (`skills/pack-builder/SKILL.md`)
- [x] `exocapitalist-audit` (`skills/exocapitalist-audit/SKILL.md`)
- [x] `soul-to-claude` (`skills/soul-to-claude/SKILL.md`)

## Public Release Polish

- [x] `SECURITY.md` disclosure channel filled in (GitHub Security Advisories, no personal email fallback).
- [x] `theory/glossary.md` Pāli/Sanskrit klesha note added (dosa/dvesha).
- [x] Personal filesystem path removed from `anatman_plan.md`.
- [x] Dosa-only KarunaBench scenario (`punitive_retaliation.yaml`).
- [x] Scaffold directories populated (`docs/audits/`, `integrations/claude_code/instances/`).
- [x] `pyproject.toml` + `.pre-commit-config.yaml` + Ruff/pre-commit in `requirements-dev.txt`.
- [x] `.github/CODEOWNERS` configured for `@emezzzzzzz`.
- [x] Skill helper scripts for `soul-lineage` and `exocapitalist-audit`.
- [x] `pytest.ini` cache relocated to `.cache/pytest`; `.gitignore` updated.
- [x] Full AGPL-3.0 license text restored in `LICENSE`; project notice added.

## Next Action

1. Enable branch protection on `main` requiring the `CI` workflow.
2. Create the `v0.1.0` release tag.
