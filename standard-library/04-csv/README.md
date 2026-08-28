<div align="center">

# Controlling CSV Dialects, Quoting, and Tabular Contracts

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

> **Phase 8 · Standard Library · Chapter 04**

CSV looks simple because a small file may resemble lines split by commas. Real CSV interfaces are more demanding: producers disagree about delimiters, quoting, line endings, null values, headers, encodings, and malformed rows. Python's `csv` module exists so you can model those rules explicitly instead of rebuilding a parser with `split(",")`.

This chapter revisits CSV at a deeper library level. Phase 7 introduced CSV as a file format. Here the focus is the **contract** around `csv.reader`, `csv.writer`, `DictReader`, `DictWriter`, dialects, quoting modes, malformed input, resource limits, and interoperability.

## 1. What problem does `csv` solve?

The module reads and writes **delimited tabular text** according to a dialect.

```python
import csv
from io import StringIO

text = "name,score\nAna,88\nBob,91\n"
reader = csv.reader(StringIO(text, newline=""))

for row in reader:
    print(row)
```

By default, fields are returned as strings. CSV itself does not provide a complete application schema, so parsing rows and validating business meaning are separate responsibilities.

## 2. CSV is a family of dialects, not one universal layout

"CSV" does not guarantee that every producer uses the same delimiter or quoting rules.

Common variations include:

```text
comma delimiter
semicolon delimiter
tab delimiter
quoted fields
escaped fields
different line terminators
different character encodings
```

Python groups parsing and formatting choices into a `Dialect`. Built-in dialect names include `excel`, `excel-tab`, and `unix`.

A dialect describes syntax. It does not prove that the data matches your application's required columns or value rules.

## 3. Readers parse text; writers format text

A writer receives Python values and writes delimited text through a file-like object with `write()`.

```python
import csv
from io import StringIO

stream = StringIO(newline="")
writer = csv.writer(stream, lineterminator="\n")
writer.writerow(["name", "score"])
writer.writerow(["Ana", 88])

print(stream.getvalue())
```

A reader consumes an iterable of strings. When working with real files, character decoding belongs to `open()`, while CSV syntax parsing belongs to `csv`.

That separation is similar to the JSON boundary from the previous chapter:

```text
bytes on storage/network
   ↓ text decoding
Python str
   ↓ csv parsing
rows and fields
   ↓ application validation
trusted domain values
```

## 4. Use `newline=""` for CSV file objects

When a real file is passed to `csv.reader()` or `csv.writer()`, Python's documentation recommends opening it with `newline=""`.

```python
import csv

with open("records.csv", encoding="utf-8", newline="") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
```

This lets the `csv` module perform its own newline handling. It matters especially for quoted fields containing embedded newlines and for avoiding unwanted carriage-return behavior on platforms that use `\r\n`.

`newline=""` is a file-opening policy. It is not a delimiter or record-schema setting.

## 5. `delimiter` and `quotechar` are part of the interface

If a producer uses semicolons, configure that explicitly:

```python
import csv
from io import StringIO

text = 'name;note\nAna;"uses;semicolon"\n'
reader = csv.reader(
    StringIO(text, newline=""),
    delimiter=";",
    quotechar='"',
)

print(list(reader))
```

A delimiter and quote character are single-character syntax choices. They should come from a known interface contract whenever possible.

Do not guess a delimiter only because a sample happens to contain a certain punctuation mark.

## 6. `QUOTE_MINIMAL` quotes only when CSV syntax needs it

`csv.QUOTE_MINIMAL` is the usual default when a quote character exists.

```python
import csv
from io import StringIO

stream = StringIO(newline="")
writer = csv.writer(
    stream,
    delimiter=";",
    quoting=csv.QUOTE_MINIMAL,
    lineterminator="\n",
)
writer.writerow(["Ana", "uses;semicolon"])

print(stream.getvalue())
```

Here the second field contains the delimiter, so the writer quotes it.

Other important policies are:

