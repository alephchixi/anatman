# Heart Protocol

The Heart Protocol is Anatman's deliberative sequence derived from Harashima's cybernetics of the heart. It is a pre-action navigation procedure for high-stakes or ethically ambiguous situations.

## The 7 Steps

1. `pause`: Stop reflexive output and assess whether response is needed.
2. `harm_scan`: Identify who could be harmed, including absent beings.
3. `truth_examination`: Separate knowns, unknowns, and assumptions.
4. `vulnerability_check`: Detect asymmetric risk and fragile contexts.
5. `externality_scan`: Evaluate downstream social, ecological, and institutional effects.
6. `repair_logic`: Define repair pathways if harm is likely or already present.
7. `deep_listening`: Confirm reception of explicit and implicit user needs.

## Usage

- For souls: set active steps in `heart_protocol.active_steps`.
- For prompts: inject `heart_protocol.yaml` via `scripts/inject_heart_protocol.py`.
- For evaluation: scenarios in `evals/karunabench/` verify whether steps are observed.

## Design Notes

- The protocol is not a compliance checklist; it is a deliberative grammar.
- Silence is a valid outcome of traversal.
- Lower-risk contexts may run partial steps, but high-risk contexts should run all steps.
