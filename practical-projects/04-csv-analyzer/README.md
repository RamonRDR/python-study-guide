<div align="center">

# Project 04 · CSV Analyzer

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Back to Practical Projects](../README.md)

This is the fourth project in **Phase 10: Practical Projects**. It focuses on CSV boundaries, explicit schemas, typed row conversion, row-level validation, structural failures, deterministic aggregation, and testable analysis without depending on pandas.

**Estimated study and implementation time:** 180–240 minutes.

## Learning goals

By the end of this project, you should be able to:

- define an exact CSV schema instead of assuming any table is acceptable;
- distinguish malformed CSV structure from invalid row data;
- convert text fields into `int`, `bool`, `date`, and `Enum` values;
- keep valid rows even when other rows fail validation;
- report multiple field problems for one rejected row;
- detect duplicate identifiers across accepted rows;
- keep parser results immutable at the public boundary;
- aggregate records deterministically without hidden float rounding;
- filter validated records without mutating them;
- test headers, malformed input, conversion rules, rejection behavior, and summaries.

## 1. Project brief

Build a CSV analyzer for a fictional incident dataset.

The analyzer must:

1. require an exact header schema;
2. read UTF-8 CSV files with an optional UTF-8 BOM;
3. parse incident rows into typed immutable records;
4. collect row-level validation problems instead of discarding all good data;
5. reject duplicate accepted `event_id` values;
6. distinguish document-level schema/format errors from row-level data errors;
7. summarize valid records;
8. filter valid records by severity, resolution state, or service;
9. format a deterministic text report;
10. prove success and failure behavior with automated tests.

## 2. Dataset contract

The exact required header is:

```text
event_id,service,severity,duration_minutes,resolved,occurred_on
```

Each column has a different contract:

```text
event_id         -> positive ASCII integer
service          -> non-blank readable text, normalized whitespace
severity         -> low | medium | high | critical
duration_minutes -> non-negative ASCII integer
resolved         -> true | false
occurred_on      -> exact YYYY-MM-DD calendar date
```

All example records are fictional.

## 3. Why the header is strict

CSV is only a container format. A file being valid CSV does not mean it contains the table your program expects.

These are different schemas:

```text
event_id,service,severity,duration_minutes,resolved,occurred_on
```

and:

```text
service,event_id,severity,duration_minutes,resolved,occurred_on
```

This project deliberately requires the exact names and order in `EXPECTED_HEADERS`.

That makes schema drift visible instead of silently mapping the wrong data.

## 4. Structural errors versus row errors

The analyzer separates two failure levels.

### Document-level failures

Examples:

- no header row;
- duplicate header names;
- wrong header order or names;
- malformed quoting rejected by Python's CSV parser.

These raise `CsvSchemaError` or `CsvFormatError` because the document cannot be trusted as the expected table.

### Row-level failures

Examples:

- `event_id` is zero;
- severity is `urgent`;
- duration is negative;
- resolved is `yes`;
- date is `2026-02-30`;
- a row has extra or missing values.

These create a `RejectedRow`. Other valid rows remain available for analysis.

## 5. Typed conversion

`csv.DictReader` returns text values. The project does not leave everything as strings.

A valid row becomes:

```python
IncidentRecord(
    event_id=101,
    service="Payments",
    severity=Severity.HIGH,
    duration_minutes=45,
    resolved=True,
    occurred_on=date(2026, 8, 1),
)
```

This moves conversion errors to the input boundary and gives the rest of the program stronger types.

## 6. Integer contracts

Two helpers make numeric intent explicit:

```python
parse_positive_integer(...)
parse_non_negative_integer(...)
```

`event_id` must be greater than zero.

`duration_minutes` may be zero.

The parsers accept ASCII decimal digits only. Values such as `-1`, `1.5`, and full-width Unicode digits are rejected under this project contract.

## 7. Service normalization

Service names are display-oriented text.

The analyzer collapses surrounding and repeated whitespace:

```python
normalize_service("  Data   Sync ")
# "Data Sync"
```

It preserves casing and enforces a small project length limit.

For grouping and filtering, service comparison is case-insensitive while the first accepted display spelling is retained in the summary.

## 8. Severity as an enum

Severity uses:

```python
class Severity(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"
```

Input is case-insensitive, so `HIGH`, `high`, and ` High ` become `Severity.HIGH`.

Unknown values are rejected rather than entering the model as arbitrary text.

## 9. Strict Boolean parsing

The `resolved` column accepts only:

```text
true
false
```

with surrounding whitespace and case ignored.

Values such as `yes`, `1`, or `truthy` are rejected.

This avoids inventing surprising truthiness rules for external data.

## 10. Strict date parsing

Dates must use exactly:

