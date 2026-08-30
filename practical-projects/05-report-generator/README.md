<div align="center">

# Project 05 · Report Generator

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Back to Practical Projects](../README.md)

This is the fifth project in **Phase 10: Practical Projects**. It focuses on turning validated domain records into a trustworthy reporting pipeline: explicit reporting windows, deterministic aggregation, presentation-independent summaries, multiple renderers, and safe text-file output.

**Estimated study and implementation time:** 180–240 minutes.

## Learning goals

By the end of this project, you should be able to:

- model report source data with validated immutable records;
- define an inclusive reporting window explicitly;
- reject duplicate source identifiers before aggregation;
- separate source records from records included in a report period;
- calculate status, duration, percentage, and grouped-team metrics deterministically;
- represent aggregate results with validated immutable summary objects;
- keep report construction separate from report rendering;
- render the same report as plain text or Markdown;
- escape Markdown table delimiters in user-facing values;
- write UTF-8 report files through an explicit format/suffix contract;
- test empty periods, boundary dates, ordering, rounding, rendering, and file output.

## 1. Project brief

Build a report generator for a fictional operational activity dataset.

The generator must:

1. validate immutable activity records;
2. define an inclusive date window for each report;
3. reject duplicate activity identifiers in the source dataset;
4. include only records whose dates fall inside the requested period;
5. sort included records deterministically;
6. calculate summary metrics independently from presentation;
7. preserve case-insensitive team grouping while retaining the first accepted display spelling;
8. render the same report as TXT-style plain text or Markdown;
9. require the output filename suffix to match the selected report format;
10. write UTF-8 files without silently creating missing directories;
11. prove the reporting contract with automated tests.

All example data is fictional.

## 2. Reporting pipeline

The central learning model is:

```text
validated records
    -> source validation
    -> inclusive date filtering
    -> deterministic ordering
    -> validated summary
    -> immutable report
    -> renderer
    -> optional file write
```

The important idea is that aggregation, presentation, and persistence are different responsibilities.

## 3. Activity record contract

A valid source item is represented by `ActivityRecord`:

```python
ActivityRecord(
    activity_id=101,
    team="Accounting",
    status=WorkStatus.COMPLETED,
    duration_minutes=30,
    occurred_on=date(2026, 8, 1),
)
```

The record requires:

```text
activity_id      -> positive integer, bool excluded
team             -> non-blank readable text, normalized whitespace
a status          -> WorkStatus enum value
duration_minutes -> non-negative integer, bool excluded
occurred_on      -> plain datetime.date value
```

The dataclass is frozen and uses slots so downstream reporting code receives a stable value object.

## 4. Readable text normalization

Titles and team names collapse surrounding and repeated whitespace.

For example:

```python
team="  Shared   Services  "
```

becomes:

```text
Shared Services
```

Blank values and values beyond the small project length limits are rejected.

The goal is not aggressive text correction. It is a narrow, visible normalization contract.

## 5. Explicit workflow states

The project uses:

```python
class WorkStatus(str, Enum):
    COMPLETED = "completed"
    IN_PROGRESS = "in_progress"
    BLOCKED = "blocked"
```

A raw string such as `"completed"` is not accepted by the record constructor.

That keeps the domain boundary explicit after data has already been validated.

## 6. Reporting window

`ReportWindow` contains:

```text
title
start_date
end_date
```

Both dates are inclusive.

For a window from `2026-08-01` through `2026-08-31`, records on both boundary dates are included.

A start date after the end date is rejected.

## 7. Plain dates instead of datetimes

This project deliberately requires exact `datetime.date` values at the domain boundary rather than accepting `datetime.datetime` subclasses silently.

The report groups activities by calendar date, so accepting time-bearing values would create a wider contract than the project needs.

## 8. Source identity validation

`activity_id` is unique across the entire source collection supplied to one report operation.

Duplicate IDs are rejected before date filtering.

That means an out-of-period duplicate still makes the source dataset invalid.

This rule treats identity validity as a property of the source, not a side effect of the selected reporting period.

## 9. Inclusive period filtering

`build_report(...)` validates the source first and then keeps records where:

```python
start_date <= record.occurred_on <= end_date
```

The resulting report keeps both:

```text
source_record_count
included records
```

From those values it can expose the number of excluded records without losing visibility into the original dataset size.

## 10. Deterministic record ordering

Included records are sorted by:

```text
occurred_on
activity_id
```

This means equivalent source collections produce the same report ordering even if the caller supplied records in a different order.

Deterministic ordering makes tests, diffs, and generated artifacts easier to trust.

## 11. Summary metrics

`summarize_activities(...)` calculates:

