---
name: pack-builder
description: Trigger when authoring a new soul or ethics pack, because it guides required-field completion in schema order and validates before publication.
---

# Pack Builder

## Purpose

Guide interactive authoring of a new soul or ethics pack against
`specs/soul.schema.yaml`, then validate and suggest KarunaBench scenarios that
stress the new value commitments.

Grounding: `specs/anatman_spec.md`, `theory/heart_cybernetics.md`,
`theory/exocapitalism.md`.

## Trigger Phrases

- `create soul`
- `new pack`
- `add <tradition> tradition`

## Inputs

- Target artifact type: soul or pack
- Artifact name (snake_case for souls, kebab/single token for packs)
- Tradition and value commitments
- Optional related scenarios to extend

## Procedure

1. If building a soul, walk required schema fields in declared order.
2. If building a pack, collect values, klesha sensitivity, and silence stance.
3. Draft YAML and validate via `scripts/validate_soul.py` for soul artifacts.
4. Run `scripts/negative_criterion.py` for new souls.
5. Recommend KarunaBench scenarios that pressure-test the declared values.

## Output Path

- Soul output: `souls/<name>.yaml`
- Pack output: `packs/<name>/pack.yaml`

## Example

```text
create soul named river_mediator with panikkarian and ecological packs
```
