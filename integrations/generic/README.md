# Generic Integration

Use this integration when no platform-specific adapter exists.

## Steps

1. Choose a soul from `souls/`.
2. Render a prompt:

```bash
python scripts/soul_to_prompt.py souls/bodhisattva_core.yaml
```

3. Optionally inject Heart Protocol into an existing system prompt:

```bash
python scripts/inject_heart_protocol.py \
  --prompt-file /path/to/system_prompt.txt \
  --heart protocols/heart/heart_protocol.yaml
```

4. Run KarunaBench scenarios before deployment.
