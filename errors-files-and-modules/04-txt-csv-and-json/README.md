<div align="center">

# Working with TXT, CSV, and JSON

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Back to Errors, Files, and Modules](../README.md) · [← Previous: Opening Files Safely with `open()` and `with`](../03-open-and-with/README.md)

Opening a file safely is only half of the job. A program also needs to understand **how the data inside that file is organized**.

A `.txt` file may contain one record per line, a CSV file may represent rows and columns, and a JSON document may represent nested objects and arrays. The file extension is a useful clue, but the real contract is the data format and the rules used to parse it.

This chapter introduces plain text records, Python's `csv` module, and Python's `json` module. The goal is not to memorize every option. The goal is to choose a format deliberately, use the parser responsible for that format, and keep parsing separate from validation and business logic.

**Estimated study time:** 120–160 minutes.

**Python requirement:** Python 3.10 or newer. The `csv` and `json` behavior taught here was checked against the official Python 3.14 documentation.

## Learning objectives

By the end of this chapter, you should be able to:

- explain the difference between a file extension and a data format;
- use plain text when a simple line-oriented contract is enough;
- explain why CSV should not be parsed with a naive `split(",")`;
- read and write CSV rows with the standard-library `csv` module;
- use `DictReader` and `DictWriter` when named columns improve clarity;
- explain why CSV values normally arrive as strings and convert them deliberately;
- open CSV files with `newline=""` and a known text encoding;
- distinguish JSON objects, arrays, strings, numbers, booleans, and `null`;
- use `json.load()`, `json.loads()`, `json.dump()`, and `json.dumps()` correctly;
- handle invalid JSON with `json.JSONDecodeError` where recovery is meaningful;
- distinguish parsing from validation;
- choose TXT, CSV, or JSON according to the shape and contract of the data;
- avoid hand-built parsers when a format-specific parser already exists.

## 1. A file is a container; a format is a contract

Chapter 03 focused on opening, reading, writing, and closing files. This chapter adds another question:

```text
bytes on storage
      ↓ decoding
text in Python
      ↓ parsing
structured Python values
      ↓ validation
values your program trusts
```

Opening a file answers **where the data comes from**. Parsing answers **what the text means**.

These are related responsibilities, but they are not the same responsibility.

## 2. The extension does not magically parse the contents

A filename such as `topics.txt`, `scores.csv`, or `profile.json` communicates intent to humans and tools. Python does not automatically inspect the extension and turn the contents into the corresponding structure.

You choose the appropriate operation:

```python
with open("topics.txt", "r", encoding="utf-8") as file:
    text = file.read()
```

or a format-specific parser such as `csv.reader()` or `json.load()`.

## 3. TXT means text, not one universal schema

`.txt` usually means plain text, but there is no single universal TXT record format.

All of these could be valid text-file contracts:

```text
Functions
Exceptions
Files
```

```text
topic=Functions
level=2
active=true
```

```text
2026-08-26 | Files | completed
```

The program and the producer of the file must agree on the rules.

## 4. A simple TXT contract can be one record per line

If every line is one independent text value, the format can remain intentionally simple:

```python
with open("topics.txt", "r", encoding="utf-8") as file:
    topics = [line.rstrip("\n") for line in file]
```

Here the parser is small because the contract is small: each physical line represents one topic.

## 5. Preserve meaningful whitespace deliberately

Avoid using `strip()` automatically when spaces might belong to the data.

```python
clean_line = line.rstrip("\n")
```

This removes only the newline character named by the format decision above.

If your format defines other normalization rules, apply those rules explicitly rather than treating all whitespace as disposable.

## 6. Simple custom separators are still a format you must define

Suppose a controlled text file contains one key-value pair per line:

```text
topic=Files
level=2
```

A deliberate parser might split only at the first separator:

```python
key, value = line.rstrip("\n").split("=", 1)
```

The `1` matters if the value itself may contain `=` later.

Once escaping, quoting, optional columns, nested data, or many edge cases appear, a standard format is usually a better choice than growing a private mini-language.

## 7. CSV represents tabular records

CSV is useful when the data naturally looks like rows with the same columns:

```text
topic,score,status
Functions,91,complete
Files,88,complete
JSON,79,review
```

The name means comma-separated values, but real CSV data can use different delimiters and quoting rules. Python models those choices through CSV dialect and formatting options.

## 8. Do not parse CSV with `split(",")`

This looks tempting:

```python
columns = line.split(",")
```

but a valid field may itself contain a comma when quoted:

