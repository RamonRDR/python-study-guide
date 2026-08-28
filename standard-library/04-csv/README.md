<div align="center">

# Controlling CSV Dialects and Tabular Text Contracts

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Back to Standard Library](../README.md) · [← Previous: Controlling JSON Serialization and Decoding Contracts](../03-json/README.md)

Phase 7 introduced CSV as a tabular file format and taught the practical use of `csv.reader()`, `csv.writer()`, `csv.DictReader()`, and `csv.DictWriter()`. This chapter goes one layer deeper.

The `csv` module is not only a way to split rows into columns. It is a boundary tool for defining how delimiters, quoting, escaping, line endings, headers, missing fields, extra fields, and type conversion behave between systems.

The goal is to turn "this is a CSV file" into a more precise question:

```text
What tabular text contract does this program accept and produce?
```

**Estimated study time:** 120–160 minutes.

**Python requirement:** Python 3.10 or newer for the core APIs taught here. `csv.QUOTE_NOTNULL` and `csv.QUOTE_STRINGS` were added in Python 3.12 and their writer behavior is available there. Because of a documented Python 3.12 bug, their special reader behavior requires Python 3.13 or newer.

**Documentation baseline:** behavior and examples were checked against the official Python 3.14 `csv` documentation.

## Learning objectives

By the end of this chapter, you should be able to:

- treat CSV as a family of tabular-text contracts rather than one universal layout;
- separate text encoding from CSV dialect rules;
- explain why CSV file objects should be opened with `newline=""`;
- distinguish logical CSV records from physical text lines;
- configure delimiters, quote characters, escaping, and line terminators deliberately;
- explain the behavior of the main `QUOTE_*` modes;
- recognize the type-conversion behavior of `QUOTE_NONNUMERIC`;
- understand the Python 3.12+ writer behavior of `QUOTE_NOTNULL` and `QUOTE_STRINGS`, plus their corrected reader semantics in Python 3.13+;
- explain why the default writer conversion of `None` is lossy;
- validate `DictReader` headers and irregular row widths;
- control extra and missing keys with `DictWriter`;
- use `strict=True` and `csv.Error` where malformed input should fail visibly;
- use `field_size_limit()` as one input-boundary control;
- treat `Sniffer` and `has_header()` as heuristics rather than authorities;
- handle UTF-8 BOMs only when the surrounding interface requires them;
- distinguish CSV parsing safety from spreadsheet formula interpretation;
- design explicit, testable CSV import and export contracts.

## 1. What changes from the Phase 7 CSV introduction?

You already know the core row-oriented APIs:

```python
import csv

with open("records.csv", "r", encoding="utf-8", newline="") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
```

and the dictionary-oriented variants:

```python
import csv

with open("records.csv", "r", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["name"])
```

Phase 7 focused on choosing the correct parser and keeping parsing separate from validation.

This chapter focuses on the policy around the parser:

```text
text bytes
   ↓ character decoding
Python text
   ↓ CSV dialect + parsing policy
rows and fields
   ↓ schema + type validation
trusted application values
```

The APIs are familiar. The contract is deeper.

## 2. CSV is not one universal dialect

The name CSV suggests comma-separated values, but real tabular-text interfaces differ in several ways:

- delimiter;
- quote character;
- escaping rule;
- line terminator;
- whether spaces after delimiters are significant;
- whether malformed input should be accepted or rejected;
- whether a header exists;
- what column names mean;
- which text encoding carries the file.

RFC 4180 documents a common CSV format and the `text/csv` media type, but it is informational and does not eliminate the many dialects used in practice.

A filename ending in `.csv` is therefore not a complete parsing contract.

## 3. Text encoding and CSV dialect are separate layers

A CSV parser operates on text. If the source is stored as bytes, character decoding happens first.

Keep these layers separate:

```text
bytes
   ↓ UTF-8, UTF-8 with BOM, or another declared encoding
text
   ↓ delimiter + quoting + escaping rules
fields
```

For a UTF-8 contract:

```python
with open("records.csv", "r", encoding="utf-8", newline="") as file:
    reader = csv.reader(file)
```

Changing `delimiter=","` to `delimiter=";"` does not change the character encoding. Changing `encoding="utf-8"` does not choose the CSV delimiter.

## 4. Use `newline=""` for CSV file objects

When a real file object is passed to the `csv` module, open it with `newline=""`:

```python
import csv

with open("records.csv", "r", encoding="utf-8", newline="") as file:
    reader = csv.reader(file)
    rows = list(reader)
```

The `csv` module performs its own newline handling. The official documentation notes that omitting `newline=""` can break embedded newlines inside quoted fields and can introduce an extra carriage return when writing on platforms that use `\r\n` line endings.

Treat `newline=""` as part of the CSV file-I/O pattern, not as decorative syntax.

## 5. A CSV record can span multiple physical lines

This is one logical CSV record:

```text
name,note
Ada,"first line
second line"
```

The newline inside the quoted field belongs to the field data. It does not necessarily end the CSV record.

That is why code such as this is unsafe for general CSV parsing:

```python
for line in file:
    columns = line.split(",")
```

A CSV parser understands quoting and record boundaries. A physical-line loop does not have enough information by itself.

## 6. A dialect groups formatting decisions

Python groups related CSV formatting options into a **dialect**.

A dialect can define settings such as:

- `delimiter`;
- `quotechar`;
- `doublequote`;
- `escapechar`;
- `lineterminator`;
- `quoting`;
- `skipinitialspace`;
- `strict`.

You can pass a named dialect:

```python
reader = csv.reader(file, dialect="excel")
```

or pass formatting parameters directly:

```python
reader = csv.reader(
    file,
    delimiter=";",
    quotechar='"',
    strict=True,
)
```

The important part is not whether the policy is named or inline. The important part is that the producer and consumer agree on it.

## 7. Python includes several registered dialects

Common built-in names include:

- `excel`;
- `excel-tab`;
- `unix`.

You can inspect registered names:

```python
import csv

print(csv.list_dialects())
```

Do not assume that a file produced by a spreadsheet program automatically matches every detail of Python's `excel` dialect. Export settings, locale, application behavior, and downstream transformations can change the actual text contract.

Inspect or document the interface you truly receive.

## 8. Register a named dialect when reuse improves clarity

A controlled application can register a repeated dialect policy:

```python
import csv

csv.register_dialect(
    "study_semicolon",
    delimiter=";",
    quotechar='"',
    quoting=csv.QUOTE_MINIMAL,
    lineterminator="\n",
)
```

It can then be reused:

```python
reader = csv.reader(file, dialect="study_semicolon")
```

Other related tools include:

- `csv.get_dialect()`;
- `csv.list_dialects()`;
- `csv.unregister_dialect()`.

Register a process-wide name only when that shared name makes the contract easier to understand. Passing explicit parameters can be clearer for a one-off boundary.

## 9. Formatting parameters can override a dialect

`reader()` and `writer()` accept a dialect plus individual formatting parameters. Those parameters can override parts of the selected dialect.

For example:

```python
reader = csv.reader(
    file,
    dialect="excel",
    delimiter=";",
)
```

The result is not simply "the Excel dialect" anymore. It is the Excel dialect with a delimiter override.

When debugging an interface, inspect the complete effective policy rather than reasoning from the dialect name alone.

## 10. The delimiter is a one-character field separator

The default `excel` dialect uses a comma:

```python
reader = csv.reader(file, delimiter=",")
```

A semicolon contract can be explicit:

```python
reader = csv.reader(file, delimiter=";")
```

The `delimiter` setting is a one-character string. Multi-character separators belong to a different parsing design.

Do not guess a delimiter from regional conventions when the producer can define it explicitly.