- total records;
- completed records;
- in-progress records;
- blocked records;
- total duration;
- average duration;
- longest duration;
- completion percentage;
- count by team.

The summary is represented by `ReportSummary` rather than an unstructured dictionary.

## 12. Exact two-decimal rounding

Average duration and completion percentage use `Decimal` values with two decimal places.

The project calculates integer scaled units and applies half-up rounding explicitly.

For example:

```text
31 minutes / 3 records -> 10.33
2 completed / 3 total  -> 66.67%
3 minutes / 8 records  -> 0.38
```

The calculation does not depend on the caller's global decimal context.

## 13. Why not use float for report metrics

Binary floating-point is excellent for many scientific and general calculations, but presentation-oriented decimal metrics often need a visible rounding policy.

This project makes that policy explicit because a report should not change formatting based on hidden numeric context.

## 14. Team grouping

Team comparison is case-insensitive.

These records:

```text
Accounting
accounting
```

belong to one logical group.

The first accepted spelling becomes the display name, and the final groups are sorted case-insensitively for deterministic output.

## 15. Empty reporting periods

A report with no included records is still valid.

Its summary contains:

```text
total records: 0
all status counts: 0
total duration: 0
average duration: 0.00
longest duration: 0
completion: 0.00%
team counts: empty
```

Both renderers show an explicit empty-state message instead of failing with division by zero or producing an ambiguous blank section.

## 16. Summary invariants

`ReportSummary` validates its public constructor.

Among its checks:

- status counts must sum to total records;
- duration fields cannot be negative;
- average duration must match total duration and record count;
- completion percentage must match completed and total counts;
- longest duration must be mathematically possible;
- team counts must use normalized names;
- team names must be unique case-insensitively;
- team counts must be sorted deterministically;
- team totals must equal total records.

A summary object is therefore more than a bag of numbers.

## 17. Immutable report boundary

`OperationalReport` combines:

```text
ReportWindow
source_record_count
included ActivityRecord tuple
ReportSummary
```

It validates that included records are sorted, unique by ID, and inside the reporting window.

The public boundary uses tuples so report contents do not expose mutable internal lists.

## 18. Construction versus presentation

`build_report(...)` does not decide whether the final document is TXT or Markdown.

That separation allows the same validated report object to be rendered several ways:

```python
report = build_report(...)

text = render_report(report, ReportFormat.TEXT)
markdown = render_report(report, ReportFormat.MARKDOWN)
```

The business result does not need to be recalculated for each presentation format.

## 19. Plain-text renderer

`render_text_report(...)` produces a CLI-friendly document with:

```text
title
period
source/included/excluded counts
summary
team counts
ordered record details
```

The output always ends with exactly one newline so file comparisons are stable.

## 20. Markdown renderer

`render_markdown_report(...)` produces:

- a level-one title;
- a period line;
- a summary table;
- team counts;
- a record table.

The same report content is expressed through a different presentation layer rather than through different aggregation logic.

## 21. Markdown delimiter escaping

Team names may contain a vertical bar (`|`) or backslash.

Because `|` has structural meaning inside Markdown tables, renderer output escapes backslashes first and then table delimiters.

This is a small but important example of adapting validated domain text to the syntax of an output format.

## 22. Explicit format dispatch

The generic renderer accepts only:

```python
ReportFormat.TEXT
ReportFormat.MARKDOWN
```

Passing a plain string such as `"text"` is rejected.

After validation, the program works with explicit enum values instead of repeatedly interpreting raw configuration text.

## 23. File suffix contract

`write_report(...)` requires the destination suffix to match the selected format:

```text
ReportFormat.TEXT     -> .txt
ReportFormat.MARKDOWN -> .md
```

Suffix comparison is case-insensitive, so `REPORT.TXT` is valid for the text renderer.

A missing or mismatched suffix is rejected before writing.

## 24. UTF-8 output

Reports are written with:

```python
encoding="utf-8"
newline="\n"
```

This makes the file contract visible and keeps generated text consistent across supported environments.

## 25. Missing directories are not created

This project writes one requested report file, but it deliberately does **not** create missing parent directories.

If the destination parent does not exist, the normal `FileNotFoundError` is allowed to propagate.

Directory discovery, creation, movement, and organization belong to the next project: **File Organizer**.

## 26. Project structure

```text
05-report-generator/
├── README.md
├── README.pt-BR.md
├── README.es.md
├── report_generator.py
├── demo.py
└── tests/
    ├── conftest.py
    └── test_report_generator.py
```

## 27. Run the deterministic demo

From the repository root:

```bash
python practical-projects/05-report-generator/demo.py
```

