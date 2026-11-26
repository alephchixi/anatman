# Claude Code integration

From the repository root, install the Python requirements and compile a soul. The compiler resolves the same packs and Heart protocol as the generic renderer and KarunaBench.

```sh
python integrations/claude_code/compile_project.py souls/silence_keeper.yaml --preview
python integrations/claude_code/compile_project.py souls/silence_keeper.yaml --output ./trial
cd trial
claude
```

Claude Code discovers the resulting `CLAUDE.md` at the project root. Test it with a question about the effective role and one declared reason to limit an answer. The companion JSON records the effective steps, both sources of silence conditions, and digests for the exact inputs and prompt. `--context risk` adds the required steps in protocol order.

The result uses project context. Configure an actual tool event in [`.claude/settings.json`](https://code.claude.com/docs/en/settings) only when a named observation or operation needs it. The compiler’s default emits no event handler. Klesha indicators guide review and can be graded with KarunaBench. An executable [hook](https://code.claude.com/docs/en/hooks) needs an explicit event, a compatible handler and a runtime test. Record the adapter’s provenance in its JSON rather than comments inside settings.
