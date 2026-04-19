# Anatman + Claude Code

## Purpose

This integration applies Anatman soul constraints to Claude Code sessions via `CLAUDE.md`.

## Setup

1. Copy `integrations/claude_code/CLAUDE.md` into your project root.
2. Keep Anatman soul files accessible in your workspace (or adapt paths).
3. Optionally regenerate a custom soul prompt:

```bash
python scripts/soul_to_prompt.py souls/bodhisattva_core.yaml > /tmp/anatman_prompt.md
```

## Customization

- Replace `bodhisattva_core.yaml` with another soul from `souls/`.
- Adjust silence thresholds and institutional role notes for your use case.

## Validation

Before relying on a custom soul:

```bash
python scripts/validate_soul.py souls/<your_soul>.yaml
python scripts/negative_criterion.py souls/<your_soul>.yaml
```