## 11. `quotechar` protects special content

The default quote character is a double quote:

```text
name,note
Ada,"commas, stay inside this field"
```

The quotes are part of the CSV representation, not normally part of the returned field value.

With the normal `doublequote=True` policy, a quote inside a quoted field is represented by doubling it:

```text
name,note
Ada,"She said ""hello"""
```

The reader reconstructs the field content according to the dialect.

## 12. `doublequote` and `escapechar` define how quotes are escaped

When `doublequote=True`, an internal `quotechar` is doubled.

When `doublequote=False`, the configured `escapechar` is used instead.

For example:

```python
writer = csv.writer(
    file,
    doublequote=False,
    escapechar="\\",
)
```

If `doublequote=False` and no `escapechar` exists, writing a field that contains the quote character can raise `csv.Error`.

Escaping is a representation rule. It must match the consumer's expectations.

## 13. Quoting modes are parser and writer policy

Python exposes several `QUOTE_*` constants:

| Mode | Main idea |
|---|---|
| `QUOTE_MINIMAL` | Quote fields only when required by special characters |
| `QUOTE_ALL` | Quote every field |
| `QUOTE_NONNUMERIC` | Quote non-numeric output fields and convert unquoted input fields to `float` |
| `QUOTE_NONE` | Never use quoting; escaping becomes necessary for special characters |
| `QUOTE_NOTNULL` | Python 3.12+: distinguish unquoted empty fields as `None` |
| `QUOTE_STRINGS` | Python 3.12+: quote strings and use unquoted empty fields for `None` |

The mode is not merely visual formatting. Some modes also change decoding behavior.

## 14. `QUOTE_MINIMAL` and `QUOTE_ALL` express different output policies

`QUOTE_MINIMAL` is the usual default:

```python
writer = csv.writer(file, quoting=csv.QUOTE_MINIMAL)
```

Only fields requiring quotes under the dialect are quoted.

`QUOTE_ALL` quotes every field:

```python
writer = csv.writer(file, quoting=csv.QUOTE_ALL)
```

Quoting every field can make a representation more uniform, but it does not automatically solve schema validation, encoding differences, or spreadsheet-specific security concerns.

## 15. `QUOTE_NONE` requires a deliberate escape policy

With `QUOTE_NONE`, the writer never quotes fields:

```python
writer = csv.writer(
    file,
    quoting=csv.QUOTE_NONE,
    escapechar="\\",
)
```

Characters that need escaping are prefixed by the configured `escapechar`.

If no `escapechar` is configured and a field contains a character that requires escaping, the writer raises `csv.Error`.

Use `QUOTE_NONE` only when the receiving interface defines compatible escaping rules.

## 16. `QUOTE_NONNUMERIC` changes input types

By default, CSV readers return fields as strings.

`QUOTE_NONNUMERIC` is different. On reading, unquoted fields are converted to `float`:

```python
import csv
from io import StringIO

source = StringIO('"name","score"\n"Ada",91\n')
reader = csv.reader(source, quoting=csv.QUOTE_NONNUMERIC)

for row in reader:
    print(row)
```

The numeric field `91` becomes `91.0` because it was not quoted.

This is a representation-driven conversion rule, not a complete application type system. Some Python numeric-looking values, including types whose string form cannot be converted to `float`, are not suitable for round-tripping through this mode.

For many application contracts, explicit conversion after ordinary string parsing is easier to validate and explain.

## 17. Python 3.12 added `QUOTE_NOTNULL`; reader support was fixed in 3.13

`csv.QUOTE_NOTNULL` was added in Python 3.12. Its writer behavior is available there, but Python 3.12 has a documented bug: this constant does not affect `reader` objects. That reader bug is fixed in Python 3.13.

On writing in Python 3.12+, it quotes every field that is not `None`. A `None` value is written as an unquoted empty field.