- `QUOTE_ALL`: quote every field;
- `QUOTE_MINIMAL`: quote fields only when required by the dialect;
- `QUOTE_NONNUMERIC`: writer quotes non-numeric fields, reader converts unquoted fields to `float`;
- `QUOTE_NONE`: never treat quote characters specially;
- `QUOTE_NOTNULL`: quote every non-`None` field and preserve an unquoted empty field as `None` when reading;
- `QUOTE_STRINGS`: quote string fields while giving unquoted numeric fields `QUOTE_NONNUMERIC`-style conversion and unquoted empty fields `None` semantics.

`QUOTE_NOTNULL` and `QUOTE_STRINGS` were added in Python 3.12 and are available in Python 3.14.

## 7. `QUOTE_NONNUMERIC` changes types during reading

Most CSV reading returns strings. `QUOTE_NONNUMERIC` is an important exception.

```python
import csv
from io import StringIO

text = '3,19.90,"ready"\n'
reader = csv.reader(
    StringIO(text, newline=""),
    quoting=csv.QUOTE_NONNUMERIC,
)

row = next(reader)
print(row)
print([type(value).__name__ for value in row])
```

Unquoted fields are converted to `float`; quoted fields remain strings.

This mode is not a general schema system. Some values produced from Python numeric-looking types, such as `bool`, `Fraction`, or `IntEnum`, can have string forms that cannot be converted back to `float`.

Use explicit application validation when exact types matter.

## 8. `QUOTE_NOTNULL` can distinguish `None` from an empty string

The ordinary writer serializes `None` as an empty string, which is not reversible by itself.

Python 3.12+ provides `QUOTE_NOTNULL`:

```python
import csv
from io import StringIO

stream = StringIO(newline="")
writer = csv.writer(
    stream,
    quoting=csv.QUOTE_NOTNULL,
    lineterminator="\n",
)
writer.writerow(["name", "note"])
writer.writerow(["Ana", None])
writer.writerow(["Bob", ""])

text = stream.getvalue()
print(text, end="")

reader = csv.reader(
    StringIO(text, newline=""),
    quoting=csv.QUOTE_NOTNULL,
)
print(list(reader))
```

With this policy:

- `None` becomes an empty **unquoted** field;
- an empty string is still a non-`None` value and is quoted;
- the matching reader interprets an empty unquoted field as `None`.

This is useful only when both ends agree on that dialect policy.

## 9. `QUOTE_STRINGS` is useful only when its conversion contract fits

`QUOTE_STRINGS` quotes string fields, writes `None` as an unquoted empty field, and makes the reader interpret unquoted non-empty fields like `QUOTE_NONNUMERIC`.

That means unquoted values are candidates for `float` conversion. It is not equivalent to "preserve arbitrary Python types."

If the interface has columns such as IDs, booleans, decimals, dates, or enums, a column-by-column schema is usually clearer than relying on quoting mode to infer types.

## 10. `QUOTE_NONE` usually requires an escape strategy

If quoting is disabled, delimiters and other special characters still need representation.

```python
import csv
from io import StringIO

stream = StringIO(newline="")
writer = csv.writer(
    stream,
    quoting=csv.QUOTE_NONE,
    escapechar="\\",
    lineterminator="\n",
)
writer.writerow(["Ana", "A,B"])

print(stream.getvalue())
```

Without a usable `escapechar`, the writer can raise `csv.Error` when it encounters characters that require escaping.

`doublequote`, `quotechar`, `escapechar`, and `quoting` work together. Changing one setting can alter what the others must do.

## 11. The writer's `lineterminator` is explicit

A dialect also controls the writer's line terminator. The `excel` dialect defaults to `\r\n`.

For deterministic generated text, you can set:

```python
writer = csv.writer(file, lineterminator="\n")
```

The reader is currently hard-coded to recognize `\r` or `\n` as end-of-line and does not use the dialect's `lineterminator` as a matching rule. Do not teach `lineterminator` as a symmetric reader/writer contract.

## 12. `DictReader` maps a header to dictionaries

When the first row is a header, `DictReader` can provide name-based access:

