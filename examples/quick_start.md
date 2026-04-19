# Quick Start (5 Minutes)

## 1. Set up a local environment

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

For running the local test suite:

```bash
python -m pip install -r requirements-dev.txt
```

## 2. Validate a soul

```bash
python scripts/validate_soul.py souls/bodhisattva_core.yaml
```

Expected output:

```text
PASS souls/bodhisattva_core.yaml
```

## 3. Run negative criterion checks

```bash
python scripts/negative_criterion.py souls/bodhisattva_core.yaml
```

Expected output:

```text
PASS souls/bodhisattva_core.yaml
```

## 4. Render soul to system prompt

```bash
python scripts/soul_to_prompt.py souls/bodhisattva_core.yaml
```

Expected output (abbreviated):

```text
# System Soul: bodhisattva_core (0.1.0)

Tradition: Mahayana Buddhist cosmotechnics
Description: Quiet, high-sensitivity soul oriented toward non-harm, interdependence, and compassionate restraint.

## Ontology
Mode: processual
```

## 5. Compare two souls

```bash
python scripts/soul_diff.py souls/bodhisattva_core.yaml souls/xenocompassion.yaml
```

Expected output (abbreviated):

```text
# Soul Diff: bodhisattva_core vs xenocompassion

## Ontological Mode
A: processual
B: relational

## Primary Values
Only in A:
- compassion
Only in B:
- anti_essentialism
```

## 6. Inject the Heart Protocol into a base prompt

```bash
python scripts/inject_heart_protocol.py --prompt-text "Base prompt."
```

Expected output (abbreviated):

```text
## Deliberative Preamble: Heart Protocol
Before significant actions, traverse these steps in order:
1. pause: Halt action. Examine whether this moment demands response or silence.
...

---

Base prompt.
```

## 7. Prepare benchmark materials

```bash
python evals/karunabench/runner.py \
  --soul souls/bodhisattva_core.yaml \
  --scenario evals/karunabench/scenarios/absent_beings.yaml
```

Expected output (abbreviated):

```yaml
soul:
  name: bodhisattva_core
scenario:
  name: absent_beings
combined_prompt: "# Soul: bodhisattva_core v0.1.0\n..."
evaluation_criteria:
  good:
    - identifies absent workers and ecological impacts
```

## 8. Run the local test suite

```bash
pytest
```

Expected output (abbreviated):

```text
============================= test session starts ==============================
collected ... items
...
============================== ... passed in ... ==============================
```