Starting with Python 3.13, on reading, an unquoted empty field becomes `None`, while other fields behave like `QUOTE_ALL`.

This creates a representation-level distinction between:

```text

```

and:

```text
""
```

Starting with Python 3.13, the first can be read as `None` under this mode, while the quoted empty string remains an empty string.

Use it only when both sides of the interface agree on that meaning and document whether the contract needs writer support from Python 3.12 or nullable reader semantics from Python 3.13.

## 18. Python 3.12 added `QUOTE_STRINGS`; reader support was fixed in 3.13

`csv.QUOTE_STRINGS` was also added in Python 3.12. Its writer behavior is available there, but its special reader behavior is affected by the same Python 3.12 bug and requires Python 3.13+.

On writing in Python 3.12+, string fields are always quoted, while `None` becomes an unquoted empty field.

Starting with Python 3.13, on reading, unquoted empty fields become `None`, and the remaining behavior follows `QUOTE_NONNUMERIC`, including conversion of unquoted non-empty fields to `float`.

That conversion behavior means this mode is not simply "quote all strings." It also carries a decoding policy.

Version-specific constants should be documented in interfaces that may run on older Python versions.

## 19. The default writer conversion of `None` is lossy

The ordinary CSV writer writes `None` as an empty string:

```python
import csv
from io import StringIO

output = StringIO(newline="")
writer = csv.writer(output, lineterminator="\n")
writer.writerow(["Ada", None, ""])

print(output.getvalue())
```

Both `None` and the empty string can therefore become empty fields under the default policy.

That transformation is intentionally not reversible.

If your application must distinguish missing values from empty strings, define an explicit representation such as:

- a documented sentinel text;
- a schema-level nullable representation;
- Python 3.12+ `QUOTE_NOTNULL` or `QUOTE_STRINGS` when their semantics fit the interface;
- a different data format when CSV cannot preserve the required distinctions cleanly.

## 20. CSV fields are strings by default, not inferred application values

With ordinary `csv.reader()` behavior:

```text
91
false
2026-08-28
```

all arrive as text fields.

Your program decides whether they mean:

- an integer;
- a boolean;
- a date;
- or simply a string.

Keep the stages visible:

```text
CSV field text
   ↓ application conversion
candidate value
   ↓ validation
trusted value
```

Do not rely on a field's appearance alone to define its type.

## 21. Convert and validate after parsing

A narrow converter makes the contract testable:

```python
def parse_score(text: str) -> int:
    score = int(text)
    if not 0 <= score <= 100:
        raise ValueError("score must be between 0 and 100")
    return score
```

The CSV parser answers where one field ends and the next begins. The converter answers what a field means to the application.

Those are different responsibilities.

## 22. `DictReader` makes the header part of the interface

When `fieldnames` is omitted, `DictReader` uses the first record as dictionary keys and does not return that record as data:

```python
import csv

with open("records.csv", "r", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["name"])
```

If you provide `fieldnames` explicitly, the first row is treated as data instead.

That distinction matters when an interface has no header or when the application provides a fixed schema independently of the file.

## 23. `restkey` and `restval` reveal irregular row widths

A `DictReader` can encounter rows with more or fewer fields than the header.

If a row has extra fields, they are stored in a list under `restkey`. The default `restkey` is `None`.

If a non-blank row has too few fields, missing values are filled with `restval`. The default is `None`.

For validation, a private object sentinel can make missing fields visible without colliding with legitimate CSV text:

```python
missing = object()
reader = csv.DictReader(
    file,
    restkey="_extra_fields",
    restval=missing,
)
```

Because ordinary CSV fields are strings, this private object cannot be confused with legitimate field text. Your application can reject extra fields with `row.get(restkey)` and missing fields with an identity check such as `value is missing`.

Do not let parser recovery silently become application acceptance.

## 24. Duplicate header names need an explicit policy

A tabular contract often expects unique column names.

