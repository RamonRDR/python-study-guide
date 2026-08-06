<div align="center">

# Task Markers and Technical Follow-up

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Back to the section index](../README.md) · [← Previous chapter: Meaningful names](../03-meaningful-names/README.md)

Task markers are short labels inside comments that draw attention to work, constraints, risks, or temporary decisions. They can make unfinished work visible, but vague or abandoned markers quickly become wallpaper.

> **Guiding principle:** A marker should tell the next maintainer what must happen, why it matters, and how to know when the marker can be removed.

## Chapter information

| Item | Details |
|---|---|
| Level | Beginner to intermediate |
| Prerequisites | The comments chapter is recommended; familiarity with issues and version control is helpful |
| Estimated study time | 45 to 65 minutes |
| Main concepts | `TODO`, `FIXME`, `NOTE`, `HACK`, `XXX`, issue references, removal conditions, searching, review, stale markers |

## Learning objectives

By the end of this chapter, you should be able to:

- explain that task markers are project conventions, not Python syntax;
- distinguish future work, known defects, contextual notes, and temporary workarounds;
- write markers that include an action, reason, reference, or removal condition;
- decide when an issue should replace or accompany a source-code marker;
- avoid hiding failing tests, security problems, or production incidents behind comments;
- search and review markers consistently;
- recognize stale, vague, private, or misleading markers;
- define a small project convention that tools and contributors can follow.

## 1. What task markers are

Python treats a marker as an ordinary comment. `TODO`, `FIXME`, and similar words have no special meaning to the interpreter.

```python
# TODO(#128): Remove the compatibility branch after every client uses API v2.
```

The value comes from a shared convention. Editors, search tools, code-review systems, and contributors can recognize the label and route attention to it.

A marker is useful when the code location matters. It should not become a substitute for planning, testing, incident response, or an issue tracker.

## 2. Common marker vocabulary

Projects use these labels differently, so the repository convention is the source of truth.

| Marker | Typical meaning | Example intention |
|---|---|---|
| `TODO` | planned improvement or incomplete work | add a feature after a dependency is ready |
| `FIXME` | known incorrect or unsafe behavior | correct a defect before a release |
| `NOTE` | important context, not necessarily work | explain a representation or external constraint |
| `HACK` | deliberate workaround with a reason | support a legacy format temporarily |
| `XXX` | high-attention question or risk | request review of an uncertain assumption |

```python
# FIXME(#241): Reject duplicate invoice numbers before saving the batch.
```

```python
# NOTE: Amounts in this module are stored in cents.
```

```python
# HACK(#305): Keep the legacy padding until the old export format is retired.
```

```python
# XXX: Review this concurrency assumption before enabling parallel workers.
```

These meanings are conventions, not universal laws. A project may forbid `XXX`, prefer `BUG`, or use a different issue-reference format.

## 3. The convention used in this guide

This project recommends the following shape:

```text
# MARKER(reference): Clear action or important context.
# Optional continuation explaining the reason or removal condition.
```

The reference is optional for a pure `NOTE`, but work markers should normally point to a durable tracking item such as an issue.

Recommended examples:

```python
# TODO(#128): Replace the temporary parser after escaped fields are supported.
# FIXME(#241): Preserve leading zeroes in account codes.
# NOTE: Amounts are represented in cents.
# HACK(#305): Keep legacy padding until the old export format is retired.
```

Use uppercase labels so searches remain predictable. Keep the sentence specific and place the marker directly above the code it describes.

## 4. Make the marker actionable

A weak marker records frustration but not a task:

```python
# TODO: improve this
```

A useful marker answers several questions:

1. What should change?
2. Why is the change not being made now?
3. Which issue or decision tracks it?
4. What condition allows the marker to be removed?
5. Is there a deadline, release, or dependency that changes urgency?

```python
# TODO(#128): Replace the temporary CSV parser after the vendor publishes
# escaped-field support. Remove this branch when issue #128 is closed.
```

Not every marker needs every field. The more costly or risky the unfinished work is, the more context it deserves.

## 5. Prefer durable references over personal ownership

A person's name may become stale when roles change. An issue, ticket, or documented decision is easier to follow.

Weak:

```python
# TODO(Ramon): revisit later
```

Stronger:

```python
# TODO(#128): Add pagination after the API contract defines the cursor format.
```

Ownership can still exist in the issue tracker. The source comment should remain useful even when the original author is unavailable.

Avoid email addresses, private chat links, inaccessible ticket URLs, or customer-identifying information in public repositories.

## 6. `TODO`: planned work, not unlimited possibility

Use `TODO` for a concrete improvement that is intentionally deferred.

Good uses include:

- a dependency has not published the required API;
- a migration is underway;
- a non-critical optimization has a tracked acceptance criterion;
- a temporary branch must be removed after a rollout.

