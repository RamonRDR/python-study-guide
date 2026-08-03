<div align="center">

# Security Policy

[🇺🇸 English](SECURITY.md) · [🇧🇷 Português](SECURITY.pt-BR.md) · [🇪🇸 Español](SECURITY.es.md)

</div>

## Supported content

Python Study Guide is an educational repository rather than a deployed service. Security fixes are applied to the current `main` branch and, when releases exist, to the latest maintained release when practical.

Historical commits, deleted branches, forks, copied material, and unsupported third-party tools are not maintained by this project.

## Report vulnerabilities privately

Do not open a public issue for a vulnerability that could expose users, credentials, private information, repository permissions, or supply-chain integrity.

Send a report to **ramoncorreka@hotmail.com** with the subject:

```text
[SECURITY] Python Study Guide
```

When GitHub private vulnerability reporting is available for the repository, it may also be used through the repository's **Security** tab.

Include only the information needed to understand the issue:

- affected file, workflow, dependency guidance, or repository feature;
- potential impact;
- safe reproduction steps or a minimal proof of concept;
- affected versions, commits, or environments;
- suggested mitigation, when available;
- whether any information has already been disclosed publicly.

Do not include real credentials, tokens, private URLs, personal data, employer data, proprietary code, or information obtained without authorization.

## What belongs in a security report

Examples include:

- a workflow or repository configuration that could allow unauthorized code execution or privilege misuse;
- instructions that expose credentials or encourage unsafe secret handling;
- malicious or compromised files presented as trusted project content;
- a dependency recommendation with a known, relevant, and reproducible security impact;
- a vulnerability in project-maintained code that creates a realistic security risk.

## What is not a security vulnerability

Use the normal issue templates for:

- incorrect explanations or translations;
- broken links or formatting;
- ordinary Python errors without security impact;
- questions about learning material;
- vulnerabilities in unrelated third-party products or personal projects;
- hypothetical concerns without a plausible attack path or affected project component.

## Response process

This project is maintained on a best-effort basis and does not provide a guaranteed service-level agreement.

The maintainer aims to:

1. acknowledge a valid report within seven calendar days;
2. confirm the affected scope and severity;
3. coordinate a correction and disclosure plan when needed;
4. credit the reporter when requested and safe;
5. publish relevant remediation information after affected users can protect themselves.

Please allow reasonable time for investigation before public disclosure. The maintainer may contact GitHub, package maintainers, or other responsible parties when coordination is required.

## Safe research expectations

Security research must be performed in good faith and within authorized environments. Do not:

- access, alter, or retain data that does not belong to you;
- disrupt services or other users;
- use social engineering, credential theft, or destructive testing;
- exploit a finding beyond what is necessary to demonstrate impact;
- demand payment, employment, or favors as a condition for withholding harmful disclosure.

This project does not currently operate a bug bounty program or promise financial rewards.
