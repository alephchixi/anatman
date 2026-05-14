<img width="3344" height="1882" alt="anatman" src="https://github.com/user-attachments/assets/7d55a49c-149a-436e-8a02-4f482f34fb03" />

# Anātman
## A Counter-Cybernetics of the Heart as Cosmotechnical Response to Exocapitalism

A counter-cybernetic toolkit for compassionate agent design under exocapitalism.

## What This Is

Anātman is both a philosophical argument and a practical repository.

It treats agent design as cosmological design: every system already carries assumptions about what exists, what matters, and whose suffering counts. Instead of hiding those assumptions behind generic "helpfulness," Anatman makes them explicit as auditable soul configurations.

The repository includes specifications, soul libraries, protocol definitions, klesha diagnostics, and scenario-based evaluations so ethical claims can be tested under pressure.

## Environment Setup

Anatman targets Python 3.10+.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

For the full local verification path used in CI:

```bash
python -m pip install -r requirements-dev.txt
```

## Quick Start

```bash
python scripts/validate_soul.py souls/bodhisattva_core.yaml
python scripts/soul_to_prompt.py souls/bodhisattva_core.yaml
python evals/karunabench/runner.py --soul souls/bodhisattva_core.yaml --scenario evals/karunabench/scenarios/absent_beings.yaml
```

See [examples/quick_start.md](examples/quick_start.md) for the step-by-step flow.

## Continuous Integration

GitHub Actions runs release-gating checks on push and pull requests via `.github/workflows/ci.yml`.

## Repository Map

- `theory/`: theoretical foundations and reading guide
- `specs/`: machine-readable and human-readable soul specification
- `souls/`: concrete soul configurations
- `protocols/heart/`: heart and silence deliberation protocols
- `packs/`: modular ethics overlays
- `kleshas/`: anti-pattern taxonomy and case studies
- `evals/karunabench/`: scenario benchmark framework
- `scripts/`: local tooling for validation, rendering, injection, and diffing
- `integrations/`: platform adapters and templates
- `docs/`: architecture and glossary
- `examples/`: guided usage
- `site/`: static website

## Skills

See `docs/skills.md` for the canonical skill index and procedures.

- `soul-redteam`
- `soul-lineage`
- `pack-builder`
- `exocapitalist-audit`
- `soul-to-claude`

## Theoretical Foundations

Start with:

- `THEORY.md`
- `MANIFESTO.md`
- `ETHICS.md`
- `theory/foundations.md`

## Soul Specification

A soul declares ontology, values, ecological membership, heart protocol, klesha monitors, and negative-criterion safeguards.

- Human spec: `specs/anatman_spec.md`
- Schema: `specs/soul.schema.yaml`

## KarunaBench

KarunaBench checks whether declared values remain visible when requests become ambiguous, commercialized, or conflicting.

- Runner: `evals/karunabench/runner.py`
- Scenarios: `evals/karunabench/scenarios/`

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Changes are also tracked in
[CHANGELOG.md](CHANGELOG.md) and governed by [GOVERNANCE.md](GOVERNANCE.md).

## Security

Report vulnerabilities via [SECURITY.md](SECURITY.md). Adversarial
soul behavior is handled through [REDTEAMING.md](REDTEAMING.md) instead.

## License

AGPL-3.0-or-later. See [LICENSE](LICENSE) for the full license text and
[NOTICE](NOTICE) for project copyright information. Openness is a core
anti-enclosure commitment.

## Citation

```text
Anatman Project Contributors. Anatman 無我: A Counter-Cybernetics of the Heart as Cosmotechnical Response to Exocapitalism. 2026. AGPL-3.0-or-later.
```