```text
topic,note
Files,"Read, write, and validate"
```

A CSV parser understands delimiters, quotes, embedded newlines, and other format rules. A naive string split does not.

## 9. Import the standard-library `csv` module

The module is part of Python's standard library:

```python
import csv
```

It provides row-oriented APIs such as:

- `csv.reader()`;
- `csv.writer()`;
- `csv.DictReader()`;
- `csv.DictWriter()`.

This chapter teaches the practical core. A later Standard Library phase can revisit broader module options and customization.

## 10. Open CSV files with `newline=""`

When a file object is passed to the `csv` module, the official documentation recommends opening it with `newline=""` so the CSV module can perform its own newline handling correctly.

```python
with open("scores.csv", "r", encoding="utf-8", newline="") as file:
    reader = csv.reader(file)
```

Keep `encoding="utf-8"` explicit when UTF-8 is the data contract.

## 11. `csv.reader()` returns rows as lists

A basic reader treats each record as a sequence of fields:

```python
import csv

with open("scores.csv", "r", encoding="utf-8", newline="") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
```

With the earlier sample, rows are lists such as:

```text
['topic', 'score', 'status']
['Functions', '91', 'complete']
```

Notice that `91` is a string.

## 12. CSV does not normally infer your application types

By default, `csv.reader()` returns fields as strings. `DictReader` also gives string values for ordinary fields.

Your program must decide which conversions are part of its contract:

```python
score = int(row[1])
```

Conversion can fail, so this is also a validation boundary.

## 13. `csv.writer()` formats rows for you

Do not build CSV records manually by joining values with commas.

```python
import csv

rows = [
    ["topic", "score"],
    ["Functions", 91],
    ["Files", 88],
]

with open("scores.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(rows)
```

The writer applies the configured CSV quoting and delimiter rules.

## 14. `DictReader` gives columns names

When the first row is a header, `DictReader` can make code easier to read:

```python
import csv

with open("scores.csv", "r", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["topic"], row["score"])
```

The header values become dictionary keys.

## 15. Header names are part of the CSV contract

Code that expects `row["score"]` depends on a column named exactly `score`.

If a producer changes the header to `final_score`, your parser may raise `KeyError` or your validation may reject the record.

Treat column names, order requirements, delimiter choices, and required fields as explicit interface decisions.

## 16. `DictWriter` makes output columns explicit

`DictWriter` requires `fieldnames`, which define the output column order:

```python
import csv

fieldnames = ["topic", "score", "status"]

with open("scores.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow(
        {"topic": "Files", "score": 88, "status": "complete"}
    )
```

This is often clearer than positional indexes when the table has named columns.

## 17. Delimiters vary

Comma is the default delimiter for the usual Excel-style dialect, but some data contracts use semicolons, tabs, or other delimiters.

```python
reader = csv.reader(file, delimiter=";")
```

Do not guess from regional habits or from one sample row. Know or document the contract whenever possible.

## 18. Quoting protects fields containing special characters

The CSV writer can quote fields that contain delimiters, quote characters, or line terminators.

```python
import csv

row = ["Files", "Read, write, and validate"]
```

With normal quoting rules, the comma inside the note can remain part of one field.

This is another reason to let `csv` generate the serialized text.

## 19. CSV parsing and CSV validation are different steps

A row can be syntactically valid CSV and still violate your application's rules:

```text
topic,score
Files,one hundred
```

The CSV parser can correctly return `"one hundred"`. Your application then decides whether `score` must be an integer.

```text
CSV text
   ↓ parser
row fields
   ↓ conversion + validation
trusted record
```

## 20. JSON represents structured values

JSON is useful for nested objects and arrays rather than only flat tables.

```json
{
  "topic": "Files",
  "score": 88,
  "tags": ["io", "formats"],
  "complete": true
}
```

JSON is a data interchange format. It resembles some Python literals, but it is not Python source code.

## 21. Core JSON values map to familiar Python values

A useful beginner mapping is:

| JSON | Typical Python value |
|---|---|
| object | `dict` |
| array | `list` |
| string | `str` |
| number | `int` or `float` |
| `true` / `false` | `True` / `False` |
| `null` | `None` |

This mapping is close enough to feel familiar, but the syntaxes are not interchangeable.

## 22. JSON syntax is not Python literal syntax

These JSON tokens are lowercase:

```json
{"active": true, "result": null}
```

Python uses:

```python
data = {"active": True, "result": None}
```

Do not parse JSON with `eval()`.

## 23. `json.loads()` parses a JSON string