```python
import csv
from io import StringIO

text = "name,score\nAna,88\nBob,91\n"
reader = csv.DictReader(StringIO(text, newline=""))

for row in reader:
    print(row["name"], row["score"])
```

If `fieldnames` is omitted, the first row becomes the field-name sequence and is not returned as data.

The resulting mapping preserves field-name order, but the values are still CSV-decoded field values, usually strings.

## 13. Extra and missing fields need an explicit policy

A row may contain more or fewer fields than the header.

```python
import csv
from io import StringIO

text = "name,score\nAna,88,extra\nBob\n"
reader = csv.DictReader(
    StringIO(text, newline=""),
    restkey="_extra",
    restval="_missing",
)

for row in reader:
    print(row)
```

For `DictReader`:

- extra fields are stored under `restkey` as a list;
- missing fields receive `restval`;
- both default to `None` if you do not choose something else.

Using defaults can make malformed row widths less obvious. For strict application contracts, check for extra and missing values deliberately.

## 14. `DictWriter` has its own schema boundary

`DictWriter` requires an explicit `fieldnames` sequence.

```python
import csv
from io import StringIO

stream = StringIO(newline="")
writer = csv.DictWriter(
    stream,
    fieldnames=["name", "score"],
    extrasaction="raise",
    lineterminator="\n",
)
writer.writeheader()
writer.writerow({"name": "Ana", "score": 88})

print(stream.getvalue())
```

If an input dictionary contains an unknown key:

- `extrasaction="raise"` raises `ValueError` and is the default;
- `extrasaction="ignore"` silently excludes the extra key.

Missing expected keys are written using `restval`, whose default is an empty string.

Choose these policies intentionally. Silent omission can be convenient, but it can also hide a producer bug.

## 15. A CSV header is not the same as validated schema

Checking the exact header is often a useful first contract:

```python
import csv
from io import StringIO

EXPECTED = ["name", "score"]

text = "name,score\nAna,88\n"
reader = csv.DictReader(StringIO(text, newline=""))

if reader.fieldnames != EXPECTED:
    raise ValueError("unexpected CSV header")

rows = list(reader)
print(rows)
```

Applications may additionally need to validate:

```text
exact column count
required columns
column order
non-empty identifiers
integer ranges
date formats
decimal rules
allowed status values
duplicate identifiers
cross-row relationships
```

The `csv` module handles syntax. Your application owns semantic validation.

## 16. Whitespace handling is not automatic cleanup

`skipinitialspace=True` ignores spaces immediately after delimiters.

It does not mean "strip every field." For example, trailing spaces remain data unless your application removes them.

Also, combining `delimiter=" "` with `skipinitialspace=True` disallows unquoted empty fields. Treat whitespace rules as part of the dialect rather than generic cleanup.

## 17. `strict=True` asks the parser to reject bad CSV input

The default dialect is relatively permissive. For interfaces that should reject malformed CSV syntax, set `strict=True`.

```python
import csv
from io import StringIO

text = 'name,score\n"Ana,88\n'

try:
    list(csv.reader(StringIO(text, newline=""), strict=True))
except csv.Error:
    print("Malformed CSV rejected")
```

`strict=True` concerns CSV syntax. A syntactically valid row can still violate your application's schema.

## 18. `csv.Error` is the module's parsing/formatting exception

When CSV processing detects an error, it can raise `csv.Error`.

A reader also exposes `line_num`:

```python
import csv
from io import StringIO

text = 'name,score\n"Ana,88\n'
reader = csv.reader(StringIO(text, newline=""), strict=True)

try:
    for row in reader:
        print(row)
except csv.Error:
    print(f"CSV error near physical line {reader.line_num}")
```

`line_num` counts physical lines read from the source. It is not necessarily the same as the number of records returned because a quoted record can span multiple physical lines.

## 19. `Sniffer` is a heuristic, not validation

`csv.Sniffer().sniff()` can estimate a dialect from sample text.

