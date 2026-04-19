---
name: soul-lineage
description: Trigger when lineage, conflicts, or ecosystem mapping is requested for a soul, because it makes cosmotechnical relations and tensions legible across souls and packs.
---

# Soul Lineage

## Purpose

Parse a soul's `meta.lineage`, `values.primary`, `ethics_pack.packs`, and
`institutional_role.balance_with`, cross-reference with all other souls and
packs, and render a Markdown lineage/tension graph.

Grounding: `theory/cosmotechnics.md`, `theory/algorithmic_beings.md`,
`theory/exocapitalism.md`.

## Trigger Phrases

- `lineage of <soul>`
- `what conflicts with <soul>`
- `show soul ecosystem`

## Inputs

- Target soul path in `souls/`
- All soul YAML files in `souls/`
- All pack files at `packs/*/pack.yaml`
- Optional `--write` flag

## Procedure

1. Read target soul and collect lineage/value/pack/role-balance fields.
2. Compare against each other soul for shared values and declared tensions.
3. Compare referenced packs for value overlap and divergence.
4. Emit Markdown summary with optional Mermaid graph section.
5. If `--write` is present, save the report to disk.

## Helper

A deterministic extractor lives at `skills/soul-lineage/helper.py`.
Use it to produce the mechanical lineage map; add interpretation on
top rather than re-deriving the extraction by hand.

```bash
python skills/soul-lineage/helper.py souls/<name>.yaml
python skills/soul-lineage/helper.py souls/<name>.yaml --write
```

## Output Path

- Default: stdout (Markdown)
- Optional file mode: `docs/lineage/<soul>.md`

## Example

```text
lineage of souls/cosmotechnical_guardian.yaml --write
```