Do not add a `TODO` for every imagined feature. Unprioritized possibilities belong in planning notes, discussions, or issues.

A `TODO` without a reference may be acceptable in a tiny exercise, but production code benefits from durable tracking.

## 7. `FIXME`: a known defect requires stronger handling

`FIXME` signals that behavior is known to be wrong, misleading, incomplete, or unsafe.

```python
# FIXME(#241): Preserve leading zeroes in account codes.
```

A `FIXME` does not neutralize the defect. Depending on severity, the code may also need:

- a failing or regression test;
- an issue with priority and impact;
- a release blocker;
- a feature flag;
- an alert or incident;
- immediate removal from production.

Do not use a comment to silence evidence:

```python
# FIXME: the test is failing, so skip it
```

A skipped test should explain the tracked reason, expected recovery condition, and risk. Critical defects should not wait politely inside a comment.

## 8. `NOTE`: context rather than unfinished work

A `NOTE` preserves information a future reader could easily miss.

```python
# NOTE: The upstream service returns dates in UTC.
created_at = parse_utc_timestamp(payload["created_at"])
```

Use it for external contracts, units, compatibility rules, or decisions that are not obvious from the code.

Do not label context as a task:

```python
# TODO: Dates come from the upstream service in UTC.
```

If no action is required, `NOTE` communicates the intent more accurately than `TODO`.

A normal explanatory comment may be clearer when the `NOTE` label adds no search or review value.

## 9. `HACK`: document the workaround and its exit

A workaround may be responsible engineering when an external constraint prevents the ideal solution. The danger is allowing temporary code to become permanent without explanation.

```python
# HACK(#305): Legacy exports pad account codes to eight characters.
# Remove this normalization after the pre-2024 export format is retired.
account_code = raw_account_code.lstrip("0")
```

A useful `HACK` states:

- which constraint forced the workaround;
- what behavior depends on it;
- the tracking reference;
- the condition for removal;
- any risk the workaround introduces.

Avoid:

```python
# HACK: weird fix
account_code = raw_account_code.lstrip("0")
```

`HACK` is not permission for careless code. The implementation should still be tested, bounded, and understandable.

## 10. `XXX` and custom markers

`XXX` often means “this deserves unusual attention,” but its meaning varies widely.

```python
# XXX(#411): Confirm whether this cache may be shared between tenants.
```

Use it only when the project defines it. Otherwise, choose a more precise marker such as `FIXME`, `SECURITY`, `PERF`, or `DEPRECATED`.

Custom markers can be useful when they correspond to a real review process. Too many labels create a private dialect that tools and contributors cannot predict.

## 11. Markers and issue trackers solve different problems

A source marker answers:

> Where in the code does this concern apply?

An issue answers:

> How is the work prioritized, discussed, assigned, tested, and completed?

For small local work, a marker may be enough. For work involving several files, teams, releases, risks, or decisions, create an issue and link the marker to it.

Close the loop:

1. update or close the issue;
2. remove or revise the marker;
3. update tests and documentation;
4. verify no stale references remain.

## 12. Dates are supporting context, not an exit strategy

A date can help explain timing, but “remove later” and “check next month” are weak conditions.

Prefer an observable event:

- after all clients migrate to API v2;
- when issue `#128` is closed;
- after the minimum supported Python version changes;
- when regression tests cover the replacement;
- before a named release.

A removal condition makes the marker testable during review.

## 13. Do not place secrets or sensitive data in markers

Comments are stored in Git history and may remain recoverable after deletion.

Never include:

- passwords, tokens, API keys, or credentials;
- customer names or private identifiers;
- confidential incident details;
- internal URLs that should not be public;
- personal contact information.

Bad:

```python
# SECURITY: Temporary token for production: abc123
```

Use the project's private security or incident process instead. Rotating a leaked credential is necessary even if the comment is removed immediately.

## 14. Keep markers close and narrow

Place a marker immediately above the smallest relevant block.

```python
# TODO(#128): Replace the temporary parser.
```

Avoid a marker at the top of a large module when only one branch is affected. A distant marker is easy to misread after refactoring.

If the concern spans several modules, the issue tracker should hold the broader explanation while local markers identify the exact code points.

## 15. Search and review markers

A simple repository search can reveal accumulated work:

```bash
rg -n "#\s*(TODO|FIXME|NOTE|HACK|XXX)\b" .
```

Editors and GitHub code search can also search by marker. Keep labels and punctuation consistent so tools do not miss variants.

For Python-aware analysis, use the standard-library `tokenize` module. It distinguishes real comments from marker-like text inside strings.

```python
from io import StringIO
import tokenize


source = '''
message = "# TODO: this is text, not a comment"
# TODO(#128): Replace the temporary parser.
'''

for token in tokenize.generate_tokens(StringIO(source).readline):
    if token.type == tokenize.COMMENT:
        print(token.string)
```