Expected beginning of the output:

```text
August Operations
=================
period: 2026-08-01 to 2026-08-31
source records: 4
included records: 3
excluded records: 1

SUMMARY
completed: 1
in progress: 1
blocked: 1
completion: 33.33%
```

The fourth fictional record is outside August so the demo makes source-versus-included behavior visible.

## 28. Run the project tests

```bash
python -m pytest -q practical-projects/05-report-generator/tests
```

The initial suite contains **70 pytest scenarios** covering immutable model validation, text normalization, enum boundaries, date-window rules, duplicate IDs, aggregation, two-decimal rounding, case-insensitive grouping, empty reports, deterministic ordering, summary invariants, TXT rendering, Markdown rendering and escaping, renderer dispatch, suffix validation, UTF-8 writes, and filesystem failure behavior.

## 29. Failure paths to inspect manually

Try changing the demo or your own calls to include:

```text
activity_id = 0
duplicate activity_id
blank team
status = "completed" instead of WorkStatus.COMPLETED
negative duration
datetime instead of date
start_date after end_date
output format = "text" instead of ReportFormat.TEXT
Markdown output written to report.txt
missing destination directory
```

Observe whether the problem belongs to the record, report window, source collection, renderer, or filesystem boundary.

## 30. Design note: one summary, several renderers

A common reporting mistake is to mix calculations directly into presentation code.

That makes every new output format repeat business logic.

This project instead builds one validated report model and lets each renderer translate that model into its own syntax.

## 31. Design note: validate before filtering

Duplicate identifiers are checked before the reporting period is applied.

That is deliberate.

If source correctness changed depending on a date filter, the same dataset could be considered valid in one report and invalid in another simply because a duplicate happened to fall outside the selected period.

## 32. Design note: reporting is a boundary

A report is not only a string.

It connects:

```text
domain data
aggregation rules
ordering rules
presentation syntax
filesystem output
```

Keeping those steps explicit makes the workflow easier to test and evolve.

## 33. What this project intentionally does not include

This version does not include:

- CSV parsing;
- Excel workbooks;
- pandas;
- charts or dashboards;
- PDF generation;
- HTML templates;
- email delivery;
- automatic directory creation;
- filename collision handling;
- recursive filesystem organization;
- database persistence;
- locale-aware date or number formatting;
- a GUI.

Those features are useful, but they would blur the reporting lesson or overlap later projects.

## 34. Extension challenge: JSON renderer

Add `ReportFormat.JSON` and render the report as structured JSON.

Decide whether dates and enum values should become strings at the renderer boundary and test deterministic key ordering where relevant.

## 35. Extension challenge: grouped duration metrics

Extend team summaries to include:

```text
record count
total duration
average duration
completion percentage
```

Consider whether a dedicated immutable `TeamSummary` model becomes clearer than nested tuples.

## 36. Extension challenge: optional detail section

Allow callers to request a summary-only report.

Keep report calculation unchanged and decide whether the detail choice belongs in the report model or only in renderer configuration.

## 37. Portfolio discussion

When presenting this project, explain more than “it writes a report.”

Useful engineering talking points include:

- immutable validated source records;
- explicit inclusive reporting windows;
- dataset-level identity validation;
- deterministic filtering and ordering;
- exact decimal rounding for presentation metrics;
- case-insensitive grouping with stable display names;
- summary invariants;
- separation of report construction and rendering;
- multiple output formats from one domain result;
- output-format escaping;
- explicit UTF-8 and filename-suffix contracts;
- deliberate scope boundaries before the File Organizer project.

## 38. Review checklist

Before considering your own implementation complete, verify:

- Are source records validated before reporting begins?
- Are Boolean values prevented from masquerading as integers?
- Are duplicate activity IDs rejected before date filtering?
- Are both report boundary dates inclusive?
- Are included records sorted deterministically?
- Do status counts equal the report total?
- Is average-duration rounding explicit and stable?
- Is completion percentage deterministic?
- Are team groups case-insensitive and stably ordered?
- Does the report object use immutable public collections?
- Can the same report be rendered without recalculating metrics?
- Are Markdown table delimiters escaped?
- Does each format require its matching file suffix?
- Are UTF-8 and newline behavior explicit?
- Are missing directories left for the caller or the next project to manage?
- Are all examples fictional and public-safe?

## 39. Next project

Project 05 turns validated records into deterministic report artifacts while keeping aggregation, rendering, and persistence separate.

Next, **Project 06: File Organizer** shifts attention from the contents of one output file to controlled filesystem workflows: discovering files, classifying them, planning moves, handling collisions, and keeping operations safe and testable.