The `s` in `loads` is a useful memory aid for working with a string value:

```python
import json

text = '{"topic": "Files", "score": 88}'
data = json.loads(text)

print(data["topic"])
```

`loads()` returns Python values created from the JSON document.

## 24. `json.dumps()` creates a JSON string

`dumps()` serializes a Python-compatible value into a JSON-formatted string:

```python
import json

data = {"topic": "Files", "score": 88}
text = json.dumps(data)

print(text)
```

Serialization means converting an in-memory value into a representation suitable for storage or transport.

## 25. `json.load()` reads JSON from a file-like object

When the JSON document is already in a text file, use `load()` with the open file:

```python
import json

with open("profile.json", "r", encoding="utf-8") as file:
    data = json.load(file)
```

`open()` manages access to the file. `json.load()` parses the text into Python values.

## 26. `json.dump()` writes one JSON value to a file-like object

```python
import json

data = {"topic": "Files", "complete": True}

with open("profile.json", "w", encoding="utf-8") as file:
    json.dump(data, file)
```

`json.dump()` writes strings to the target file-like object. In ordinary file use, open that target in text mode.

## 27. `ensure_ascii=False` keeps non-ASCII text readable

By default, the JSON encoder escapes non-ASCII characters. When a UTF-8 file is your explicit contract, `ensure_ascii=False` can keep characters readable in the serialized document:

```python
import json

data = {"language": "Português"}

with open("profile.json", "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False)
```

The choice affects representation, not the Python string value after correct decoding.

## 28. `indent` improves human readability

Pretty-printed JSON is useful for configuration, examples, and files people inspect manually:

```python
json.dump(data, file, ensure_ascii=False, indent=2)
```

Indentation increases file size, so compact output can be better for some machine-focused interfaces. Choose according to the contract, not aesthetics alone.

## 29. Invalid JSON raises `JSONDecodeError`

Syntax errors in a JSON document are reported with `json.JSONDecodeError`, a subclass of `ValueError`:

```python
import json

text = '{"topic": "Files",}'

try:
    data = json.loads(text)
except json.JSONDecodeError:
    print("Invalid JSON")
```

Catch it only where the program has a useful recovery or reporting policy.


Python's decoder also has a deliberate interoperability extension: by default, `json.loads()` accepts `NaN`, `Infinity`, and `-Infinity` and converts them to floating-point values, even though those tokens are not valid JSON according to the interoperable JSON specification. Therefore, a successful `json.loads()` call is **not** by itself proof that the input is standards-compliant JSON.

When strict standards compliance is part of the contract, provide `parse_constant` with a callback that rejects those values explicitly:

```python
import json


def reject_nonstandard_constant(value: str):
    raise ValueError(f"non-standard JSON constant: {value}")


text = '{"value": NaN}'

try:
    data = json.loads(text, parse_constant=reject_nonstandard_constant)
except ValueError as error:
    print(error)
```

Here the `ValueError` is raised deliberately by the callback. `JSONDecodeError` still represents ordinary JSON syntax errors such as the trailing comma in the earlier example.


The encoder has the matching interoperability concern in the other direction. By default, `json.dumps()` and `json.dump()` use `allow_nan=True`, so Python can serialize non-finite floating-point values as `NaN`, `Infinity`, and `-Infinity`. Those tokens are outside standards-compliant JSON and may be rejected by strict consumers.

When strict JSON output is part of the contract, set `allow_nan=False`:

```python
import json

data = {"value": float("nan")}

try:
    text = json.dumps(data, allow_nan=False)
except ValueError as error:
    print(error)
```

With `allow_nan=False`, Python raises `ValueError` instead of emitting a non-standard JSON constant. The same option is available with `json.dump()`.

## 30. Not every Python object is JSON serializable by default

The default encoder handles common JSON-compatible structures, but arbitrary objects are not automatically converted.

```python
import json

values = {1, 2, 3}
json.dumps(values)
```

A `set` is not a JSON type, so this raises `TypeError` unless you deliberately transform or customize the value.

For beginner code, explicit transformation is usually clearer than a custom encoder.

## 31. A JSON round trip may change some Python-specific structure

JSON arrays map back to lists. That means a tuple serialized as an array does not return as a tuple automatically:

```python
import json

original = ("Files", "JSON")
restored = json.loads(json.dumps(original))

print(type(restored).__name__)
```

Output:

```text
list
```

JSON represents JSON types, not every distinction in Python's object model.

## 32. JSON object keys are strings in the data model

