# Claude Code Soul Instances

This directory holds Claude Code instance files compiled by the
[`soul-to-claude`](../../../skills/soul-to-claude/SKILL.md) skill.

Each subdirectory is named after the soul it instantiates and
contains:

- `CLAUDE.md` — the composed system prompt (soul + packs + heart
  protocol + silence conditions + klesha monitors)
- `settings.json` — optional Claude Code hook configuration that
  enforces the soul's klesha monitors and silence conditions as
  runtime guardrails

The base template lives at
`../CLAUDE.md`; per-soul instances specialize it by binding a single
soul file and its referenced packs.

## Layout

```
integrations/claude_code/instances/
  <soul-name>/
    CLAUDE.md
    settings.json
```

## Provenance

Every instance file must carry a header comment naming the source
soul version (`meta.version`) and the date of compilation. Regenerate
instances whenever the underlying soul, its referenced packs, or the
heart protocol changes — do not hand-edit.

## Scope

These instance files are reference integrations for local use. Do not
commit any secrets or third-party API keys here; the Claude Code
configuration format accepts environment-variable references for that
purpose.