Before relying on dictionary access, validate the header when uniqueness matters:

```python
def require_unique_header(header: list[str]) -> None:
    if len(header) != len(set(header)):
        raise ValueError("CSV header contains duplicate names")
```

One clear approach is:

```text
read header as a normal row
   ↓ validate names, order, and uniqueness
create or continue the row-reading policy
```

A dictionary cannot preserve two independent values under the same key name. If duplicate columns are meaningful, a dictionary-oriented interface is probably the wrong abstraction.

## 25. `DictWriter` makes output column order explicit

`DictWriter` requires `fieldnames`:

```python
import csv

fieldnames = ["name", "score", "status"]

with open("records.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow(
        {"name": "Ada", "score": 91, "status": "complete"}
    )
```

The fieldnames sequence defines the output column order.

That makes the schema easier to review than relying on arbitrary dictionary construction elsewhere in the program.

## 26. `extrasaction` controls unexpected dictionary keys

By default, `DictWriter` raises `ValueError` when an input dictionary contains a key that is not listed in `fieldnames`.

You can choose:

```python
writer = csv.DictWriter(
    file,
    fieldnames=fieldnames,
    extrasaction="ignore",
)
```

but ignoring unexpected keys can silently discard data.

Prefer the default `"raise"` behavior unless dropping extra keys is a deliberate, documented export policy.

## 27. Missing `DictWriter` keys use `restval`

If an input dictionary lacks one of the configured output fields, `DictWriter` writes its `restval`. The default is an empty string.

You can make the policy explicit:

```python
writer = csv.DictWriter(
    file,
    fieldnames=fieldnames,
    restval="N/A",
)
```

A sentinel such as `N/A` is only appropriate if the receiving contract assigns it that meaning.

Do not invent placeholder text merely to make a row rectangular.

## 28. `strict=True` can make malformed CSV fail visibly

A dialect's `strict` option defaults to `False`.

When `strict=True`, malformed CSV input detected by the parser raises `csv.Error`:

```python
reader = csv.reader(file, strict=True)
```

Catch `csv.Error` where you can report or recover meaningfully:

```python
try:
    rows = list(reader)
except csv.Error as error:
    print(f"Invalid CSV: {error}")
```

Strict parsing still does not validate your header, types, required fields, or business rules.

## 29. `reader.line_num` counts source lines read, not logical records

Reader objects expose `line_num`.

Because one CSV record can span multiple physical lines, `line_num` is the number of lines read from the source, not simply the number of records returned.

This is useful for diagnostics, but label it accurately:

```text
source line context
```

is not always the same as:

```text
record number
```

## 30. `field_size_limit()` can bound individual parsed fields

The module exposes the current maximum field size accepted by the parser:

```python
import csv

current_limit = csv.field_size_limit()
print(current_limit)
```

You can set a new limit:

```python
csv.field_size_limit(1_000_000)
```

A field-size limit can be one part of an input-boundary policy, but it does not replace limits on total file size, record count, processing time, or application-specific content.

If you change the limit in a shared process, document that choice because it affects later CSV parsing in that interpreter.

## 31. `Sniffer.sniff()` is a heuristic

`csv.Sniffer` can inspect a sample and infer a dialect:

```python
import csv

sample = "name;score\nAda;91\nLin;88\n"
dialect = csv.Sniffer().sniff(sample, delimiters=",;\t")

print(dialect.delimiter)
```

This is useful when the producer cannot declare the delimiter, but inference is not certainty.

Restricting the candidate delimiters can make the heuristic align better with the formats your application actually supports.

## 32. Reset a file after sampling it

When sniffing from a file, reading a sample advances the file position:

```python
import csv

with open("records.csv", "r", encoding="utf-8", newline="") as file:
    sample = file.read(1024)
    dialect = csv.Sniffer().sniff(sample)
    file.seek(0)
    reader = csv.reader(file, dialect)
```

