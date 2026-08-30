<div align="center">

# Project 02 · Grade Calculator

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Back to Practical Projects](../README.md)

This is the second project in **Phase 10: Practical Projects**. It focuses on configurable rules, weighted aggregation, validation, progress reporting, and deterministic tests without repeating the persistence boundaries from Project 01.

**Estimated study and implementation time:** 150–210 minutes.

## Learning goals

By the end of this project, you should be able to:

- translate grading rules into explicit data contracts;
- model immutable assessments and grade boundaries with dataclasses;
- validate scores and weights before mutating calculator state;
- calculate weighted averages without relying on binary floating point;
- distinguish a progress average from a final course result;
- make letter-grade and passing rules configurable;
- return a structured report before formatting it for display;
- test boundary values, invalid configurations, and custom policies.

## 1. Project brief

Build a grade calculator that can:

1. register graded assessments;
2. assign a percentage weight to each assessment;
3. reject cumulative weights above 100%;
4. calculate the current weighted average from assessments entered so far;
5. show completed and remaining course weight;
6. classify the average with a configurable grade policy;
7. report pass/fail only when the course reaches exactly 100% weight;
8. support custom letter-grade boundaries and passing scores;
9. render a deterministic text report;
10. prove the important behavior with automated tests.

## 2. Functional requirements

Each assessment contains:

```text
name   -> non-blank text
score  -> percentage from 0.00 to 100.00
weight -> percentage greater than 0.00 and at most 100.00
```

The calculator preserves insertion order and never allows the combined assessment weight to exceed `100.00`.

## 3. Default grading policy

The default policy is:

```text
A -> 90.00 to 100.00
B -> 80.00 to 89.99
C -> 70.00 to 79.99
D -> 60.00 to 69.99
F ->  0.00 to 59.99

passing score -> 60.00
```

These thresholds are a project convention, not a universal academic standard. A different institution can supply a different `GradePolicy`.

## 4. Why percentages use `Decimal`

Scores and weights are normalized to two decimal places with `ROUND_HALF_UP`.

```python
Assessment.create("Midterm", "91", "30")
```

The project does not use `float` for grading values. Parsing also uses an explicit local decimal context so unrelated caller precision, rounding, or traps do not alter the project's validation contract.

## 5. Exact weighted aggregation

Once scores and weights are validated to two decimal places, the calculator converts them to integer hundredths.

```text
91.00 -> 9100
30.00 -> 3000
```

Weighted aggregation then uses Python integers, which avoids losing decimal precision because of an external `Decimal` arithmetic context. The final ratio is rounded half up back to two decimal places.

## 6. The `Assessment` model

`Assessment` is immutable:

```python
@dataclass(frozen=True, slots=True)
class Assessment:
    name: str
    score: Decimal
    weight: Decimal
```

Validation runs even when callers use the dataclass constructor directly.

## 7. Grade bands and policies

One grade band contains a label and a minimum score:

```python
GradeBand.create("A", "90")
```

A policy contains ordered bands plus a passing score. Bands must:

- use unique labels;
- use unique minimum scores;
- be ordered from highest to lowest;
- end with a `0.00` floor so every valid score is covered.

## 8. Adding assessments

```python
calculator = GradeCalculator()
calculator.add("Homework", "82.50", "20")
calculator.add("Midterm", "91", "30")
```

If a new assessment would push total weight above `100.00`, the operation raises `ValueError` and does not append the rejected assessment.

## 9. Progress average

`average()` calculates the weighted average normalized over assessments entered so far.

If only 40% of the course has been graded, the current average describes that 40%. It does **not** pretend the missing 60% has a score of zero.

## 10. Progress report versus final report

`report()` can be used before the course is complete. In that state:

```text
complete -> False
passed   -> None
```

`final_report()` requires total weight to equal exactly `100.00`. Only then is pass/fail treated as final.

This distinction prevents an incomplete course from being presented as a completed result.

## 11. Structured reporting

The calculator first returns a `GradeReport` dataclass containing:

```text
assessment_count
total_weight
remaining_weight
average
letter_grade
complete
passed
```

Formatting is a separate operation through `format_report(...)`. Business rules therefore remain testable without parsing printed text.

## 12. Custom grading policy

A caller can replace the default A–F rules:

```python
policy = GradePolicy(
    bands=(
        GradeBand.create("Excellent", "85"),
        GradeBand.create("Satisfactory", "70"),
        GradeBand.create("Needs Improvement", "0"),
    ),
    passing_score=Decimal("70"),
)
```

The calculator code does not need to change when the policy changes.

## 13. Project structure

```text
02-grade-calculator/
├── README.md
├── README.pt-BR.md
├── README.es.md
├── grade_calculator.py
├── demo.py
└── tests/
    ├── conftest.py
    └── test_grade_calculator.py
```

## 14. Run the deterministic demo

From the repository root:

```bash
python practical-projects/02-grade-calculator/demo.py
```

Expected output:

```text
assessments: 4
weight: 100.00
remaining: 0.00
average: 89.65
letter: B
status: complete
passed: yes
```

## 15. Run the project tests

```bash
python -m pytest -q practical-projects/02-grade-calculator/tests
```

The initial suite covers validation, decimal-context isolation, policy boundaries, custom rules, partial reports, exact weighted aggregation, mutation safety, completion rules, and deterministic formatting.

## 16. Failure paths to inspect manually

Try:

```python
calculator.add("Quiz", "101", "10")
calculator.add("Quiz", "90", "0")
calculator.add("Project", "90", "100.01")
calculator.final_report()
```

Read each exception and confirm that rejected assessments do not change the calculator.

## 17. Design note: configuration is data

Letter-grade thresholds are represented by `GradeBand` values instead of a chain of hard-coded `if` statements inside `GradeCalculator`.

That makes policy changes explicit, testable, and independent from aggregation logic.

## 18. Design note: incomplete is a real state

A partial course is not an error. It is a valid state with a current average, remaining weight, and no final pass/fail result yet.

Modeling that state directly is clearer than inventing placeholder scores for unfinished assessments.

## 19. Design note: validate before mutation

`add()` creates and validates an `Assessment`, checks the future combined weight, and only then appends it.

A rejected operation therefore leaves the existing collection unchanged.

## 20. Testing strategy

Tests target public contracts and important boundaries:

- `0.00`, `60.00`, `90.00`, and `100.00` score boundaries;
- weight overflow beyond `100.00`;
- exact completion at `100.00`;
- partial-course behavior;
- policy configuration errors;
- custom policy behavior;
- caller decimal-context isolation.

## 21. What this project intentionally does not include

This version does not include:

- student accounts;
- persistence or a database;
- attendance rules;
- dropped lowest grades;
- bonus points or extra credit;
- multiple courses;
- a GUI;
- charts.

Those features would hide the core lesson: converting configurable rules into small, reliable data contracts and calculations.

## 22. Extension challenge: drop the lowest score

Add an assessment group where the lowest score can be excluded before aggregation. Define how ties and weights should behave before writing code.

## 23. Extension challenge: target-score calculator

Given the remaining weight, calculate the score required on unfinished work to reach a target final average.

Define what should happen when the target is mathematically impossible.

## 24. Extension challenge: multiple students

Create a separate collection that applies one shared `GradePolicy` to multiple student calculators and produces a class summary.

Keep student identity separate from grade calculation rules.

## 25. Extension challenge: alternative rounding policy

Make rounding itself configurable. Compare rounding each assessment contribution separately with rounding only the final weighted average and document the consequences.

## 26. Portfolio discussion

When presenting this project, explain the decisions rather than only saying “it calculates grades”:

- configurable grade policy;
- immutable validated records;
- exact percentage normalization;
- integer-based weighted aggregation;
- explicit partial versus final state;
- no mutation after rejected input;
- structured report separated from presentation;
- boundary-focused automated tests.

## 27. Review checklist

Before considering your own implementation complete, verify:

- Can invalid scores or weights enter the collection?
- Can cumulative weight exceed 100%?
- Does a partial report avoid claiming final pass/fail?
- Does the final report require exactly 100% weight?
- Do grade boundaries behave correctly at exact threshold values?
- Can a different policy be supplied without editing calculator logic?
- Are calculations independent from external decimal context?
- Do tests prove both success and failure paths?

## 28. Next project

Project 02 adds configurable rules and weighted aggregation to the Phase 10 pattern.

The next planned project is **User Registration**, which will focus on identity-like data validation, duplicate prevention, lookup behavior, and clearer service-layer boundaries without introducing real authentication or personal data.