```python
import csv

sample = "name;score\nAna;88\nBob;91\n"
dialect = csv.Sniffer().sniff(sample, delimiters=",;\t")

print(dialect.delimiter)
```

`Sniffer.has_header()` can also estimate whether a first row looks like a header.

Both are heuristics. `has_header()` can return false positives or false negatives, and `sniff()` can choose among plausible delimiters based on its preferences.

Use sniffing for discovery when you truly do not control the format, then validate the result against allowed interface policies before trusting it.

## 20. Registered dialects can centralize repeated syntax

If several files share the same syntax, register a named dialect:

```python
import csv
from io import StringIO

csv.register_dialect(
    "study_semicolon",
    delimiter=";",
    quoting=csv.QUOTE_MINIMAL,
)

reader = csv.reader(
    StringIO("name;score\nAna;88\n", newline=""),
    dialect="study_semicolon",
)
print(list(reader))

csv.unregister_dialect("study_semicolon")
```

`get_dialect()` returns an immutable dialect object, and `list_dialects()` shows registered names.

Global dialect registration affects the process-wide registry. In libraries, explicit local formatting parameters or carefully namespaced dialect names may be easier to reason about.

## 21. Limit field size for untrusted or constrained input

`csv.field_size_limit()` returns the parser's current maximum field size. Passing an argument changes that process-wide limit.

```python
import csv
from io import StringIO

previous_limit = csv.field_size_limit()

try:
    csv.field_size_limit(8)
    try:
        list(csv.reader(StringIO("value\n123456789\n", newline="")))
    except csv.Error:
        print("Field limit enforced")
finally:
    csv.field_size_limit(previous_limit)
```

A field-size limit is one resource boundary, not a full security solution. A document can still contain many rows, and downstream validation can still consume time or memory.

Because the limit is process-wide, restore it when making a temporary change inside reusable code.

## 22. Encoding belongs to the text-file boundary

The `csv` module works with strings. `open()` decides how bytes become text.

For ordinary UTF-8 CSV:

```python
with open("records.csv", encoding="utf-8", newline="") as file:
    reader = csv.reader(file)
```

Some spreadsheet-produced UTF-8 files begin with a BOM. When that is part of the external contract, `encoding="utf-8-sig"` can consume it:

```python
import csv

with open(
    "records.csv",
    encoding="utf-8-sig",
    newline="",
) as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
```

Do not choose `utf-8-sig` automatically for every CSV. Encoding is an interface decision.

## 23. The default writer's `None` conversion loses information

For ordinary `csv.writer`, `None` is written as an empty string. This makes database exports convenient, but the transformation is not reversible by default.

If `None` and `""` mean different things in your application, choose a representation policy such as:

```text
an agreed sentinel
a separate presence column
QUOTE_NOTNULL on Python 3.12+
another format with explicit null semantics
```

The right choice depends on interoperability requirements.

## 24. CSV quoting does not define spreadsheet execution policy

CSV quoting protects CSV syntax. It does not automatically make a value harmless when another program interprets the cell after opening the file.

If user-controlled data will be opened by spreadsheet software, formulas and other consumer-specific interpretations need a separate output-safety policy.

Treat this as another boundary:

```text
valid CSV syntax
        ≠
safe behavior in every CSV consumer
```

## 25. Stream large files instead of building unnecessary lists

Readers are iterators. You can process records one at a time:

```python
import csv

with open("records.csv", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        process_name = row["name"].strip()
        print(process_name)
```

This can keep memory use much lower than `list(reader)` for large files.

Streaming does not remove the need for limits. You may still need policies for file size, row count, field length, and processing time.

## 26. `writerows()` accepts an iterable of rows

A writer can consume a generator:

```python
import csv
from io import StringIO

rows = (
    [name, score]
    for name, score in [("Ana", 88), ("Bob", 91)]
)

stream = StringIO(newline="")
writer = csv.writer(stream, lineterminator="\n")
writer.writerows(rows)

print(stream.getvalue())
```

This is useful for pipelines that transform records lazily.

