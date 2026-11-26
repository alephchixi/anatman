---
name: soul-to-claude
description: >-
  Compile an Anātman soul, its packs and protocol into a Claude Code project with a deterministic context file and provenance. Use when asked to instantiate or preview a soul for Claude Code.
---

# Soul to Claude

Run the [compiler](../../integrations/claude_code/compile_project.py) from a full checkout. Choose `ordinary` for the soul’s declared profile and `risk` for the required high-impact floor.

```sh
python integrations/claude_code/compile_project.py souls/silence_keeper.yaml --preview
python integrations/claude_code/compile_project.py souls/silence_keeper.yaml --output ./trial
```

The compiler writes `CLAUDE.md` and `anatman-provenance.json`. Repeating generation with identical inputs is safe. A changed file at either destination requires a new destination or an explicit reconciliation. Open the generated project in Claude Code and check a profile-specific instruction the trial prompt did not itself supply.

The default expresses monitors in contextual instructions and criteria. If a project needs a concrete observable control, name the event and action it can observe, configure it in `.claude/settings.json`, and test that event. Keep ethical interpretation and limits in the evidence. The [integration guide](../../integrations/claude_code/README.md) shows the current runtime boundary.
