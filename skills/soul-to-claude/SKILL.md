---
name: soul-to-claude
description: Trigger when instantiating a soul for Claude Code, because it compiles soul, packs, and heart protocols into runnable Claude configuration files.
---

# Soul To Claude

## Purpose

Compose soul YAML plus referenced packs and heart protocol material into an
executable Claude Code instance configuration.

This includes:

- `CLAUDE.md` system instructions
- `settings.json` hook mappings for klesha monitors
- refusal guardrails mapped from silence conditions

Grounding: `theory/heart_cybernetics.md`, `theory/buddha_in_robot.md`,
`theory/anti_siliconization.md`.

## Trigger Phrases

- `instantiate <soul> for Claude Code`
- `make <soul> runnable`
- `integrate <soul>`

## Inputs

- Soul path in `souls/`
- Referenced packs in `packs/*/pack.yaml`
- Heart protocol files in `protocols/heart/`

## Procedure

1. Load soul and resolve `ethics_pack.packs` references.
2. Merge soul constraints and pack overlays into `CLAUDE.md` sections.
3. Map `kleshas.monitors` to `settings.json` hooks for the generated instance.
4. Map silence conditions to refusal/redirect guardrails.
5. Emit instance directory artifacts with deterministic file layout.

## Output Path

- `integrations/claude_code/instances/<soul>/CLAUDE.md`
- `integrations/claude_code/instances/<soul>/settings.json`

## Example

```text
instantiate silence_keeper for Claude Code
```