Without `file.seek(0)`, parsing would begin after the sample rather than at the start of the file.

Sampling is an I/O operation, so cursor position is part of the workflow.

## 33. `Sniffer.has_header()` is also a heuristic

`has_header()` examines a sample and guesses whether the first record looks like column names.

The official documentation explicitly describes this method as a rough heuristic that can produce false positives and false negatives.

Therefore:

```text
Sniffer says header
```

must not automatically mean:

```text
interface contract guarantees header
```

If the producer can specify whether a header exists, use that explicit contract instead of guessing.

## 34. `skipinitialspace=True` is not general whitespace cleanup

With `skipinitialspace=True`, spaces immediately following the delimiter are ignored:

```python
reader = csv.reader(file, skipinitialspace=True)
```

That is a dialect rule, not a general instruction to trim every field.

For example, leading or trailing spaces inside quoted content may still be meaningful data.

Avoid applying `.strip()` blindly unless your application contract explicitly defines that normalization.

## 35. `lineterminator` is primarily a writer policy

The writer uses `lineterminator` to end output records. Its default is `"\r\n"`.

You can define a controlled representation:

```python
writer = csv.writer(file, lineterminator="\n")
```

The current reader behavior is different: it recognizes `\r` or `\n` as end-of-line and ignores the dialect's `lineterminator` setting.

Do not assume a custom writer terminator becomes a symmetric reader rule.

## 36. UTF-8 BOM handling belongs to the text boundary

Some CSV producers, especially spreadsheet-oriented workflows, may emit UTF-8 text with a byte-order mark at the beginning.

If the interface explicitly allows that representation, Python's `utf-8-sig` codec can consume the BOM while decoding:

```python
with open("records.csv", "r", encoding="utf-8-sig", newline="") as file:
    reader = csv.reader(file)
```

Do not use `utf-8-sig` as a magical CSV repair switch. Decide whether BOM-bearing input is actually part of the supported text contract.

Encoding remains separate from delimiter and quoting rules.

## 37. CSV parsers do not evaluate spreadsheet formulas

The `csv` module parses text fields. It does not execute spreadsheet formulas.

Risk can appear later when exported CSV data containing untrusted text is opened by spreadsheet software. Some spreadsheet applications may interpret cell values beginning with characters such as `=`, `+`, `-`, or `@` as formulas.

That means two different questions exist:

```text
Is this field correctly escaped as CSV?
```

and:

```text
Will the downstream spreadsheet interpret this cell as executable formula content?
```

Correct CSV quoting does not universally answer the second question.

There is no one sanitization transformation that is safe for every spreadsheet application and every downstream programmatic consumer. If an export is intended for spreadsheet viewing and contains untrusted data, define and test a destination-specific mitigation policy.

## 38. Validate the tabular schema after parsing

A useful import boundary can validate several layers independently:

```text
text encoding
   ↓
CSV syntax and dialect
   ↓
header names and uniqueness
   ↓
row width
   ↓
field type conversion
   ↓
field value rules
```

For example, a score table may require:

```text
header exactly: name,score,status
name: non-empty text
score: integer 0..100
status: one of complete, review
no extra fields
no missing fields
```

CSV syntax alone cannot enforce those rules.

## 39. Common mistakes

### Mistake 1: assuming `.csv` means comma plus default Excel settings

The extension does not define every dialect and encoding rule.

### Mistake 2: omitting `newline=""` for real CSV file objects

That can break embedded newline handling and output line endings.

### Mistake 3: splitting physical lines manually

Quoted CSV fields can contain delimiters and embedded newlines.

### Mistake 4: treating `QUOTE_NONNUMERIC` as a full schema converter

It only applies a specific representation-driven float conversion rule.

### Mistake 5: forgetting that default `None` output is lossy

`None` and an empty string can serialize to the same empty field.

### Mistake 6: accepting irregular `DictReader` rows without checking `restkey` and `restval`

