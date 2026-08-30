<div align="center">

# Project 01 · Expense Tracker

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Back to Practical Projects](../README.md)

This is the first project in **Phase 10: Practical Projects**. The goal is to stop studying concepts in isolation and combine data modeling, functions, collections, exceptions, files, JSON, CSV, `pathlib`, `Decimal`, and `pytest` into one small but complete workflow.

**Estimated study and implementation time:** 180–240 minutes.

## Learning goals

By the end of this project, you should be able to:

- turn a short problem statement into explicit software requirements;
- model one expense as validated structured data;
- use `Decimal` for exact two-decimal monetary values;
- separate validation, storage, filtering, and reporting responsibilities;
- persist records to JSON without silently converting money to binary floating point;
- export the same records to CSV;
- write repeatable automated tests for success and failure paths;
- explain the project as a portfolio artifact rather than only showing code.

## 1. Project brief

Build a small expense tracker that can:

1. register expenses;
2. list stored expenses;
3. filter expenses by category;
4. calculate the complete total;
5. calculate a total for one category;
6. summarize totals by category;
7. save records to JSON;
8. restore records from JSON;
9. export records to CSV;
10. prove the important behavior with automated tests.

The project deliberately starts as a Python module rather than a graphical application. Phase 10 begins by integrating logic and data contracts before adding another interface layer.

## 2. Functional requirements

Each expense must contain:

```text
spent_on    -> date in YYYY-MM-DD format
description -> non-blank text
category    -> non-blank text
amount      -> positive monetary value with two decimal places
```

The tracker must preserve insertion order and expose stored records without giving callers direct access to mutate its internal list.

## 3. Validation requirements

Invalid input must fail explicitly.

Examples:

- invalid date text raises `ValueError`;
- blank description raises `ValueError`;
- blank category raises `ValueError`;
- zero or negative amount raises `ValueError`;
- `NaN` and infinity are rejected;
- JSON with the wrong top-level shape is rejected;
- JSON records missing required fields are rejected.

A failed validation must not append a partial expense to the tracker.

## 4. Why money uses `Decimal`

The project stores amounts with `decimal.Decimal` instead of `float`.

```python
from decimal import Decimal

amount = Decimal("25.90")
```

The amount parser rounds to two decimal places with `ROUND_HALF_UP` after verifying that the value is finite and greater than zero.

This is not a universal accounting engine. It is an explicit project rule for a two-decimal expense tracker.

## 5. The `Expense` data model

`Expense` is an immutable dataclass:

```python
@dataclass(frozen=True, slots=True)
class Expense:
    spent_on: date
    description: str
    category: str
    amount: Decimal
```

Callers normally create records through `Expense.create(...)`, which applies all input normalization before an object exists.

## 6. The tracker service

`ExpenseTracker` owns the collection of expenses and the operations that use that collection.

```python
tracker = ExpenseTracker()
tracker.add("2026-08-29", "Lunch", "Food", "25.40")
tracker.add("2026-08-29", "Bus", "Transport", "12.00")
```

The public `expenses` property returns a tuple, so external code can inspect the current records without receiving the mutable internal list.

## 7. Category filtering

Category matching is case-insensitive:

```python
food_expenses = tracker.filter_by_category("food")
```

`Food`, `food`, and `FOOD` are treated as the same category for filtering and summaries while the first stored spelling remains the display form.

## 8. Totals

The complete total is:

```python
total = tracker.total()
```

A category total is:

```python
food_total = tracker.total("Food")
```

Because every stored amount is already a `Decimal`, the aggregation never crosses into binary floating-point arithmetic.

## 9. Totals by category

The tracker can produce a dictionary such as:

```text
Food      -> 53.90
Transport -> 120.00
```

This operation combines dictionary accumulation, case-insensitive normalization, iteration, and exact decimal arithmetic.

## 10. JSON persistence

`save_json()` writes a list of records.

A monetary amount is serialized as text:

```json
{
  "spent_on": "2026-08-29",
  "description": "Coffee",
  "category": "Food",
  "amount": "8.50"
}
```

Storing the amount as a string makes the decimal representation explicit instead of routing it through a JSON floating-point number.

## 11. JSON restoration

`ExpenseTracker.load_json(...)` parses the file and rebuilds each item through the same validated `Expense.create(...)` path used for new data.

That means persisted data does not bypass validation merely because it came from a file.

## 12. CSV export

`export_csv()` creates this schema:

```text
spent_on,description,category,amount
```

The file is opened with `newline=""`, following the CSV file-boundary contract taught earlier in the curriculum.

## 13. Project structure

```text
01-expense-tracker/
├── README.md
├── README.pt-BR.md
├── README.es.md
├── expense_tracker.py
├── demo.py
└── tests/
    ├── conftest.py
    └── test_expense_tracker.py
```