```text
YYYY-MM-DD
```

The parser checks both shape and calendar validity.

So:

```text
2024-02-29 -> valid
2026-2-01  -> invalid shape
20260201   -> invalid shape
2026-02-30 -> invalid calendar date
```

The result is a real `datetime.date`, not a date-looking string.

## 11. Immutable valid records

`IncidentRecord` is a frozen dataclass with slots.

Validation also runs for direct constructor calls, so the model cannot be bypassed simply by skipping the CSV parser.

The parser returns tuples of records instead of exposing mutable internal lists.

## 12. Field-level issues

One bad row may contain several independent problems.

For example:

```text
0, ,urgent,-2,yes,2026-02-30
```

produces issues for:

```text
event_id
service
severity
duration_minutes
resolved
occurred_on
```

The project collects all those field problems for the logical row rather than stopping at the first one.

## 13. Logical row numbers

`RejectedRow.row_number` identifies the logical CSV row, with the header considered row 1 and the first data row considered row 2.

Blank physical lines are ignored by Python's CSV reader.

This project uses logical record numbering rather than promising exact physical line numbers for every possible quoted multiline CSV field.

## 14. Extra and missing values

A row with more values than the schema allows is rejected with an `_row` issue.

A row with a missing trailing field passes `None` to that field parser and is rejected by the matching field contract.

This prevents truncated or shifted data from looking valid.

## 15. Duplicate identifiers

`event_id` must be unique among **accepted valid rows**.

If a valid `event_id=101` has already been accepted, a later valid row with `event_id=101` is rejected.

An earlier invalid row does not reserve its ID. A later valid row may therefore use the same ID.

This rule makes the accepted dataset the source of uniqueness.

## 16. File loading and UTF-8 BOM

`load_incident_csv(...)` opens files with:

```python
encoding="utf-8-sig"
newline=""
```

`utf-8-sig` accepts a normal UTF-8 file and removes one optional UTF-8 BOM at the start.

`newline=""` follows Python's CSV guidance so the CSV module controls newline handling.

Missing files intentionally propagate `FileNotFoundError`.

## 17. Text and stream entry points

The project exposes three input boundaries:

```python
parse_incident_csv(stream)
parse_incident_csv_text(text)
load_incident_csv(path)
```

The core parsing behavior remains centralized in `parse_incident_csv(...)`.

That keeps file I/O separate from row conversion and makes tests easy to write with `StringIO` or literal strings.

## 18. Parse result

Successful parsing returns:

```python
CsvLoadResult(
    records=(...),
    rejected_rows=(...),
)
```

Convenience properties expose:

```text
valid_count
rejected_count
data_row_count
```

`data_row_count` counts logical accepted plus rejected data rows, not the header.

## 19. Deterministic aggregation

`summarize_incidents(...)` calculates:

- total valid records;
- resolved and unresolved counts;
- total duration;
- average duration to two decimal places;
- longest duration;
- count by every severity;
- count by service.

Service counts are sorted case-insensitively for stable output.

Severity counts always follow enum order:

```text
low
medium
high
critical
```

## 20. Exact average rounding

The average is returned as `Decimal` with two decimal places.

The implementation does not depend on the caller's global `decimal` context. It calculates integer hundredths directly and applies half-up rounding.

For example, an exact average of `0.375` becomes:

```text
0.38
```

That keeps report formatting deterministic.

## 21. Empty analysis

An empty valid dataset is still analyzable.

The summary returns:

```text
total records: 0
average duration: 0.00
longest duration: 0
service counts: empty
all severity counts: 0
```

No division-by-zero exception is needed.

## 22. Summary invariants

`IncidentSummary` validates its own public constructor.

Among other checks:

- resolved + unresolved must equal total;
- average duration must match total duration divided by the record count;
- longest duration cannot exceed total duration, with empty and one-record summaries enforcing their obvious duration constraints;
- severity counts must contain every enum value exactly once;
- severity totals must equal total records;
- service keys must be unique case-insensitively;
- service counts must be deterministically sorted;
- service totals must equal total records.

A summary that contradicts itself is rejected.

## 23. Filtering

`filter_incidents(...)` can combine optional criteria:

```python
filter_incidents(
    records,
    severity=Severity.HIGH,
    resolved=True,
    service="Payments",
)
```

The function returns a tuple and does not mutate the original collection.

Service matching is case-insensitive after the same whitespace normalization used by the record model.

## 24. Deterministic text report

`format_analysis(...)` produces a stable CLI-style report:

```text
data rows: 6
valid: 4
rejected: 2
resolved: 3
unresolved: 1
total duration: 165
average duration: 41.25
longest duration: 90
```

It also verifies that the supplied summary belongs to the same number of valid rows as the parse result.

