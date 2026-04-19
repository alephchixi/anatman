# Governance

This document defines how Anatman is maintained as an open, anti-extractive
project.

## Governance Principles

1. AGPL continuity is non-negotiable.
2. The negative criterion is the acceptance gate.
3. Theory and implementation must remain auditable and traceable.
4. Disagreement is expected and handled through explicit rationale.

## Change Classes

Contributions are reviewed in these classes:

1. Theory changes (`THEORY.md`, `theory/`, `MANIFESTO.md`, `ETHICS.md`)
2. Specification changes (`specs/`, schema or field semantics)
3. Soul and pack changes (`souls/`, `packs/`, `kleshas/`)
4. Tooling changes (`scripts/`, `evals/`, `integrations/`)
5. Documentation and examples (`docs/`, `examples/`, `site/`)

## Decision Rules

1. Any change that weakens anti-extractive guarantees is rejected.
2. Schema changes must include migration notes and compatibility impact.
3. Soul changes must include rationale tied to theory and expected behavior.
4. New evaluation scenarios are preferred over purely stylistic arguments.

## Required Evidence For Merges

At minimum:

1. Relevant validation passes (once scripts are available).
2. Negative criterion review for affected souls.
3. Red-team notes for high-impact behavior changes.
4. Updated docs when public behavior changes.

## Conflict Resolution

When disagreement persists:

1. Summarize competing proposals and tradeoffs in writing.
2. Evaluate against the negative criterion and project ethics.
3. Prefer the option that increases legibility and reduces capture risk.

## Stewardship Note

Anatman is designed as a commons-oriented repository. Governance protects the
conditions that keep the project open, contestable, and accountable.
