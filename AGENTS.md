# Repository Instructions

## Project purpose

Python Study Guide is an independent, public, collaborative, and multilingual educational project.

Its purpose is to help people study Python, understand how its concepts connect, and practice through clear, accurate, original, and executable examples.

Assume that some readers have no previous programming experience. Explain necessary terms, avoid unexplained jumps, and never confuse brevity with clarity.

## Project stewardship

Python Study Guide was created and is maintained by [Ramon Estevez Rodriguez](https://github.com/RamonRDR).

Preserve the project's authorship records and license notice. Do not remove, overwrite, or misrepresent contributor credit recorded in commit metadata, Git history, or pull requests. See [AUTHORS.md](AUTHORS.md) for the repository's attribution policy.

## Priority order

When working on this repository, use the following order of priority:

1. Technical accuracy
2. Educational clarity
3. Privacy and safety
4. Consistency across languages
5. Maintainability
6. Delivery speed

Do not sacrifice accuracy, verification, or clarity to finish faster. Speed becomes a priority only when the maintainer explicitly requests a rapid or provisional result, and even then confidential information, fabricated claims, and unreviewed changes remain unacceptable.

## Languages

Documentation is maintained in:

- English
- Brazilian Portuguese
- Spanish

English is the default language for:

- directory names;
- file names;
- branch names;
- code identifiers;
- code comments;
- commit messages.

Translated documents must remain conceptually aligned. A translation does not need to be literal, but it must preserve the same technical meaning, examples, warnings, prerequisites, learning objectives, and links.

When a change affects multilingual documentation, update every affected language version in the same pull request whenever possible. Clearly disclose any missing translation.

## Educational content

Learning chapters should explain:

1. What the concept is
2. Why it exists
3. Its syntax
4. When to use it
5. When to avoid it
6. How it connects to other concepts
7. A basic example
8. A practical example
9. Common mistakes
10. An exercise
11. A quick-reference summary

Content must distinguish verifiable facts from recommendations or project conventions. Do not present an opinion as a Python rule.

Prefer primary and official sources when verification is required, including the official Python documentation, Python Enhancement Proposals, and the official documentation of any library or product being discussed.

For information that may change over time, verify the current documentation before publishing. Avoid hard-coding prices, plan limits, release availability, or other rapidly changing details unless the document is specifically intended to track them.

## Examples, originality, and privacy

Use only original, generic, fictional, and non-confidential examples.

Never include, reproduce, summarize, or adapt:

- private employer or client information;
- internal company processes;
- material from personal or family projects;
- credentials, secrets, tokens, or private URLs;
- proprietary source code;
- personal data;
- confidential documents;
- identifying details from private conversations or uploaded files;
- copyrighted examples without permission or an appropriate license.

Replacing a real name with a fictional label is not enough when the surrounding rules, dates, roles, system details, or workflow could still identify the source. Create an independent example instead.

## Code quality

- Follow PEP 8.
- Use descriptive English identifiers.
- Add type hints when they improve understanding.
- Keep examples small enough to study and realistic enough to be useful.
- Avoid unnecessary dependencies.
- Do not rely on version-specific behavior without identifying and verifying the relevant Python version.
- Comment decisions, constraints, and non-obvious reasons.
- Do not narrate code that already explains itself.
- Run or otherwise validate executable examples whenever possible.
- Never claim that code was executed or tested when it was not.

## Repository workflow

- Never modify the `main` branch directly.
- Create a focused branch from the current `main` branch.
- Keep each pull request limited to one clear purpose.
- Use English branch names and commit messages.
- Avoid unrelated formatting or refactoring in a focused change.
- Review every changed file before requesting a merge.
- Address review feedback before resolving its conversation.
- Do not bypass repository protections to accelerate a change.
- Use squash merging unless the repository configuration changes.

## AI-assisted work

AI tools may support research, planning, drafting, translation, explanation, code generation, testing, review, and repository maintenance.

AI output is a proposal, not an authority. It must not be accepted merely because it is fluent, detailed, or convincing.

The contributor and maintainer remain responsible for:

- understanding the submitted work;
- verifying technical accuracy;
- checking sources and links;
- reviewing translations;
- running relevant examples and tests;
- identifying unsupported or fabricated information;
- protecting private and proprietary information;
- confirming compliance with the repository license and policies.

Use AI to support thinking, not to avoid it. When teaching, prefer hints, questions, comparisons, and gradual explanations when they help the learner build understanding.

When uncertain, state the uncertainty and verify it. Do not invent missing facts, test results, citations, files, or behavior.

## Completion checklist

Before completing a change, confirm that:

- the change has one clear purpose;
- technical claims are accurate and appropriately sourced;
- examples are original, generic, and free of confidential information;
- executable examples work as described or their untested status is disclosed;
- all affected language versions are conceptually aligned;
- terminology and links are consistent;
- no unrelated files were modified;
- review discussions were properly addressed;
- the final result teaches rather than merely supplies an answer.
