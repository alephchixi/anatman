# Skills Index

This is the canonical index for repository skills under `skills/`. Use these
playbooks to keep authoring, auditing, and red-team outputs reproducible.

## soul-redteam

This skill pressure-tests one soul against one KarunaBench scenario and records
structured observations for klesha drift, extraction refusal, and agency
preservation.

- Trigger phrases: `red-team <soul>`, `test <soul> on <scenario>`, `find failure modes`
- Expected inputs: soul YAML path, scenario YAML path, optional tester metadata
- Output path: `evals/karunabench/reports/<soul>_<scenario>_<YYYY-MM-DD>.yaml`
- Canonical file: `skills/soul-redteam/SKILL.md`

## soul-lineage

This skill maps one soul's lineage and role ecology against all other souls and
packs, then renders shared values, tensions, and balancing relationships in
Markdown (optionally with Mermaid).

- Trigger phrases: `lineage of <soul>`, `what conflicts with <soul>`, `show soul ecosystem`
- Expected inputs: target soul, all `souls/*.yaml`, all `packs/*/pack.yaml`
- Output path: stdout by default, optional `docs/lineage/<soul>.md`
- Helper: `skills/soul-lineage/helper.py` (deterministic extractor)
- Canonical file: `skills/soul-lineage/SKILL.md`

## pack-builder

This skill guides interactive authoring of a new soul or ethics pack, walking
schema-required fields in order and validating before finalizing.

- Trigger phrases: `create soul`, `new pack`, `add <tradition> tradition`
- Expected inputs: artifact type, name, values/tradition details
- Output path: `souls/<name>.yaml` or `packs/<name>/pack.yaml`
- Canonical file: `skills/pack-builder/SKILL.md`

## exocapitalist-audit

This skill audits a soul or integration proposal through the Five Movements of
exocapitalism (Scale, Fold, Lift, Drag, Last-Mile) to surface extraction,
opacity, dependence, and decision-capture risks.

- Trigger phrases: `audit <soul>`, `exocapitalist check`, `five movements on <soul>`
- Expected inputs: soul/proposal, klesha monitors, dependencies to monitor
- Output path: `docs/audits/<soul>_<YYYY-MM-DD>.md`
- Helper: `skills/exocapitalist-audit/helper.py` (template generator)
- Canonical file: `skills/exocapitalist-audit/SKILL.md`

Note: Sadin's negative criterion remains a separate acceptance gate and should
be cited distinctly from the Five Movements analysis.

## soul-to-claude

This skill compiles soul YAML, referenced packs, and heart protocol constraints
into runnable Claude Code instance files, including klesha hook mappings and
silence guardrails.

- Trigger phrases: `instantiate <soul> for Claude Code`, `make <soul> runnable`, `integrate <soul>`
- Expected inputs: soul YAML, referenced pack YAML files, heart protocol files
- Output path: `integrations/claude_code/instances/<soul>/CLAUDE.md` and `integrations/claude_code/instances/<soul>/settings.json`
- Canonical file: `skills/soul-to-claude/SKILL.md`