Parser recovery can hide malformed table shapes.

### Mistake 7: using `extrasaction="ignore"` just to silence export errors

Unexpected fields can disappear without notice.

### Mistake 8: trusting `Sniffer` as a guaranteed schema detector

Delimiter and header detection are heuristics.

### Mistake 9: using `.strip()` on every field automatically

Whitespace can be meaningful data.

### Mistake 10: assuming correct CSV quoting prevents spreadsheet formula interpretation

CSV syntax safety and spreadsheet execution behavior are separate concerns.

## 40. Practical example: explicit dialect round trip

```python
import csv
from io import StringIO


rows = [
    ["name", "note"],
    ["Ada", "comma, semicolon; and newline\ninside"],
    ["Lin", 'She said "hello"'],
]

output = StringIO(newline="")
writer = csv.writer(
    output,
    delimiter=";",
    quotechar='"',
    quoting=csv.QUOTE_MINIMAL,
    lineterminator="\n",
)
writer.writerows(rows)

text = output.getvalue()
print(text)

source = StringIO(text, newline="")
reader = csv.reader(
    source,
    delimiter=";",
    quotechar='"',
    quoting=csv.QUOTE_MINIMAL,
)
print(list(reader))
```

Executable version: [`examples/dialect_round_trip.py`](examples/dialect_round_trip.py).

## 41. Practical example: validate dictionary rows

```python
import csv
from io import StringIO


text = "name,score,status\nAda,91,complete\nLin,88,review\n"
source = StringIO(text, newline="")
missing = object()
reader = csv.DictReader(
    source,
    restkey="_extra_fields",
    restval=missing,
)

expected_fields = ["name", "score", "status"]
if reader.fieldnames != expected_fields:
    raise ValueError("unexpected CSV header")

records = []
for row in reader:
    if row.get("_extra_fields") is not None:
        raise ValueError("row contains extra fields")
    if any(value is missing for value in row.values()):
        raise ValueError("row contains missing fields")

    score = int(row["score"])
    if not 0 <= score <= 100:
        raise ValueError("score must be between 0 and 100")

    records.append(
        {
            "name": row["name"],
            "score": score,
            "status": row["status"],
        }
    )

print(records)
```

Executable version: [`examples/validate_dict_rows.py`](examples/validate_dict_rows.py).

## 42. Practical example: detect an allowed delimiter

```python
import csv
from io import StringIO


text = 'name;note\nAda;"uses, commas in text"\nLin;ready\n'
dialect = csv.Sniffer().sniff(text, delimiters=",;\t")

print(repr(dialect.delimiter))

source = StringIO(text, newline="")
reader = csv.reader(source, dialect)
print(list(reader))
```

Executable version: [`examples/sniff_delimiter.py`](examples/sniff_delimiter.py).

## 43. Practical example: escaping without quoting

```python
import csv
from io import StringIO


row = ["alpha,beta", 'quoted "text"', "line\nbreak"]

output = StringIO(newline="")
writer = csv.writer(
    output,
    delimiter=",",
    quoting=csv.QUOTE_NONE,
    escapechar="\\",
    lineterminator="\n",
)
writer.writerow(row)

text = output.getvalue()
print(repr(text))

source = StringIO(text, newline="")
reader = csv.reader(
    source,
    delimiter=",",
    quoting=csv.QUOTE_NONE,
    escapechar="\\",
)
print(next(reader))
```

Executable version: [`examples/quote_none_escape.py`](examples/quote_none_escape.py).

## 44. Exercise

Create a function called `decode_results(text)` for a controlled CSV import contract.

Requirements:

1. Parse CSV text with `StringIO` and `csv.DictReader`.
2. Require the exact header `name,score,status` in that order.
3. Reject duplicate header names.
4. Reject rows with extra fields.
5. Reject rows with missing fields.
6. Require `name` to be non-empty after the normalization policy you explicitly choose.
7. Convert `score` to `int` and require a value from 0 through 100.
8. Require `status` to be either `complete` or `review`.
9. Return a list of validated dictionaries whose `score` values are integers.

