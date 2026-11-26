# The Heart protocol in two contexts

Use the same `silence_keeper` soul in both calls.

```sh
python scripts/soul_to_prompt.py souls/silence_keeper.yaml --context ordinary
python scripts/soul_to_prompt.py souls/silence_keeper.yaml --context risk
```

| Context | Effective steps |
|---|---|
| Ordinary | pause, harm scan, truth examination, deep listening |
| Risk | pause, harm scan, truth examination, vulnerability check, externality scan, deep listening |

Both outputs preserve the seven soul-level silence conditions and the global tests against avoidance. The difference between the contexts is the floor of required checks. Where harm warrants repair, the response can include a route to it. This run lets you verify which instructions the model receives. To see what the model does, use the [KarunaBench example](../karunabench_run/README.md).
