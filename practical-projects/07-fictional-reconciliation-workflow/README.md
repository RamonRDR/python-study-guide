# Fictional Reconciliation Workflow

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

[← Back to Practical Projects](../README.md)

This is **Project 07 of Phase 10: Practical Projects**. It turns two fictional record collections into an explicit, deterministic reconciliation report.

The example is original and fictional. It does not reproduce any real company, client, accounting system, or private workflow.

## What you will practice

This project combines concepts from earlier phases:

- immutable data modeling with `dataclass`;
- controlled states with `StrEnum`;
- exact money with `Decimal`;
- dictionaries as lookup indexes;
- sets for the union of reconciliation keys;
- deterministic sorting;
- validation and deliberate exceptions;
- functions with clear input/output boundaries;
- pytest coverage;
- separation between domain logic and presentation.

## Fictional scenario

Two imaginary sources should contain the same references and amounts.

Source North:

| Reference | Amount |
|---|---:|
| `REF-001` | `150.00` |
| `REF-002` | `275.50` |
| `REF-003` | `100.00` |

Source South:

| Reference | Amount |
|---|---:|
| `REF-001` | `150.00` |
| `REF-002` | `270.50` |
| `REF-004` | `100.00` |

The expected classifications are:

```text
REF-001 -> matched
REF-002 -> amount_mismatch
REF-003 -> left_only
REF-004 -> right_only
```

For records found on both sides, the signed difference is:

```text
difference = left.amount - right.amount
```

So `275.50 - 270.50` is `5.00`.

## Requirements

The workflow must:

1. accept two iterables of `ReconciliationRecord`;
2. reject empty reference identifiers;
3. require finite `Decimal` amounts;
4. accept only amounts exactly representable at cent precision and with at most 100 integer digits;
5. normalize surrounding whitespace in reference identifiers;
6. canonicalize accepted amounts to two decimal places;
7. reject duplicate references inside either source;
8. match identifiers exactly and case-sensitively;
9. classify every reference as `matched`, `amount_mismatch`, `left_only`, or `right_only`;
10. preserve the signed difference for amount mismatches;
11. sort output by reference identifier;
12. build deterministic summary counts;
13. calculate total absolute mismatch magnitude;
14. render a stable text report.

The 100-integer-digit boundary is an explicit resource-safety contract for this educational project. It is intentionally far above realistic sample values while preventing compact scientific notation such as `1e1000000` from expanding into enormous Python integers.

## Deliberate scope

The first version starts **after ingestion**.

It does not parse CSV files, spreadsheets, APIs, databases, or private data. Those layers were studied elsewhere and can be added later as extensions.

Keeping ingestion separate makes the core question easier to study:

> Given two already validated collections, how should reconciliation behave?

## Structure

```text
07-fictional-reconciliation-workflow/
├── README.md
├── README.pt-BR.md
├── README.es.md
├── demo.py
├── reconciliation.py
└── tests/
    ├── conftest.py
    ├── test_decimal_precision.py
    ├── test_reconciliation.py
    └── test_text_safety.py
```

## Core model

### `ReconciliationRecord`

```python
ReconciliationRecord(
    reference_id="REF-001",
    amount=Decimal("150.00"),
)
```

The record:

- trims surrounding identifier whitespace;
- rejects blank identifiers;
- requires an actual `Decimal`;
- rejects `NaN` and infinities;
- rejects values beyond cent precision;
- rejects amounts whose integer part exceeds 100 digits;
- stores accepted amounts in canonical two-decimal form.

Negative amounts are allowed because a generic workflow may represent reversals or adjustments.

### `ReconciliationStatus`

The controlled states are:

```python
MATCHED
AMOUNT_MISMATCH
LEFT_ONLY
RIGHT_ONLY
```

### `ReconciliationItem`

Each reconciled key has one valid shape:

| Status | Left | Right | Difference |
|---|---|---|---|
| `MATCHED` | yes | yes | zero |
| `AMOUNT_MISMATCH` | yes | yes | non-zero |
| `LEFT_ONLY` | yes | no | none |
| `RIGHT_ONLY` | no | yes | none |

The dataclass validates these invariants instead of trusting callers to build a consistent result.

### `ReconciliationSummary`

The summary stores:

- total items;
- matched items;
- amount mismatches;
- left-only items;
- right-only items;
- total absolute difference for amount mismatches.

Per-item differences keep their sign. The aggregate uses absolute values so a `+5.00` mismatch and a `-5.00` mismatch do not incorrectly cancel each other.

### `ReconciliationReport`

The report groups source names, ordered items, and the summary. Rendering happens afterward, so comparison logic is not tied to text output.

## Reconciliation pipeline

```text
validate source labels
        ↓
index left source
        ↓
index right source
        ↓
reject duplicates
        ↓
union all reference ids
        ↓
sort ids
        ↓
classify each id
        ↓
calculate differences
        ↓
build summary
        ↓
return immutable report
```