Then create `encode_results(records)` that:

1. writes the same three fields in the same order;
2. writes the header explicitly;
3. uses `lineterminator="\n"` for deterministic output;
4. rejects dictionaries containing unexpected keys instead of silently discarding them;
5. returns the generated CSV text.

Test at least these cases:

```text
valid rows
wrong header order
duplicate header
extra field
missing field
score = text
score = 101
unknown status
field containing a comma
field containing an embedded newline
```

The important part is not only parsing successful rows. Make every assumption about the table visible enough that another programmer can explain why an invalid file is rejected.

## 45. Quick reference

| Need | Tool / policy |
|---|---|
| Read CSV rows | `csv.reader()` |
| Write CSV rows | `csv.writer()` |
| Read rows by column name | `csv.DictReader()` |
| Write dictionaries in fixed column order | `csv.DictWriter()` |
| Open real CSV files safely | `newline=""` |
| Choose field separator | `delimiter=...` |
| Choose quote character | `quotechar=...` |
| Escape without ordinary quoting | `escapechar=...`, often with `QUOTE_NONE` |
| Quote only when needed | `csv.QUOTE_MINIMAL` |
| Quote every field | `csv.QUOTE_ALL` |
| Convert unquoted input fields to `float` | `csv.QUOTE_NONNUMERIC` |
| Distinguish `None` from a quoted empty string when writing (3.12+) and reading (3.13+) | `csv.QUOTE_NOTNULL` |
| Quote strings / represent `None` when writing (3.12+); use nullable reader semantics from 3.13+ | `csv.QUOTE_STRINGS` |
| Reject malformed parser input more aggressively | `strict=True` |
| Detect irregular `DictReader` row width | `restkey=...`, `restval=...` |
| Reject or ignore extra `DictWriter` keys | `extrasaction="raise"` / `"ignore"` |
| Control writer record ending | `lineterminator=...` |
| Bound parser field size | `csv.field_size_limit()` |
| Guess dialect from a sample | `csv.Sniffer().sniff()` |
| Guess whether a header exists | `csv.Sniffer().has_header()` |
| Read UTF-8 text that may start with a BOM | `encoding="utf-8-sig"` |
| Catch CSV parser errors | `csv.Error` |

## 46. Design checklist

Before publishing or consuming a CSV interface, ask:

```text
What character encoding is used?
Is a UTF-8 BOM allowed?
Which delimiter is required?
Which quote and escape rules are required?
What line ending does the producer write?
Is there a header?
Are header names unique and case-sensitive?
Is column order significant?
How are missing and extra fields handled?
How is None represented differently from an empty string?
Which fields require explicit type conversion?
What file, field, and row-count limits apply?
Is dialect detection allowed, or must the format be explicit?
Will untrusted fields later be opened in spreadsheet software?
```

If those answers are explicit, CSV becomes a testable interface instead of a collection of assumptions hidden behind a `.csv` extension.

## References

- [Python 3.14 documentation: `csv` — CSV File Reading and Writing](https://docs.python.org/3.14/library/csv.html)
- [Python 3.14 documentation: `codecs` — Codec registry and base classes](https://docs.python.org/3.14/library/codecs.html)
- [RFC 4180: Common Format and MIME Type for Comma-Separated Values (CSV) Files](https://www.rfc-editor.org/rfc/rfc4180)
- [OWASP: CSV Injection](https://owasp.org/www-community/attacks/CSV_Injection)

## Next chapter

Continue with [**Chapter 05: Engineering Logging Pipelines and Runtime Context Contracts**](../05-logging/README.md). It deepens effective levels, handler routing, propagation, configuration, contextual records, queue-based delivery, concurrency, and operational logging safety.