The example in this chapter demonstrates a small scanner for simple marker conventions. It is educational, not a replacement for a mature linter or issue-management workflow.

## 16. Consistency enables automation

A stable format supports:

- editor highlighting;
- repository reports;
- CI rules for forbidden markers;
- issue-reference validation;
- release checks;
- dashboards for technical debt.

Consistent:

```python
# TODO(#128): Replace the temporary parser after escaped fields are supported.
# FIXME(#241): Preserve leading zeroes in account codes.
# NOTE: Amounts are represented in cents.
# HACK(#305): Keep legacy padding until the old export format is retired.
```

Harder to search reliably:

```python
# TODO-128 replace parser
# todo: maybe later
# FixMe(issue 241): zeros
```

Automation should support judgment, not encourage meaningless issue numbers or comments written only to satisfy a pattern.

## 17. Examples in this repository

| File | Purpose |
|---|---|
| [`actionable_markers.py`](examples/actionable_markers.py) | Shows markers with references, context, and a removal condition |
| [`temporary_workaround.py`](examples/temporary_workaround.py) | Documents a bounded workaround for a fictional legacy format |
| [`scan_markers.py`](examples/scan_markers.py) | Uses `tokenize` to find markers in real Python comments |

Run an example from the repository root:

```bash
python comments-and-documentation/04-task-markers/examples/actionable_markers.py
```

On systems where the command is named `python3`:

```bash
python3 comments-and-documentation/04-task-markers/examples/actionable_markers.py
```

## 18. Practical refactoring example

Before:

```python
def load_report(file_path):
    # TODO: make this better
    return file_path.read_text()
```

After:

```python
def load_report(file_path):
    # TODO(#512): Stream files larger than 50 MB to avoid loading them at once.
    # Remove this marker after the streaming reader is covered by regression tests.
    return file_path.read_text()
```

The improved marker identifies the limitation, impact, issue, and completion condition. The code may still require immediate redesign if the current behavior is unsafe for supported inputs.

## 19. Common mistakes

### Writing a marker with no action

“Improve this” does not define done.

### Using `TODO` for a known defect

A defect may deserve `FIXME`, a test, and urgent tracking.

### Treating `NOTE` as technical debt

A note may remain permanently because it documents a stable constraint.

### Creating a marker instead of an issue

Cross-team or release-critical work needs prioritization outside the source file.

### Leaving a closed issue reference

When the issue is completed, remove or update the source marker.

### Recording only a date or person's name

Dates and owners change. Prefer durable references and observable exit conditions.

### Hiding risk behind `HACK`

A workaround still requires tests, boundaries, and review.

### Including private information

Git history is not a private notebook.

### Reformatting unrelated code while adding markers

Keep the pull request focused so reviewers can evaluate the actual change.

## 20. Exercise

Rewrite these vague or incomplete markers using the chapter's recommended convention:

```python
# TODO: improve parser
```

```python
# TODO(Ramon): fix leading zeroes later
```

```python
# TODO: rates are fractions
```

```python
# HACK: temporary workaround
```

```python
# XXX: check tenant isolation
```

For each marker, decide:

1. Is the label accurate?
2. Is an issue reference needed?
3. Is the required action clear?
4. Is the reason or risk documented?
5. Is there an observable removal condition?
6. Should the concern block release instead of remaining as a comment?

Then search a small practice project for markers and classify each one as active, stale, resolved, or unnecessary.

## 21. Review checklist

Before accepting a marker, verify:

- [ ] the label matches the meaning;
- [ ] the action or context is specific;
- [ ] the marker is next to the relevant code;
- [ ] tracked work includes a durable reference;
- [ ] risky work includes impact and urgency;
- [ ] temporary work includes a removal condition;
- [ ] no secret, personal, or confidential data appears;
- [ ] the marker does not replace a necessary test or issue;
- [ ] spelling and punctuation match the project convention;
- [ ] resolved work removes or updates the marker.

## 22. Quick-reference summary

| Need | Preferred approach |
|---|---|
| Concrete deferred improvement | `TODO(reference): action and condition` |
| Known incorrect behavior | `FIXME(reference): defect and impact` plus appropriate tracking |
| Important stable context | `NOTE: context` or a normal explanatory comment |
| Temporary workaround | `HACK(reference): reason and removal condition` |
| Uncertain high-attention assumption | project-defined `XXX` or a more precise label |
| Cross-file planning | issue tracker, with local markers where code location matters |
| Search | consistent labels, editor search, `rg`, or Python `tokenize` |
| Completed work | remove or update both the marker and its tracking item |

Task markers are useful when they create a bridge from code to responsible follow-up. Without context and closure, that bridge becomes decorative scaffolding.