The project is intentionally small enough to understand in one sitting while still containing production-like boundaries: model, service behavior, persistence, export, demo, and tests.

## 14. Run the deterministic demo

From the repository root:

```bash
python practical-projects/01-expense-tracker/demo.py
```

Expected output:

```text
expenses: 3
total: 173.90
food: 53.90
transport: 120.00
json round-trip: True
csv rows: 3
```

The demo uses a temporary directory, so it does not leave JSON or CSV files in the repository.

## 15. Run the project tests

```bash
python -m pytest -q practical-projects/01-expense-tracker/tests
```

The initial suite covers:

- field normalization;
- half-up amount rounding;
- rejection of invalid monetary values;
- complete totals;
- category totals and case-insensitive filtering;
- JSON round-trip behavior;
- rejection of an invalid JSON top-level shape;
- exact CSV header and row output.

## 16. Design note: one validation path

New user data and restored JSON records both eventually call `Expense.create(...)`.

This avoids two competing validation systems:

```text
new input ----\
              -> Expense.create -> validated Expense
JSON record --/
```

One validation boundary is easier to reason about and test.

## 17. Design note: immutable records, mutable collection

An individual `Expense` is frozen, but the tracker can append new valid expenses.

That split reflects two different responsibilities:

- an expense record represents a fact that should not change accidentally;
- the tracker represents a collection that grows as new expenses are registered.

## 18. Design note: persistence is explicit

Adding an expense changes memory. Saving JSON changes a file.

The tracker does not silently write to disk every time `add()` runs. Keeping these operations explicit makes side effects easier to see, test, and later replace.

## 19. Failure paths to inspect manually

Try these calls and read the exceptions:

```python
tracker.add("not-a-date", "Lunch", "Food", "10.00")
tracker.add("2026-08-29", "", "Food", "10.00")
tracker.add("2026-08-29", "Lunch", "Food", "0")
tracker.add("2026-08-29", "Lunch", "Food", "NaN")
```

The purpose is not only to see failures. Confirm that the tracker remains unchanged after each rejected input.

## 20. Testing strategy

The tests focus on observable contracts instead of private implementation details.

For example, the CSV test checks the resulting file rather than asserting how many times `csv.DictWriter.writerow()` was called.

This keeps future refactoring possible as long as public behavior remains correct.

## 21. What this project intentionally does not include yet

The first version does not include:

- a graphical interface;
- a database;
- authentication;
- cloud synchronization;
- multiple currencies;
- recurring expenses;
- budgets;
- editing or deleting records;
- charts.

A small project with clear boundaries is more useful for learning than a large project with half-finished features.

## 22. Extension challenge: add date filtering

Add methods for:

- one exact date;
- a start/end date range;
- one month.

Write boundary tests before adding presentation code.

## 23. Extension challenge: editing and deletion

Introduce a stable expense identifier and then implement deliberate update/delete behavior.

Think about what happens if an identifier does not exist and whether persisted files should preserve identifiers across reloads.

## 24. Extension challenge: monthly budgets

Add a budget per category and calculate:

```text
budget
spent
remaining
percentage used
```

Keep money in `Decimal` throughout the pipeline.

## 25. Extension challenge: pandas report

Load exported CSV data with pandas and produce a monthly/category summary.

The goal is not to replace the core tracker with pandas. It is to use pandas at the analytical boundary where tabular transformation becomes useful.

## 26. Extension challenge: Excel report

Use openpyxl to generate a workbook with:

- raw expenses;
- category summary;
- monthly summary;
- number formats;
- a table.

This directly connects Project 01 back to Phase 9.

## 27. Portfolio discussion

When presenting the project, do not describe it only as “an expense tracker.” Explain the engineering decisions:

- exact money with `Decimal`;
- immutable validated records;
- one validation path for new and persisted data;
- JSON round-trip preservation;
- CSV interoperability;
- case-insensitive category behavior;
- deterministic automated tests;
- temporary files in demos/tests to avoid repository pollution.

Those decisions demonstrate more skill than the number of lines in the program.

## 28. Review checklist

Before considering your own implementation complete, verify:

- Does every invalid record fail before mutation?
- Are money calculations exact under the declared two-decimal rule?
- Can JSON data be saved and restored without changing records?
- Is CSV output readable by another tool?
- Are category rules explicit?
- Are filesystem side effects intentional?
- Do tests cover both success and failure paths?
- Can another developer understand the project structure without asking you where the important code lives?

## 29. Next project

Project 01 establishes the Phase 10 pattern: **requirements → design → implementation → tests → explanation → extensions → portfolio discussion**.

The next planned project is the **Grade Calculator**, which will focus on configurable rules, aggregation, validation, and reporting without repeating the persistence design of this project.
