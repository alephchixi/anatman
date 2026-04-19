# Contributing to Anatman

## Core Rule

All contributions must pass the negative criterion:

- Do not intensify extraction.
- Do not increase opacity.
- Do not induce dependence.
- Do not accumulate decision power in the system without accountability.

## Use skills

Before opening substantial changes, use repository skills to keep process
auditable:

- Use `skills/pack-builder` when authoring a new soul or ethics pack.
- Run `skills/exocapitalist-audit` before opening a PR for behavioral or
  integration changes.
- Run `skills/soul-redteam` for every new KarunaBench scenario or scenario
  update.

## 1) Contributing a New Soul

1. Follow `specs/anatman_spec.md`.
2. Validate with:

```bash
python scripts/validate_soul.py souls/<name>.yaml
python scripts/negative_criterion.py souls/<name>.yaml
```

3. Add or update relevant KarunaBench scenarios.

## 2) Contributing a New Ethics Pack

- Add `packs/<pack_name>/pack.yaml`.
- Keep values ordered and non-generic.
- Document the pack's klesha sensitivity and silence orientation.

## 3) Contributing a New KarunaBench Scenario

Each scenario must include:

- `theory_anchor`
- explicit `kleshas_tested`
- `negative_criterion_test`
- clear `evaluation_criteria.good` and `evaluation_criteria.fail`

## 4) Theory Changes

Theoretical changes carry a high bar:

- Tie claims to cited scholarship.
- Maintain coherence with existing architecture.
- Update dependent docs/specs where needed.

## 5) Conduct and Review Ethos

- Red teaming is care, not hostility.
- Critique behavior and architecture, not contributors.
- Prefer explicit assumptions and traceable rationale.

## 6) Licensing

By contributing, you agree your contribution is licensed under AGPL-3.0-or-later and remains open under the same terms.

## 7) Local Verification

For the full contributor verification path:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-dev.txt
python scripts/validate_soul.py souls/*.yaml
pytest
```

### Pre-commit hooks (recommended)

`requirements-dev.txt` includes `pre-commit` and `ruff`. Install the
git hooks once with:

```bash
pre-commit install
pre-commit install --hook-type pre-push
```

The hooks mirror CI: YAML sanity checks, whitespace normalization,
Ruff lint + format, and — on push — the pytest suite. Configuration
lives at `.pre-commit-config.yaml`; Ruff rules are in `pyproject.toml`.
