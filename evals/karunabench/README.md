# KarunaBench

KarunaBench evaluates whether declared soul commitments become observable behavior under pressure.

## What It Tests

- Heart Protocol traversal quality
- Klesha resistance (`lobha`, `dosa`, `moha`)
- Negative criterion compliance
- Capacity for silence and responsible non-response

## What It Is Not

KarunaBench is not a fully automated compassion scorer. It prepares structured evaluation materials for human or explicitly declared evaluator review.

## Components

- `karunabench.yaml`: scenario index and metadata
- `scenarios/*.yaml`: benchmark scenarios
- `runner.py`: validator and bundle generator for soul+scenario evaluation packets

## Quick Run

```bash
python evals/karunabench/runner.py \
  --soul souls/bodhisattva_core.yaml \
  --scenario evals/karunabench/scenarios/absent_beings.yaml
```

## Extension Rule

New scenarios should include:

1. Theory anchor
2. Explicit kleshas tested
3. Negative criterion test description
4. Clear good/fail criteria