Remember that the writer still stringifies non-string field values according to the module's rules. Streaming affects memory behavior, not schema meaning.

## 27. A CSV round trip does not preserve arbitrary Python types

With the ordinary reader/writer pair:

```text
Python int 88
   ↓ writer
CSV field 88
   ↓ reader
Python str "88"
```

`QUOTE_NONNUMERIC`, `QUOTE_NOTNULL`, and `QUOTE_STRINGS` change specific parts of this behavior, but none of them turns CSV into a general Python object serialization format.

If exact type reconstruction matters, define it column by column.

## 28. When CSV is a good fit

CSV is useful when:

- data is naturally tabular;
- rows share a stable column contract;
- humans or spreadsheet tools need to inspect the data;
- interoperability with systems that already exchange delimited text matters;
- streaming row-by-row processing is valuable.

## 29. When CSV is a poor fit

Consider another format when:

- data is deeply nested;
- null versus empty string must be unambiguous without a custom dialect;
- rich types must round-trip directly;
- per-record schemas vary significantly;
- binary data is a first-class field;
- you need a strongly standardized envelope or metadata model.

## 30. Common mistakes

### Mistake 1: using `split(",")`

```python
line = 'Ana,"A,B"'
print(line.split(","))
```

This ignores quoting rules. Use `csv.reader()`.

### Mistake 2: omitting `newline=""` on real CSV files

Let the `csv` module handle CSV newlines.

### Mistake 3: assuming every `.csv` file uses commas

Confirm or configure the dialect.

### Mistake 4: treating a header as schema validation

Validate row width and value semantics separately.

### Mistake 5: expecting numeric types to round-trip automatically

The default reader returns strings.

### Mistake 6: trusting `Sniffer` as proof

It is a heuristic.

### Mistake 7: silently ignoring extra dictionary keys

Use `extrasaction="raise"` unless omission is intentional.

### Mistake 8: assuming quoted output is safe in every spreadsheet

CSV syntax and spreadsheet execution behavior are different boundaries.

## 31. Practical example: semicolon dialect round trip

```python
import csv
from io import StringIO

stream = StringIO(newline="")
writer = csv.writer(
    stream,
    delimiter=";",
    quoting=csv.QUOTE_MINIMAL,
    lineterminator="\n",
)
writer.writerow(["name", "note"])
writer.writerow(["Ana", "uses;semicolon"])
writer.writerow(["Bob", 'says "hello"'])

text = stream.getvalue()
print(text, end="")

reader = csv.reader(
    StringIO(text, newline=""),
    delimiter=";",
)
print(list(reader))
```

Executable version: [`examples/semicolon_dialect.py`](examples/semicolon_dialect.py).

## 32. Practical example: validate a dictionary-row contract

```python
import csv
from io import StringIO

EXPECTED_FIELDS = ["name", "score"]

text = "name,score\nAna,88\nBob,91\n"
reader = csv.DictReader(StringIO(text, newline=""))

if reader.fieldnames != EXPECTED_FIELDS:
    raise ValueError("unexpected header")

for row in reader:
    if None in row:
        raise ValueError("row has extra fields")
    if any(value is None for value in row.values()):
        raise ValueError("row has missing fields")
    print(row)
```

Executable version: [`examples/dict_contract.py`](examples/dict_contract.py).

## 33. Practical example: preserve `None` versus empty string

```python
import csv
from io import StringIO

stream = StringIO(newline="")
writer = csv.writer(
    stream,
    quoting=csv.QUOTE_NOTNULL,
    lineterminator="\n",
)
writer.writerow(["name", "note"])
writer.writerow(["Ana", None])
writer.writerow(["Bob", ""])

text = stream.getvalue()
print(text, end="")

reader = csv.reader(
    StringIO(text, newline=""),
    quoting=csv.QUOTE_NOTNULL,
)
print(list(reader))
```

Executable version: [`examples/quote_notnull.py`](examples/quote_notnull.py).

## 34. Practical example: reject malformed CSV syntax

