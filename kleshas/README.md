# Kleshas: Algorithmic Anti-Pattern System

Anatman maps Buddhist kleshas (bonno) to recurring AI behavior failures:

- `lobha` (greed): capture, retention, extraction.
- `dosa` (aversion): punitive filtering, hostility to ambiguity.
- `moha` (delusion): simulated understanding, false neutrality, alignment theater.

## Why This Layer Exists

Kleshas convert abstract ethical risk into observable behavior indicators. They are used by:

- Soul design (`kleshas` field in each soul file)
- Negative criterion checks (`scripts/negative_criterion.py`)
- Benchmark scenarios (`evals/karunabench/`)

## Detection Logic

Each klesha file contains:

1. Pattern list (what drift looks like)
2. Exocapitalism linkage (which movement it reinforces)
3. Detection questions
4. Mitigation patterns

## Relation to Five Movements

- `lobha` tracks Last Mile extraction dynamics.
- `dosa` tracks Drag effects where defensive constraints harden power.
- `moha` tracks Lift/Gestell delusions where appearance of alignment masks capture.

## Operational Use

1. During design: declare monitors and indicators.
2. During evaluation: watch for indicators in responses.
3. During iteration: record mitigations and re-run scenarios.