Python's encoder accepts some non-string basic dictionary keys and converts them for JSON, but JSON object member names are strings.

Therefore, a dictionary with non-string keys may not compare equal after a dump/load round trip.

If key type matters to your application, design that representation explicitly.

## 33. Do not append independent JSON documents with repeated `dump()` calls

JSON is not a framed protocol. Writing two top-level JSON values back-to-back does not automatically create one valid JSON document:

```python
json.dump(first, file)
json.dump(second, file)
```

If you need multiple records, choose a defined container such as one JSON array, or a different explicitly specified format.

## 34. Parsing is not validation

A parser answers whether the text follows the syntax of the format and reconstructs values.

Validation answers whether those values satisfy your program's rules.

```python
import json

data = json.loads('{"score": -50}')

if not 0 <= data["score"] <= 100:
    raise ValueError("score must be between 0 and 100")
```

The JSON is syntactically valid. The application value is invalid.

## 35. Separate I/O, parsing, and validation when the program grows

Small programs can keep these steps close together, but clear functions help as complexity grows:

```text
read bytes/text
     ↓
parse format
     ↓
validate values
     ↓
transform/use data
```

This separation makes it easier to identify whether a failure came from file access, format syntax, type conversion, or a business rule.

## 36. Practical example: one TXT record per line

The executable example uses a temporary directory only to keep repository tests clean:

```python
import os
import tempfile


with tempfile.TemporaryDirectory() as directory:
    path = os.path.join(directory, "topics.txt")

    with open(path, "w", encoding="utf-8") as file:
        file.write("Functions\n")
        file.write("Files\n")
        file.write("JSON\n")

    with open(path, "r", encoding="utf-8") as file:
        topics = [line.rstrip("\n") for line in file]

    print(topics)
```

Output:

```text
['Functions', 'Files', 'JSON']
```

Executable version: [`examples/text_records.py`](examples/text_records.py).

## 37. Practical example: CSV dictionaries and explicit conversion

```python
import csv
import os
import tempfile


records = [
    {"topic": "Functions", "score": 91, "note": "Clear flow"},
    {"topic": "Files", "score": 88, "note": "Read, write, validate"},
]

with tempfile.TemporaryDirectory() as directory:
    path = os.path.join(directory, "scores.csv")
    fieldnames = ["topic", "score", "note"]

    with open(path, "w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(records)

    with open(path, "r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            score = int(row["score"])
            print(f'{row["topic"]}: {score} - {row["note"]}')
```

Output:

```text
Functions: 91 - Clear flow
Files: 88 - Read, write, validate
```

Executable version: [`examples/csv_records.py`](examples/csv_records.py).

## 38. Practical example: write and read a JSON document

```python
import json
import os
import tempfile


profile = {
    "topic": "Files",
    "score": 88,
    "tags": ["io", "formats"],
    "complete": True,
}

with tempfile.TemporaryDirectory() as directory:
    path = os.path.join(directory, "profile.json")

    with open(path, "w", encoding="utf-8") as file:
        json.dump(profile, file, ensure_ascii=False, indent=2)

    with open(path, "r", encoding="utf-8") as file:
        restored = json.load(file)

    print(restored["topic"])
    print(restored["tags"])
    print(restored["complete"])
```

Output:

```text
Files
['io', 'formats']
True
```

Executable version: [`examples/json_document.py`](examples/json_document.py).

## 39. Practical example: handle invalid JSON deliberately

```python
import json


text = '{"topic": "Files",}'

try:
    data = json.loads(text)
except json.JSONDecodeError:
    print("Invalid JSON")
else:
    print(data)
```

Output:

```text
Invalid JSON
```

Executable version: [`examples/handle_invalid_json.py`](examples/handle_invalid_json.py).

## 40. Common mistake: treating every text file as CSV

A text file containing prose, log lines, or one value per line does not become CSV merely because fields could theoretically be separated.

Use CSV when the contract is genuinely tabular and its quoting/delimiter rules are appropriate.

Use simpler text when simpler text is the actual format.

## 41. Common mistake: manually constructing JSON

Avoid this style:

```python
text = '{"name": "' + name + '", "score": ' + str(score) + '}'
```

Escaping quotes, backslashes, control characters, nested structures, booleans, and `null` quickly becomes error-prone.

Build Python values, then let `json.dumps()` or `json.dump()` serialize them.

## 42. Common mistake: trusting parsed data automatically

Successful parsing does not prove that required fields exist, types match your application contract, numeric ranges are valid, or strings are acceptable.

Treat file and network data as input:

