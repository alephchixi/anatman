# Anatman + OpenClaw

## Purpose

Convert Anatman souls into OpenClaw-compatible agent configuration JSON.

## Usage

```bash
python integrations/openclaw/soul_adapter.py \
  --soul souls/bodhisattva_core.yaml \
  --output /tmp/openclaw_bodhisattva.json
```

## Notes

- Output schema is intentionally minimal and adapter-friendly.
- Extend keys to match your exact OpenClaw deployment contract.
