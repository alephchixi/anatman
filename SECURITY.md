# Security Policy

## Reporting a Vulnerability

Please report security issues privately through GitHub Security Advisories:
`https://github.com/alephchixi/anatman/security/advisories/new`.

If the advisory form is unavailable, open a minimal public issue asking for a
private security contact. Do not include vulnerability details in the issue.

Include clear reproduction steps, affected paths, and expected impact.
You can expect an acknowledgement within seven days and a triage note
within fourteen days. Coordinated disclosure is preferred; a public
advisory follows the patch release.

## Scope

This policy covers vulnerabilities in:

- Soul and pack configuration handling (`souls/`, `packs/`, `protocols/`)
- Local tooling scripts (`scripts/`, `evals/karunabench/runner.py`,
  `integrations/openclaw/soul_adapter.py`)
- CI/CD workflow behavior (`.github/workflows/ci.yml`)
- Dependency supply chain (`requirements.txt`, `requirements-dev.txt`)

Out of scope: findings about adversarial soul behavior, klesha drift,
or failure under ethical pressure. Report those through the red-team
process documented in [`REDTEAMING.md`](REDTEAMING.md) — they are part
of the ethical evaluation loop, not a security defect.

## Supported Versions

During the `0.x` series only the latest minor release receives
security fixes. Once the project reaches `1.0.0`, a formal support
policy will replace this section.
