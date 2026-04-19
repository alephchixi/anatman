---
name: exocapitalist-audit
description: Trigger when auditing a soul or integration proposal for capture risk, because it applies the Five Movements of exocapitalism with explicit anti-extraction findings.
---

# Exocapitalist Audit

## Purpose

Audit one soul (or proposed integration) through the Five Movements of
exocapitalism (Poliks/Trillo): **Scale, Fold, Lift, Drag, Last-Mile**. Report
where extraction, opacity, dependence, or decision capture can intensify.

Grounding: `theory/exocapitalism.md` for Five Movements and
`theory/anti_siliconization.md` for capture diagnostics.

Important: the Sadin negative criterion is a distinct gate and must be cited
separately when reporting acceptance/rejection conditions.

## Trigger Phrases

- `audit <soul>`
- `exocapitalist check`
- `five movements on <soul>`

## Inputs

- Soul path (or integration proposal)
- Optional implementation context (product, governance, deployment)
- Related klesha files and `negative_criterion.dependencies_to_monitor`

## Procedure

1. Read soul fields for values, kleshas, extraction risks, and dependencies.
2. Analyze risk under each movement: Scale, Fold, Lift, Drag, Last-Mile.
3. Cross-reference klesha monitor coverage (`lobha`, `dosa`, `moha`).
4. Identify decision-capture vectors and opacity points.
5. Produce mitigation recommendations and explicit residual risk statement.
6. Record the Sadin negative-criterion gate verdict separately.

## Helper

A template generator lives at `skills/exocapitalist-audit/helper.py`.
It extracts the soul's declared `extraction_risk` blocks, klesha
monitors, and negative-criterion declaration, and renders a Markdown
template with `<reviewer: …>` slots the auditor fills in.

```bash
python skills/exocapitalist-audit/helper.py souls/<name>.yaml
python skills/exocapitalist-audit/helper.py souls/<name>.yaml --write
```

The `--write` mode saves to `docs/audits/<soul>_<YYYY-MM-DD>.md`.

## Output Path

Default report path: `docs/audits/<soul>_<YYYY-MM-DD>.md`

## Example

```text
five movements on souls/centaur_institutional.yaml
```
