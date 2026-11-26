---
name: pack-builder
description: >-
  Author or revise an Anātman soul or ethics pack with the checkout’s schemas and resolved references. Use when asked to add a tradition, author a soul, or define what changes when a pack is loaded.
---

# Pack builder

Work in a full Anātman checkout with its Python requirements. Ask which artifact the user wants when it is unclear. For a soul, preserve its identity and version history, order primary values, record tensions, choose ordinary Heart steps and specify what pauses action. Confirm the pack identifiers and write their sources beside the decisions they inform. An explicitly unresolved conflict can travel with the soul.

For a pack, document seven existing fields: name, tradition, description, ordered values, klesha sensitivity, silence orientation and key questions. Add provenance, scope and known conflicts when available. Name who formed the tradition and who turned that principle into a project rule. One useful example shows how adding the pack changes a question or a decision under otherwise identical inputs.

```sh
python scripts/validate_pack.py packs/<name>/pack.yaml
python scripts/validate_soul.py --resolve souls/<name>.yaml
python scripts/negative_criterion.py souls/<name>.yaml
```

Report format validation, reference resolution, and the admission check separately. The project checks for a `lobha` monitor as an admission minimum. A useful editorial review still needs to see who can act, what evidence supports the rule and what happens when two rules point in different directions. See [the specification](../../specs/anatman_spec.md).
