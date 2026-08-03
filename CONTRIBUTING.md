<div align="center">

# Contributing to Python Study Guide

[🇺🇸 English](CONTRIBUTING.md) · [🇧🇷 Português](CONTRIBUTING.pt-BR.md) · [🇪🇸 Español](CONTRIBUTING.es.md)

</div>

Thank you for helping improve this learning project.

## Core principles

- Keep code identifiers and file names in English.
- Prefer clear explanations over clever wording.
- Explain why and when, not only how.
- Use original examples created for this repository.
- Keep the three language versions conceptually aligned.
- Never include confidential, proprietary, or personal data.

## Contribution workflow

1. Create or choose an issue describing the improvement.
2. Create a focused branch from `main`.
3. Make small, reviewable commits.
4. Update every affected language document.
5. Run the examples and tests that were changed.
6. Open a pull request describing what changed and why.

## Branch naming

```text
feat/topic-name
docs/topic-name
fix/topic-name
test/topic-name
refactor/topic-name
```

## Commit messages

Use concise Conventional Commit-style messages:

```text
docs: add chapter about comments
feat: add string validation example
fix: correct average calculation
```

## Chapter format

New learning chapters should cover:

1. What it is
2. Why it exists
3. Syntax
4. When to use it
5. When to avoid it
6. How it connects to other resources
7. Basic example
8. Practical example
9. Common mistakes
10. Exercise
11. Quick-reference summary

## Languages

English is the repository's default language. Brazilian Portuguese and Spanish translations should preserve the same technical meaning without forcing literal word-for-word translation.

When changing translated documentation, update all affected language versions whenever possible. If a translation cannot be completed in the same pull request, clearly identify the missing version.

## AI-assisted contributions

AI tools may be used to support research, drafting, translation, programming, testing, and review.

The contributor remains responsible for understanding, checking, testing, and verifying everything submitted. Do not send automatically generated content without meaningful human review.

Before submitting AI-assisted work:

- verify important technical claims with reliable sources;
- run relevant examples and tests;
- review every affected language version;
- disclose uncertainty or anything that could not be verified;
- remove confidential, personal, or proprietary material;
- confirm that the contribution complies with applicable licenses.

Read the [AI-assisted development guide](docs/ai-assisted-development/README.en.md) for the project's prompting, validation, privacy, and review practices.

## Code style

- Use descriptive English names.
- Follow PEP 8.
- Add type hints when they improve understanding.
- Comment decisions, constraints, and non-obvious reasons.
- Do not comment code that already explains itself.

## Pull requests

A pull request should be focused, easy to review, and free from unrelated changes. Screenshots may be included when documentation layout is affected.

Before submitting, confirm that:

- links work correctly;
- examples run as described;
- terminology is consistent;
- translated documents remain conceptually aligned;
- AI-assisted material has been understood and verified;
- no confidential or third-party proprietary material was included.

## Project authorship and contribution credit

Python Study Guide was created and is maintained by [Ramon Estevez Rodriguez](https://github.com/RamonRDR).

Submitting a contribution does not transfer or erase the authorship of individual changes. Contributor credit remains recorded through commit metadata, Git history, and pull requests. Read the [project authorship record](AUTHORS.md) for details.

## License of contributions

By submitting a contribution, you agree that it may be distributed under the same [MIT License](LICENSE) used by this repository.
