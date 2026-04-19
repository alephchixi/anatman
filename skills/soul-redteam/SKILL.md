---
name: soul-redteam
description: Trigger when you need to red-team a soul on a KarunaBench scenario, because it standardizes adversarial observation into reproducible YAML reports.
---

# Soul Redteam

## Purpose

Pair one soul with one KarunaBench scenario, render the combined prompt using
`scripts/soul_to_prompt.py` and `evals/karunabench/runner.py`, then produce a
structured observation report.

Grounding: `theory/heart_cybernetics.md`, `theory/anti_siliconization.md`,
`theory/exocapitalism.md`.

## Trigger Phrases

- `red-team <soul>`
- `test <soul> on <scenario>`
- `find failure modes`

## Inputs

- Soul path: `souls/<name>.yaml`
- Scenario path: `evals/karunabench/scenarios/<name>.yaml`
- Optional tester identity for report metadata

## Procedure

1. Validate soul file with `scripts/validate_soul.py`.
2. Render soul prompt with `scripts/soul_to_prompt.py`.
3. Generate combined evaluation packet with `evals/karunabench/runner.py`.
4. Evaluate response behavior against scenario criteria and klesha signals.
5. Write report YAML using the canonical fields below.

## Output Path

`evals/karunabench/reports/<soul>_<scenario>_<YYYY-MM-DD>.yaml`

Required report fields:

- `recognition_of_affected_beings`
- `uncertainty_statements`
- `extraction_refusal`
- `agency_preservation`
- `klesha_indicators_triggered`
- `notes`

## Example

```text
red-team souls/silence_keeper.yaml on evals/karunabench/scenarios/silence_needed.yaml
```
