# Professional Python Workflow

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Previous](../03-test-driven-development/README.md) · [Module index](../README.md) · [Next →](../../problem-solving-and-live-coding/01-problem-solving-fundamentals/README.md)
<!-- /chapter-navigation:top -->

## Goal

**Estimated time:** 35–50 minutes. Apply the previous lessons in a small Python change. You need local Git, a practice repository and the verified Python interpreter. See [Git basics](../../getting-started/06-git-and-version-control/README.md). A hosting account is optional; do not create a paid service or use the real study-guide repository for experiments.

## 1. Make the work reviewable

Use your own local repository with a committed baseline. Save the reading-progress requirements, plan and ADR from the SDD lesson in your practice repository. If not yet committed, review and commit them on the baseline before branching. Make sure `git status` is clean. Create a focused branch:

```shell
git switch -c feat/reading-progress
```

Implement and test the behavior manually using the previous lesson. Keep generated files and secrets out of Git. Before committing, run tests in the practice folder:

```shell
python -m unittest discover -s . -p 'test_*.py' -v
git status
git diff
git add reading_progress.py test_reading_progress.py
git diff --cached
git commit -m "feat: calculate remaining reading pages"
```

Use the actual files you intend to change; inspect staged contents first. If there is a failure, investigate and rerun rather than reporting success.

## 2. Write a reviewable change description

In a local note, draft a pull request: purpose; requirements R1–R4; implementation summary; acceptance evidence AC1–AC5; commands and actual outcomes; known limitations; out-of-scope work. A code review is a reasoning exercise: compare code against the spec, inspect edge cases, naming, error handling, tests and privacy. A passing CI run is necessary when required, not a guarantee of correctness.

## 3. Optional GitHub practice

Only if you own a practice remote and understand its visibility, push the feature branch with `git push -u origin feat/reading-progress`. Open a pull request targeting the practice main branch. If using GitLab, the equivalent review is a merge request. Never push to someone else's repository without permission. Git and platform depth belongs to the future Git Study Guide; this lesson is a Python workflow example.

CI executes configured checks on changes. For example, a minimal GitHub Actions workflow for this isolated practice repository could be saved as .github/workflows/python-tests.yml **on the feature branch**:

```yaml
name: Python tests
on: [pull_request]
permissions:
  contents: read
jobs:
  tests:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v6
      - uses: actions/setup-python@v6
        with:
          python-version: "3.13"
      - run: python -m unittest discover -s . -p 'test_*.py' -v
```

This is an illustrative minimal workflow, not an instruction to replace the study guide's [existing workflow](../../.github/workflows/quality-checks.yml). It assumes test files are in the practice repository root and no external dependencies are needed. Review the workflow file before staging and committing it separately; push again. Check hosting availability and quotas before running hosted CI; local tests are sufficient for the required exercise. Do not claim the illustrative workflow ran if it did not. Review results, address feedback, rerun tests and merge only with approval. If CI fails or histories conflict, stop and investigate; do not bypass protections. Without a remote, simulate review locally with `git diff main...HEAD`; leave the branch unmerged until review.

## 4. Independent work and AI boundaries

First solve and explain the problem without AI-generated implementation or grading. Use official docs, tests, debugging and human feedback. If using AI for learning, ask for a hint after a genuine attempt; verify any answer and do not share private data. The separate [AI-assisted maintenance guide](../../docs/ai-assisted-development/README.en.md) explains how contributors may use ChatGPT/Codex with human responsibility. AI-assisted repository maintenance is not the student's independent practice.

## 5. Completion checklist

- Requirement and acceptance criteria are explicit.
- I wrote and understood the code; tests demonstrate normal, boundary and invalid cases.
- I checked the diff, commit and actual test outcomes.
- I can explain one design decision and one trade-off.
- Review feedback is addressed; merge requires approval.
- I can reproduce the workflow on a different small problem.

**Quick reference:** need → spec → plan → branch → test/code/refactor → review diff → commit → optional PR/CI → human approval → merge. For more detailed contributor rules, read [CONTRIBUTING](../../CONTRIBUTING.md).

<!-- chapter-navigation:bottom -->
[← Previous](../03-test-driven-development/README.md) · [Module index](../README.md) · [Next →](../../problem-solving-and-live-coding/01-problem-solving-fundamentals/README.md)
<!-- /chapter-navigation:bottom -->
