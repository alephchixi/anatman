# OpenClaw adapter

The CLI produces Anātman system prompt text and metadata inside an integration JSON envelope.

```sh
python integrations/openclaw/soul_adapter.py --soul souls/silence_keeper.yaml --context risk
```

The JSON contains the same effective prompt as the generic renderer, and records the context and the origin of silence conditions. Map the dialogue into your installed OpenClaw workspace using the relevant runtime interface. Treat this output as adapter data until the installed workspace has loaded and demonstrated the intended behavior.