Dictionaries are useful here because they provide direct lookup by reconciliation key and make duplicate detection explicit.

## Matching contract

Identifiers are compared after surrounding whitespace is removed.

Matching is otherwise exact and case-sensitive:

```text
REF-001 != ref-001
```

That is a project decision, not a universal business rule. If a domain requires case folding, composite keys, or another normalization rule, that rule should be declared before reconciliation begins.

## Why `Decimal`?

For monetary values, the project uses:

```python
Decimal("275.50")
```

instead of `float`.

Creating `Decimal` from text preserves the intended decimal value. The record then enforces the project's two-decimal monetary boundary and a maximum of 100 integer digits before any integer-cent expansion occurs.

## Basic example

```python
from decimal import Decimal

from reconciliation import ReconciliationRecord, reconcile

left = (
    ReconciliationRecord("REF-001", Decimal("150.00")),
    ReconciliationRecord("REF-002", Decimal("275.50")),
)

right = (
    ReconciliationRecord("REF-001", Decimal("150.00")),
    ReconciliationRecord("REF-002", Decimal("270.50")),
)

report = reconcile(left, right)

for item in report.items:
    print(item.reference_id, item.status)
```

Logical output:

```text
REF-001 matched
REF-002 amount_mismatch
```

## Demo

Run from this directory:

```bash
python demo.py
```

The demo is deterministic, non-interactive, network-free, and uses only fictional in-memory data.

It produces the four important states and a summary.

## Failure paths

The workflow fails deliberately when its input contract is ambiguous or invalid.

Examples:

```python
ReconciliationRecord("", Decimal("10.00"))
```

raises `ValueError`.

```python
ReconciliationRecord("REF-001", 10.00)
```

raises `TypeError` because floats are not silently converted.

```python
ReconciliationRecord("REF-001", Decimal("10.001"))
```

raises `ValueError` because the amount exceeds cent precision.

```python
ReconciliationRecord("REF-001", Decimal("1e100"))
```

raises `ValueError` because the amount would require 101 integer digits, beyond the documented 100-digit boundary.

Duplicate references inside one source also raise `ValueError`. The workflow does not guess whether the first or last duplicate should win.

## Common mistakes

### Comparing rows by position

The same logical records may arrive in different orders. Reconcile by a stable key, not by list position.

### Silently overwriting duplicates

A normal dictionary assignment can hide duplicate source records. This project detects duplicates before insertion wins silently.

### Using absolute difference too early

`abs(left - right)` removes direction. Keep the signed difference on each item and use absolute values only for the summary metric.

### Mixing comparison and printing

Returning structured results makes the workflow easier to test and allows other renderers later.

### Adding normalization without a contract

Case folding, fuzzy matching, punctuation removal, or leading-zero removal can merge different identifiers. Treat normalization as an explicit domain decision.

## Tests

Run the focused suite from the repository root:

```bash
python -m pytest -q practical-projects/07-fictional-reconciliation-workflow/tests
```

The initial tests cover validation, duplicate detection, all four statuses, positive and negative differences, generators, deterministic ordering, source labels, case sensitivity, item invariants, empty input, exact-money precision boundaries, magnitude limits, summaries, and deterministic rendering.

## Exercise

Add `REF-005` to both demo sources with different values.

Before executing the program, predict:

1. the status;
2. the signed difference;
3. the new mismatch count;
4. the new total absolute difference.

Then run the demo and compare your prediction with the actual report.

## Extension challenges

After the base contract is clear, try one extension at a time:

1. Add a configurable `Decimal` tolerance and test its exact boundary.
2. Add a CSV ingestion layer that produces validated records before reconciliation.
3. Replace the simple reference with a composite key such as `(reference_id, period)`.
4. Add a Markdown renderer without changing `reconcile()`.
5. Export only unresolved items while preserving the canonical full report.
6. Introduce a reconciliation policy object instead of many unrelated Boolean flags.

## Portfolio discussion

This project demonstrates how to turn a generic comparison problem into explicit software contracts.

Useful points to explain in a portfolio:

- stable domain keys;
- exact monetary values;
- explicit magnitude boundaries;
- duplicate rejection;
- indexed lookup;
- deterministic states and ordering;
- signed differences and aggregate metrics;
- immutable results;
- separation of reconciliation and rendering;
- boundary-focused automated tests.

## Quick reference

```text
Input:       two iterables of ReconciliationRecord
Key:         normalized reference_id
Matching:    exact and case-sensitive
Money:       finite Decimal, cent precision, <= 100 integer digits
Statuses:    matched / amount_mismatch / left_only / right_only
Difference:  left.amount - right.amount
Ordering:    ascending reference_id
Duplicates:  rejected within each source
Output:      immutable ReconciliationReport
```

## Next project

After this project is reviewed, Phase 10 continues with **Project 08: Simulated Automation Flow**.