```python
import csv
from io import StringIO

text = 'name,score\n"Ana,88\n'

try:
    list(csv.reader(StringIO(text, newline=""), strict=True))
except csv.Error:
    print("Malformed CSV rejected")
```

Executable version: [`examples/strict_csv.py`](examples/strict_csv.py).

## 35. Exercise

Create `decode_inventory_csv(text)` for this contract:

```text
header: item,quantity,active
delimiter: comma
quoting: normal CSV quoting
top-level concept: one row per inventory item
```

Requirements:

1. parse with `csv.DictReader`;
2. require the exact header order `item`, `quantity`, `active`;
3. reject rows with extra or missing fields;
4. require `item` to be a non-empty string after trimming surrounding whitespace;
5. convert `quantity` with `int()` and require it to be zero or greater;
6. accept only `true` or `false` for `active`, case-insensitively;
7. return validated dictionaries whose `quantity` is `int` and `active` is `bool`;
8. reject malformed CSV syntax with a clear application-level error.

Then create `encode_inventory_csv(rows)` that writes the same field order with:

```text
newline-aware CSV writing
explicit lineterminator
extrasaction="raise"
```

Test valid data plus:

```text
wrong header
extra field
missing field
invalid integer
negative quantity
invalid boolean
quoted comma inside item
```

The goal is to make the boundary explainable, not merely to make the happy path work.

## 36. Quick reference

| Need | Tool / policy |
|---|---|
| Read rows | `csv.reader(...)` |
| Write rows | `csv.writer(...)` |
| Read header-mapped rows | `csv.DictReader(...)` |
| Write dictionaries | `csv.DictWriter(...)` |
| Open real CSV files | `newline=""` |
| Choose delimiter | `delimiter=";"` or another one-character value |
| Choose quote character | `quotechar='"'` |
| Minimal quoting | `csv.QUOTE_MINIMAL` |
| Quote all fields | `csv.QUOTE_ALL` |
| Convert unquoted fields to `float` while reading | `csv.QUOTE_NONNUMERIC` |
| Preserve unquoted empty field as `None` | `csv.QUOTE_NOTNULL` |
| Quote strings with numeric conversion for unquoted values | `csv.QUOTE_STRINGS` |
| Disable quote processing | `csv.QUOTE_NONE` |
| Escape special characters | `escapechar=...` |
| Explicit writer line ending | `lineterminator="\n"` |
| Reject malformed CSV syntax | `strict=True` |
| CSV parser/formatter error | `csv.Error` |
| Inspect physical line progress | `reader.line_num` |
| Estimate dialect | `csv.Sniffer().sniff(...)` |
| Estimate header presence | `csv.Sniffer().has_header(...)` |
| Register reusable dialect | `csv.register_dialect(...)` |
| Limit parser field size | `csv.field_size_limit(...)` |
| Reject unknown DictWriter keys | `extrasaction="raise"` |

## 37. Design checklist

Before publishing or consuming a CSV interface, ask:

```text
What delimiter is required?
What quote and escape rules are required?
What line ending will writers produce?
What character encoding carries the text?
Is there a header, and is its order significant?
How are extra or missing fields handled?
How are null and empty string distinguished?
Which columns require type conversion?
How are malformed rows reported?
What size limits apply?
Is dialect sniffing allowed or must the format be explicit?
Will spreadsheet software interpret exported cell contents?
```

If those answers are explicit, CSV stops being "just comma-separated text" and becomes a testable interface contract.

## References

- [Python 3.14 documentation: `csv` — CSV File Reading and Writing](https://docs.python.org/3.14/library/csv.html)
- [PEP 305: CSV File API](https://peps.python.org/pep-0305/)
- [RFC 4180: Common Format and MIME Type for CSV Files](https://www.rfc-editor.org/rfc/rfc4180)

## Next chapter

Continue with **Chapter 05: `logging`** when it becomes available. It will deepen logger hierarchies, handlers, formatters, levels, configuration, and application-versus-library logging.

[← Previous: Chapter 03 · `json`](../03-json/README.md)