## 25. Project structure

```text
04-csv-analyzer/
├── README.md
├── README.pt-BR.md
├── README.es.md
├── csv_analyzer.py
├── demo.py
└── tests/
    ├── conftest.py
    └── test_csv_analyzer.py
```

## 26. Run the deterministic demo

From the repository root:

```bash
python practical-projects/04-csv-analyzer/demo.py
```

Expected output:

```text
data rows: 6
valid: 4
rejected: 2
resolved: 3
unresolved: 1
total duration: 165
average duration: 41.25
longest duration: 90
critical: 1
```

The demo intentionally contains two invalid rows so rejection behavior is visible.

## 27. Run the project tests

```bash
python -m pytest -q practical-projects/04-csv-analyzer/tests
```

The initial suite contains **75 pytest scenarios** covering parsing helpers, direct model validation, schema failures, malformed CSV, field-level row issues, duplicate IDs, UTF-8 BOM handling, file loading, aggregation invariants, filtering, and deterministic reporting.

## 28. Failure paths to inspect manually

Try changing the demo data to include:

```text
wrong header order
missing occurred_on value
extra seventh value
severity = urgent
resolved = yes
occurred_on = 2026-02-30
duplicate valid event_id
```

Observe which problems stop the document and which reject only one row.

## 29. Design note: parse at the boundary

The rest of the analyzer should not repeatedly ask whether `"45"` is a number or whether `"true"` means a Boolean.

Those conversions happen once at the CSV boundary.

After a row becomes `IncidentRecord`, downstream functions can rely on its types and invariants.

## 30. Design note: useful partial success

Many import workflows must decide whether one invalid row should destroy every valid row.

This project chooses:

```text
invalid document structure -> stop
invalid row data           -> reject row, keep valid rows
```

That is not the only possible policy, but it is explicit, testable, and useful for learning data-ingestion design.

## 31. Design note: standard library before pandas

Phase 9 already introduced pandas. This project intentionally uses Python's `csv` module instead.

The goal is to expose the mechanics pandas often hides:

- schema expectations;
- raw string conversion;
- missing and extra fields;
- row rejection policy;
- duplicate identity checks;
- immutable domain records.

Understanding those boundaries makes later dataframe work easier to reason about.

## 32. What this project intentionally does not include

This version does not include:

- automatic delimiter detection;
- arbitrary user-defined schemas;
- pandas;
- Excel input;
- database persistence;
- streaming datasets larger than memory;
- parallel processing;
- fuzzy correction of invalid values;
- charts or dashboards;
- a GUI.

Those are possible extensions, but they would dilute the core ingestion and validation lesson.

## 33. Extension challenge: configurable schema

Extract the field rules into reusable column specifications.

A later version could define:

```text
column name
required/optional
parser
normalizer
default value
uniqueness rule
```

Keep the current project simple before generalizing it.

## 34. Extension challenge: rejection export

Write rejected logical rows and their issue messages to a second CSV file.

Think carefully about:

- stable columns;
- quoting;
- multiple issues per row;
- whether to preserve raw values;
- CSV formula-injection risks if that file will be opened in spreadsheet software.

## 35. Extension challenge: date filters

Add optional start/end dates to `filter_incidents(...)`.

Define whether boundaries are inclusive and test invalid ranges such as start date after end date.

## 36. Portfolio discussion

When presenting this project, explain more than “it reads CSV files.”

Useful engineering talking points include:

- exact schema contracts;
- structural versus row-level failures;
- typed conversion at the data boundary;
- immutable accepted records;
- multi-field rejection diagnostics;
- duplicate detection across valid rows;
- deterministic aggregation and rounding;
- public summary invariants;
- testable file, stream, and text entry points;
- deliberate use of the standard library instead of hiding ingestion behavior behind pandas.

## 37. Review checklist

Before considering your own implementation complete, verify:

- Are header names and order checked before data rows are trusted?
- Are duplicate header names rejected?
- Does malformed CSV raise a document-level error?
- Can one bad row coexist with valid rows in the result?
- Are all field problems for a rejected row visible?
- Are extra and missing values detected?
- Are accepted `event_id` values unique?
- Does an invalid row avoid reserving its ID?
- Are dates real `date` objects after parsing?
- Is Boolean parsing explicit rather than based on truthiness?
- Are summary counts internally consistent?
- Is average rounding deterministic?
- Are filters non-mutating?
- Are examples fictional and public-safe?

## 38. Next project

Project 04 adds schema-aware CSV ingestion, row-level validation, typed conversion, partial-success policy, deterministic filtering, and aggregation to the Phase 10 progression.

The next planned project is **Report Generator**, which will shift the focus from ingesting structured data to composing structured output and presentation-ready reports.
