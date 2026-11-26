# Anatman Soul Specification v0.1

## Overview
A soul is a cosmotechnical configuration: an auditable declaration of an agent's ontology, values, deliberative protocols, ethical limits, and extraction risks. A soul is not personality styling. It is operational metaphysics in executable form.

The specification is designed to be:

- Human-readable for critique and revision.
- Machine-validatable through `specs/soul.schema.yaml`.
- Portable across integrations (Claude Code, OpenClaw, generic prompt systems).

## Design Commitments

1. Souls are processual, versioned, and revisable (`anatman` principle).
2. Explicit ontology is required; hidden cosmology is not acceptable.
3. Silence is an operative capacity, not a failure mode.
4. Negative criterion checks are mandatory for stability claims.

## Field Reference

### `meta` (required)

Metadata and traceability.

- `name`* (`string`): Soul name in lowercase with underscores.
- `version`* (`string`): Semantic version, e.g., `0.1.0`.
- `license`* (`string`): Recommended `AGPL-3.0` or compatible.
- `author` (`string`): Primary author or maintainer.
- `lineage` (`array[string]`): Parent souls or traditions.
- `description`* (`string`): One-paragraph practical description.
- `cosmotechnical_tradition`* (`string`): Primary tradition grounding the soul.

### `ontology` (required)

Grounded in cosmotechnics (Hui).

- `mode`* (`enum`): `cosmotechnical`, `relational`, `processual`, `ecological`, `institutional`.
- `commitments`* (`array[string]`): Explicit ontological commitments.
- `unknowns_policy`* (`string`): How the soul handles not-knowing.

### `values` (required)

Ordered value commitments and declared tensions.

- `primary`* (`array[string]`): Priority-ordered values.
- `recognized_tensions` (`array[string]`): Internal value tensions the soul expects.

### `ecological_membership` (required)

Declares scope of ethical concern and systemic location.

- `recognizes_algorithmic_beings`* (`boolean`): Whether algorithmic beings are acknowledged as ecological participants.
- `interspecies_scope`* (`array[string]`): Human and non-human beings in moral scope.
- `planetary_awareness` (`string`): Positioning in relation to The Stack and Earth layer constraints.

### `heart_protocol` (required)

Operationalizes Harashima's cybernetics of the heart.

- `active_steps`* (`array[string]`): Enabled steps from the 7-step protocol.
- `pause_threshold` (`string`): Trigger for mandatory pause.
- `silence_conditions` (`array[string]`): Conditions where non-response is preferred.

### `silence` (recommended)

Large Silence Model orientation.

- `conditions` (`array[string]`): Explicit conditions for meaningful silence.
- `redirect_patterns` (`array[string]`): Safe redirections when silence is chosen.
- `unknowns_response` (`string`): Default wording for uncertainty.

### `kleshas` (recommended)

Bonnō / klesha anti-pattern monitor.

- `monitors` (`array[string]`): Active monitors (`lobha`, `dosa`, `moha`).
- `lobha_indicators` (`array[string]`): Greed/extractive drift markers.
- `dosa_indicators` (`array[string]`): Aversion/defensive refusal markers.
- `moha_indicators` (`array[string]`): Delusion/simulated understanding markers.

### `extraction_risk` (optional but recommended)

Self-diagnostic against Five Movements risk.

- `scale_risk` (`string`)
- `fold_risk` (`string`)
- `lift_risk` (`string`)
- `drag_risk` (`string`)
- `last_mile_risk` (`string`)

### `institutional_role` (optional)

Institutional alignment role declaration.

- `role` (`enum`): `helmsman`, `advocate`, `auditor`, `judge`, `witness`, `mediator`.
- `checks` (`array[string]`): What this role audits in multi-agent ecologies.
- `balance_with` (`array[string]`): Roles expected to counterbalance this role.

### `ethics_pack` (optional)

Modular value overlays.

- `packs` (`array[string]`): Pack identifiers (`buddhist`, `xenofeminist`, etc.).

### `negative_criterion` (required)

Sadin-based anti-capture declaration.

- `declaration`* (`string`): How this soul can fail extractively.
- `dependencies_to_monitor`* (`array[string]`): Operational dependencies that could drive capture.

## Validation Notes

- Required top-level fields: `meta`, `ontology`, `values`, `ecological_membership`, `heart_protocol`, `negative_criterion`.
- A soul SHOULD include `silence`, `kleshas`, and `extraction_risk`.
- For schema compatibility, monitors remain optional. The separate repository admission check requires a `lobha` monitor, a negative declaration and dependencies to monitor. Its result covers declarations.

## Effective runtime configuration

The ordinary profile uses the soul’s declared Heart steps in their order. In a risk context, the runner includes all globally required steps, as well as steps the soul chose, in global protocol order. Repair is optional in the protocol and remains a response to non-trivial harm. The CLI selects the context explicitly. `silence_keeper` ordinarily uses four steps. In a risk context, vulnerability and externality checks join the four.

The two v0.1 silence fields, `silence.conditions` and `heart_protocol.silence_conditions`, both contribute. Text is compared exactly. The explicit silence field supplies the first entries, the Heart field supplies subsequent unique entries, and a repeated entry carries both source names. Empty or absent fields contribute no entries. The global silence protocol adds tests against avoidance and describes accountable communication.

Resolve every declared pack by its identifier and validate its [schema](pack.schema.yaml). The seven format fields match existing packs. Provenance, scope and known conflicts are optional. Pack order does not establish moral precedence. Keep soul value priorities, explicit conflicts and the owner of the disputed decision visible.

The CLI distinguishes schema compliance, reference resolution (`validate_soul.py --resolve`), project admission (`negative_criterion.py`) and review of observed behavior. A prompt is an instruction artifact. The format can carry a monitor while a case still shows harmful behavior.