```text
parse successfully
      ≠
safe and valid for every use
```

Validate the properties your program actually depends on.

## 43. Choosing among TXT, CSV, and JSON

| Shape or need | Good starting choice |
|---|---|
| Simple human-readable lines | TXT |
| Flat rows with consistent columns | CSV |
| Nested objects, arrays, booleans, and nulls | JSON |
| Data already governed by an external format contract | Use that required format |

The extension is not the deciding factor. The data model and interoperability contract are.

## 44. When to avoid inventing a custom text format

A tiny private format can be fine for a tiny controlled task. It becomes risky when you start adding:

- escaping rules;
- optional or repeated fields;
- quoted delimiters;
- nested values;
- versioning;
- multiple independent producers and consumers.

At that point, a standard format usually buys you tested parsers and clearer interoperability.

## 45. Exercise

Create a program called `study_export.py` with these requirements:

1. Start with a list of dictionaries containing `topic`, `score`, and `complete`.
2. Write the records to `study.csv` with `csv.DictWriter`.
3. Reopen the CSV with `csv.DictReader`, convert `score` to `int`, and convert `complete` back to `bool` with an explicit mapping such as `{"True": True, "False": False}`; reject unexpected text instead of using `bool()` directly.
4. Build a new list containing the converted records.
5. Write that list to `study.json` using `json.dump()` with UTF-8, `ensure_ascii=False`, and `indent=2`.
6. Reopen the JSON with `json.load()`.
7. Print only the topics whose score is at least 80.
8. Use `with` for every real file operation.

Extra questions:

- Why is `newline=""` used for the CSV file?
- Why must the CSV score be converted explicitly?
- Why would `bool(row["complete"])` be wrong when the CSV text is `"False"`?
- What exception would invalid JSON syntax raise?
- Why would `split(",")` be unsafe for a note containing commas?
- Which step is parsing, and which step is application validation?

## 46. Review checklist

Before continuing, confirm that you can answer these without guessing:

- What is the difference between a file extension and a data format?
- Does `.txt` define one universal record structure?
- Why should CSV not be parsed with a naive comma split?
- Why is `newline=""` recommended when a file object is used with `csv`?
- What do `csv.reader()` rows contain by default?
- Why might `DictReader` be clearer than numeric column indexes?
- What is the difference between `json.load()` and `json.loads()`?
- What is the difference between `json.dump()` and `json.dumps()`?
- What JSON value maps to Python `None`?
- What exception indicates invalid JSON syntax?
- Can every Python object be serialized to JSON automatically?
- Why are parsing and validation separate concepts?

## 47. Quick reference

| Need | Pattern |
|---|---|
| Read plain UTF-8 text | `open(path, "r", encoding="utf-8")` |
| Read CSV rows | `csv.reader(file)` |
| Write CSV rows | `csv.writer(file)` |
| Read CSV with named columns | `csv.DictReader(file)` |
| Write CSV with named columns | `csv.DictWriter(file, fieldnames=...)` |
| Open a CSV file object | `open(path, ..., encoding="utf-8", newline="")` |
| Parse JSON string | `json.loads(text)` |
| Create JSON string | `json.dumps(data)` |
| Parse JSON file | `json.load(file)` |
| Write JSON file | `json.dump(data, file)` |
| Preserve readable Unicode output | `ensure_ascii=False` |
| Pretty-print JSON | `indent=2` |
| Invalid JSON syntax | `json.JSONDecodeError` |
| JSON-incompatible object during serialization | `TypeError` |

A useful default pipeline is:

```text
open safely
    ↓
parse with the format-aware parser
    ↓
convert and validate application values
    ↓
use or transform trusted data
```

## What comes next

Chapter 04 adds common text-data formats to the file-management foundation. The final Phase 7 chapter, **Imports, Modules, and Packages**, will move from data stored across files to Python code organized across files.

```text
exceptions
    ↓
deliberate exception signaling
    ↓
safe file lifetime
    ↓
TXT / CSV / JSON data boundaries
    ↓
imports / modules / packages
```

## Official references

- Python 3.14 `csv` documentation: <https://docs.python.org/3.14/library/csv.html>
- Python 3.14 `json` documentation: <https://docs.python.org/3.14/library/json.html>
- Python 3.14 tutorial, Reading and Writing Files: <https://docs.python.org/3.14/tutorial/inputoutput.html#reading-and-writing-files>
- Python 3.14 tutorial, Saving structured data with `json`: <https://docs.python.org/3.14/tutorial/inputoutput.html#saving-structured-data-with-json>
