<div align="center">

# Controlling JSON Serialization and Decoding Contracts

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Back to Standard Library](../README.md) · [← Previous: Working with Dates and Time Calculations Using `datetime`](../02-datetime/README.md)

Phase 7 introduced JSON as a structured data format and taught the practical difference between `load()`, `loads()`, `dump()`, and `dumps()`. This chapter goes one layer deeper.

The `json` module is not only a way to read and write `.json` files. It is also a boundary tool. Its options decide which Python values are accepted, how numbers are reconstructed, whether non-standard values are tolerated, how custom types are represented, how duplicate object names are handled, and how stable the serialized representation is.

The goal is to turn "JSON works" into a more precise question:

```text
What JSON contract does this program accept and produce?
```

**Estimated study time:** 120–160 minutes.

**Python requirement:** Python 3.10 or newer for the core APIs. The direct `python -m json` command shown later is available in Python 3.14; older supported versions can use `python -m json.tool`.

**Documentation baseline:** behavior and examples were checked against the official Python 3.14 `json` documentation.

## Learning objectives

By the end of this chapter, you should be able to:

- treat JSON serialization as an interface contract rather than only a file operation;
- distinguish JSON text from byte encoding;
- produce stable output with `sort_keys` when deterministic ordering is useful;
- control whitespace with `indent` and `separators`;
- explain what `ensure_ascii` changes and what it does not change;
- reject non-finite floating-point values with `allow_nan=False`;
- reject Python's non-standard decoder constants with `parse_constant`;
- decode JSON numbers with custom functions such as `decimal.Decimal`;
- recognize interoperability limits around numeric range and precision;
- understand why JSON object member names are strings;
- avoid silently dropping unsupported keys with `skipkeys=True` unless that policy is deliberate;
- serialize selected custom Python values with `default` or `JSONEncoder`;
- reconstruct selected representations with `object_hook`;
- inspect ordered name-value pairs with `object_pairs_hook`;
- detect duplicate JSON object names when uniqueness is part of the contract;
- keep circular-reference checking enabled unless you have a specific reason not to;
- use `JSONDecodeError` details for useful diagnostics;
- limit untrusted JSON input according to the boundary you control;
- use Python's JSON command-line interface for validation and formatting;
- distinguish ordinary JSON documents from line-delimited JSON formats.

## 1. What changes from the Phase 7 JSON introduction?

You already know the four core operations:

```python
import json

text = json.dumps({"topic": "JSON"})
data = json.loads(text)
```

and file-oriented variants:

```python
import json

with open("data.json", "r", encoding="utf-8") as file:
    data = json.load(file)
```

Phase 7 focused on the format boundary:

```text
JSON text
   ↓ parsing
Python values
```

This chapter focuses on the policy around that boundary:

```text
Python values
   ↓ serialization policy
JSON representation
   ↓ transport / storage
JSON representation
   ↓ decoding policy
Python values
```

The APIs are familiar. The contracts are deeper.

## 2. Serialization is part of an interface contract

Two JSON strings can represent the same logical object while differing in whitespace or member order:

```json
{"topic":"JSON","score":88}
```

```json
{
  "score": 88,
  "topic": "JSON"
}
```

That means serialized text can have at least two kinds of requirements:

- **semantic requirements**, such as required fields and acceptable value types;
- **representation requirements**, such as whitespace, ordering, escaping, or strict numeric syntax.

Do not assume one implies the other.

## 3. `dumps()` produces text, not bytes

`json.dumps()` returns a Python `str`:

```python
import json

text = json.dumps({"topic": "JSON"})
print(type(text).__name__)
```

Output:

```text
str
```

If a network protocol or storage layer needs bytes, encoding is a separate step:

```python
payload = text.encode("utf-8")
```

Keep the layers distinct:

```text
Python values
   ↓ json.dumps()
Unicode text
   ↓ .encode("utf-8")
bytes
```

The encoder side of `json` works with text: `json.dumps()` returns `str`, and `json.dump()` writes text to a compatible file-like object. The decoder side accepts a broader set of inputs: `json.loads()` accepts `str`, `bytes`, and `bytearray`, while `json.load()` can consume a compatible file-like object whose `read()` returns one of those supported forms. If your application controls a network or storage byte boundary, an explicit encoding policy still makes that boundary easier to reason about.

## 4. Deterministic member order with `sort_keys=True`

Python dictionaries preserve insertion order, but insertion order is not always the representation policy you want.

For tests, snapshots, examples, or generated configuration files, sorted keys can make changes easier to compare:

```python
import json

record = {"status": "ready", "score": 88, "topic": "JSON"}
text = json.dumps(record, sort_keys=True)

print(text)
```

`sort_keys=True` orders dictionary keys in the serialized output.

This can improve determinism, but it does **not** turn arbitrary JSON into a universal canonical form. Canonicalization standards may define additional rules for numbers, Unicode, escaping, and other representation details.

## 5. Human-readable output with `indent`

Use `indent` when people are expected to inspect the output:

```python
import json

record = {"topic": "JSON", "score": 88}
print(json.dumps(record, indent=2))
```

Pretty printing increases whitespace and usually increases the size of the representation.

Choose it because the interface benefits from readability, not because indented JSON is somehow more correct.

## 6. Compact output with `separators`

For a compact representation, remove optional spaces around separators:

```python
import json

record = {"topic": "JSON", "score": 88}
text = json.dumps(record, separators=(",", ":"))

print(text)
```

This produces:

```text
{"topic":"JSON","score":88}
```

A common deterministic machine-oriented recipe is:

```python
import json

record = {"status": "ready", "score": 88, "topic": "JSON"}
text = json.dumps(
    record,
    sort_keys=True,
    separators=(",", ":"),
)
```

Again, stable output for your application is not automatically a standards-defined canonical JSON representation.

## 7. `ensure_ascii` controls escaping, not text encoding

By default, non-ASCII characters are escaped:

```python
import json

record = {"language": "Português"}
print(json.dumps(record))
```

With `ensure_ascii=False`, those characters can remain directly visible in the returned `str`:

```python
import json

record = {"language": "Português"}
print(json.dumps(record, ensure_ascii=False))
```

This does **not** mean the JSON module selected UTF-8 bytes. The result is still a Python `str`.

If you write it to a UTF-8 text file, the encoding decision belongs to the file boundary:

```python
with open("data.json", "w", encoding="utf-8") as file:
    json.dump(record, file, ensure_ascii=False)
```

## 8. Strict JSON output and non-finite floats

Python's encoder deliberately allows these floating-point values by default:

- `NaN`;
- `Infinity`;
- `-Infinity`.

Those tokens are not valid JSON according to the interoperable JSON specification.

If standards-compliant output is required, use `allow_nan=False`:

```python
import json

record = {"value": float("nan")}

try:
    json.dumps(record, allow_nan=False)
except ValueError:
    print("Non-finite float rejected")
```

This is a contract decision. A successful default `json.dumps()` call is not proof that the generated text avoids Python's non-standard numeric extension.

## 9. Strict JSON input and `parse_constant`

The decoder has the matching extension. By default, Python accepts `NaN`, `Infinity`, and `-Infinity`.

To reject them, provide a callback through `parse_constant`:

```python
import json


def reject_nonstandard_constant(value: str):
    raise ValueError(f"non-standard JSON constant: {value}")


text = '{"value": NaN}'

try:
    json.loads(text, parse_constant=reject_nonstandard_constant)
except ValueError as error:
    print(error)
```

`JSONDecodeError` still represents ordinary JSON syntax errors. The `ValueError` above comes from the callback you deliberately supplied.

A strict interface often needs both sides:

```text
encoding: allow_nan=False
decoding: parse_constant=rejecting_callback
```

## 10. JSON numbers do not define your application precision policy

JSON has a number syntax, but different implementations can map numbers to different runtime numeric types and precision limits.

Python normally decodes:

- integer-form JSON numbers without a fraction or exponent to `int`;
- JSON numbers containing a fraction or exponent to `float`.

```python
import json

data = json.loads('{"count": 3, "ratio": 0.1}')

print(type(data["count"]).__name__)
print(type(data["ratio"]).__name__)
```

For interfaces that exchange very large integers or high-precision decimal values, the receiving system's limits matter too. A Python `int` can represent values that another implementation may not preserve exactly.

Interoperability is a property of both ends of the interface.

## 11. Decode JSON floating-point numbers with `parse_float`

The decoder can hand each JSON floating-point number to a function you choose. That includes tokens with a fractional part, such as `19.90`, and exponent forms such as `1e2`.

For example, `decimal.Decimal` can preserve the decimal text exactly:

```python
import json
from decimal import Decimal


data = json.loads(
    '{"price": 19.90}',
    parse_float=Decimal,
)

print(data["price"])
print(type(data["price"]).__name__)
```

This is useful when the application needs decimal semantics rather than binary floating-point semantics.

It does not mean `Decimal` becomes a native JSON type. It is a decoding choice inside Python.

## 12. `parse_int` can customize integer decoding too

`parse_int` receives the text of each JSON integer:

```python
import json


def tagged_integer(text: str):
    return ("integer", text)


data = json.loads('{"count": 42}', parse_int=tagged_integer)
print(data["count"])
```

Customizing integer parsing is less common for beginner applications, but it shows an important principle: decoding is configurable reconstruction, not a magical one-to-one conversion.

Use a custom numeric hook only when its behavior is part of a documented contract.

## 13. JSON object names are strings

JSON object member names are strings.

Python's encoder accepts some basic non-string dictionary keys and converts them, so a round trip may not preserve key types:

```python
import json

original = {1: "one", 2: "two"}
restored = json.loads(json.dumps(original))

print(original)
print(restored)
print(original == restored)
```

The decoded keys are strings.

If key type carries meaning in your application, represent that meaning explicitly instead of relying on a dictionary-key round trip.

## 14. Prefer visible failures to `skipkeys=True`

By default, unsupported dictionary key types raise `TypeError`:

```python
import json

record = {(1, 2): "coordinate"}

try:
    json.dumps(record)
except TypeError:
    print("Unsupported key type")
```

`skipkeys=True` can silently omit unsupported keys:

```python
text = json.dumps(record, skipkeys=True)
```

That can be appropriate only when dropping such entries is an explicit policy.

For most data contracts, silently losing data is more dangerous than receiving an exception that forces the representation to be designed correctly.

## 15. Custom serialization with `default`

Arbitrary Python objects are not JSON serializable by default.

A `default` callback can convert selected unsupported objects into JSON-compatible structures:

```python
import json
from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int


def encode_custom(value):
    if isinstance(value, Point):
        return {"type": "point", "x": value.x, "y": value.y}
    raise TypeError(f"unsupported type: {type(value).__name__}")


text = json.dumps(Point(4, 7), default=encode_custom, sort_keys=True)
print(text)
```

A good callback handles only types it deliberately supports and raises `TypeError` for everything else.

Do not turn `default` into a catch-all that guesses how arbitrary objects should be serialized.

## 16. Tagged representations are your schema, not JSON's schema

This representation:

```json
{"type": "point", "x": 4, "y": 7}
```

is ordinary JSON. The meaning of `"type": "point"` belongs to your application.

That means your contract should answer questions such as:

- Is `type` required?
- Which type names are allowed?
- Are `x` and `y` required integers?
- What happens when extra fields appear?
- Which schema version produced the document?

JSON syntax does not answer those business questions for you.

## 17. A custom `JSONEncoder` can centralize encoding behavior

For reusable encoding policy, subclass `json.JSONEncoder` and override `default()`:

```python
import json
from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int


class StudyEncoder(json.JSONEncoder):
    def default(self, value):
        if isinstance(value, Point):
            return {"type": "point", "x": value.x, "y": value.y}
        return super().default(value)


text = json.dumps(Point(4, 7), cls=StudyEncoder)
print(text)
```

Use a custom encoder when the application genuinely benefits from a reusable encoder policy. For a single conversion, an explicit transformation or `default` function is often easier to understand.

## 18. Custom reconstruction with `object_hook`

`object_hook` is called for each decoded JSON object after it has been turned into a dictionary.

```python
import json


def decode_custom(record):
    if record.get("type") == "point":
        return (record["x"], record["y"])
    return record


text = '{"type": "point", "x": 4, "y": 7}'
data = json.loads(text, object_hook=decode_custom)

print(data)
```

The hook's return value replaces that dictionary in the decoded result.

This is powerful, so keep the policy narrow and explicit.

## 19. Do not let untrusted tags choose arbitrary code paths

An `object_hook` is Python code executed while decoding.

Avoid designs where an untrusted string can dynamically select arbitrary imports, classes, functions, or constructors.

Prefer a fixed allowlist of representations you understand:

```text
input tag
   ↓ validate against known values
known conversion
```

JSON itself is a data format. Risk appears when your application gives untrusted data excessive authority over what code runs next.

## 20. Duplicate object names are accepted by default

Consider this JSON text:

```json
{"topic": "JSON", "topic": "CSV"}
```

Python's default decoder accepts repeated names and keeps only the last value:

```python
import json

text = '{"topic": "JSON", "topic": "CSV"}'
data = json.loads(text)

print(data)
```

Output:

```text
{'topic': 'CSV'}
```

If uniqueness matters to your interface, default decoding is not enough to enforce it.

## 21. Inspect pairs with `object_pairs_hook`

`object_pairs_hook` receives each JSON object's name-value pairs in order, before they become an ordinary dictionary.

That makes duplicate detection possible:

```python
import json


def reject_duplicate_keys(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON object name: {key}")
        result[key] = value
    return result


text = '{"topic": "JSON", "topic": "CSV"}'

try:
    json.loads(text, object_pairs_hook=reject_duplicate_keys)
except ValueError as error:
    print(error)
```

This is another example of turning a vague assumption into an enforced contract.

## 22. `object_pairs_hook` takes priority over `object_hook`

If both are provided, `object_pairs_hook` takes priority for object decoding.

Avoid combining hooks casually. If one policy needs duplicate detection and custom reconstruction, design the steps so that their order and responsibilities are obvious.

A clear decoder policy is easier to audit than a collection of hooks that accidentally overlap.

## 23. Keep circular-reference checking enabled

Python containers can contain cycles:

```python
items = []
items.append(items)
```

JSON cannot represent that object graph directly.

The encoder checks for circular references by default. Keep `check_circular=True` unless you have a measured and well-understood reason to disable it.

Turning the check off does not make cycles serializable. It removes the protection that detects them and can lead to recursion failure.

## 24. Use `JSONDecodeError` details for diagnostics

`JSONDecodeError` includes useful location information:

```python
import json

text = '{"topic": "JSON",}'

try:
    json.loads(text)
except json.JSONDecodeError as error:
    print(error.msg)
    print(error.lineno)
    print(error.colno)
```

Useful fields include:

- `msg` for the decoder message;
- `lineno` for the line number;
- `colno` for the column number;
- `pos` for the character position in the source document.

Expose only the amount of source detail that is appropriate for the interface. Diagnostics for a developer tool and diagnostics returned by a public service do not have to be identical.

## 25. Parsing valid JSON is still not schema validation

This is valid JSON:

```json
{"score": -500, "status": "banana"}
```

The decoder's job is to reconstruct values. Your program still needs to validate domain rules:

```python
import json

record = json.loads('{"score": -500}')

if not 0 <= record["score"] <= 100:
    raise ValueError("score must be between 0 and 100")
```

Keep these questions separate:

```text
Is the text valid JSON?
        ↓
Does the decoded shape match the interface schema?
        ↓
Do the values satisfy application rules?
```

## 26. Bound untrusted input

The official Python documentation warns that malicious JSON can consume considerable CPU and memory during decoding.

The `json` module is not a general resource quota system. At boundaries you control, consider limits such as:

- maximum request or file size;
- maximum accepted nesting defined by your surrounding application or gateway;
- timeouts at the transport or worker level;
- schema limits on array lengths and string sizes.

Do not accept an unlimited payload merely because the syntax is JSON.

## 27. Text encoding is a separate transport concern

JSON exchanged as bytes needs an agreed character encoding. UTF-8 is the interoperability default in modern systems.

When you control file I/O, make the text encoding explicit:

```python
import json

record = {"language": "Português"}

with open("data.json", "w", encoding="utf-8") as file:
    json.dump(record, file, ensure_ascii=False)
```

Python's serializer does not add a byte-order mark to its JSON output. Keep transport encoding decisions outside the logical data model whenever possible.

## 28. Top-level JSON does not have to be an object

These are all valid top-level JSON values under modern JSON specifications:

```json
42
```

```json
"ready"
```

```json
true
```

```json
[1, 2, 3]
```

Your API may still require an object or array. That would be an **application contract**, not a universal JSON syntax rule.

Validate the top-level shape you actually expect.

## 29. The command-line interface can validate and pretty-print JSON

Python includes a JSON command-line tool.

In Python 3.14, the preferred direct form is:

```text
python -m json data.json
```

For compatibility with earlier versions, this form remains available:

```text
python -m json.tool data.json
```

The command is useful for quick validation and human-readable formatting.

Python 3.14's interface also supports options such as:

```text
--sort-keys
--no-ensure-ascii
--json-lines
--indent
--tab
--compact
```

Use `python -m json --help` to inspect the exact options in the interpreter you are running.

## 30. JSON Lines is a different framing contract

A single JSON document contains one top-level JSON value.

This is not one ordinary JSON document:

```text
{"id": 1}
{"id": 2}
{"id": 3}
```

It can, however, be a valid **JSON Lines / line-delimited JSON** contract when every line is independently defined as one JSON value.

Python 3.14's JSON CLI has `--json-lines` support, but your application still has to declare that it is consuming a line-delimited format.

Do not confuse:

```text
one JSON document containing an array
```

with:

```text
multiple JSON values framed by line boundaries
```

The framing rule is part of the interface.

## 31. Repeated `dump()` calls still do not frame a stream

This remains an important boundary from Phase 7:

```python
json.dump(first, file)
json.dump(second, file)
```

Repeated calls do not automatically add a separator or container that turns the values into one valid JSON document.

Choose one explicit structure:

- one array containing many values;
- one object containing named collections;
- a documented line-delimited JSON format;
- another protocol that defines framing.

## 32. Stable output is not cryptographic canonicalization

A useful local recipe such as:

```python
json.dumps(
    data,
    ensure_ascii=False,
    sort_keys=True,
    separators=(",", ":"),
)
```

can make snapshots and diffs stable for a controlled Python application.

Do not automatically use that string for signatures, hashes shared across implementations, or cross-language canonicalization protocols.

Those use cases require a canonicalization specification that defines every relevant representation rule.

## 33. A practical strict-decoding policy

For an interface that wants to reject Python's non-standard numeric constants and duplicate object names, combine narrow hooks deliberately:

```python
import json


def reject_nonstandard_constant(value: str):
    raise ValueError(f"non-standard JSON constant: {value}")


def reject_duplicate_keys(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON object name: {key}")
        result[key] = value
    return result


def load_strict_json(text: str):
    return json.loads(
        text,
        parse_constant=reject_nonstandard_constant,
        object_pairs_hook=reject_duplicate_keys,
    )
```

This still does not validate your business schema. It only tightens two JSON-decoding policies.

## 34. A practical deterministic-encoding policy

For human-independent snapshots or generated artifacts where compact stable output helps:

```python
import json


def dump_stable_json(data):
    return json.dumps(
        data,
        allow_nan=False,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    )
```

The policy now communicates several decisions explicitly:

- reject non-finite floats;
- keep Unicode characters readable in the Python text;
- sort dictionary keys;
- omit optional separator spaces.

That is much easier to review than relying on undocumented defaults scattered around a codebase.

## 35. Common mistakes

### Mistake 1: treating successful parsing as schema validation

Valid syntax does not prove required fields, types, ranges, or business rules are correct.

### Mistake 2: assuming default Python JSON is strict in both directions

By default, Python accepts and emits `NaN`, `Infinity`, and `-Infinity`.

### Mistake 3: assuming a round trip preserves every Python type

Tuples become arrays and return as lists; object names are strings; custom objects need an explicit representation.

### Mistake 4: enabling `skipkeys=True` to make errors disappear

That can silently remove data.

### Mistake 5: using `default=str` without defining a contract

Turning every unsupported object into an arbitrary display string may make serialization succeed while destroying type meaning.

### Mistake 6: using `sort_keys=True` and calling the result canonical JSON

Sorted keys solve only one representation dimension.

### Mistake 7: decoding unlimited untrusted input

Syntax parsers can still consume CPU and memory.

### Mistake 8: dynamically constructing arbitrary Python objects from untrusted tags

Keep custom reconstruction on an explicit allowlist and validate fields before using them.

## 36. Practical example: deterministic JSON output

```python
import json


data = {"status": "ready", "score": 88, "topic": "JSON"}
text = json.dumps(
    data,
    ensure_ascii=False,
    sort_keys=True,
    separators=(",", ":"),
)

print(text)
```

Expected output:

```text
{"score":88,"status":"ready","topic":"JSON"}
```

Executable version: [`examples/deterministic_json.py`](examples/deterministic_json.py).

## 37. Practical example: strict non-finite-number handling

```python
import json


def reject_nonstandard_constant(value: str):
    raise ValueError(f"non-standard JSON constant: {value}")


try:
    json.dumps({"value": float("nan")}, allow_nan=False)
except ValueError:
    print("Encoding rejected non-finite float")

try:
    json.loads('{"value": NaN}', parse_constant=reject_nonstandard_constant)
except ValueError:
    print("Decoding rejected non-standard constant")
```

Executable version: [`examples/strict_numbers.py`](examples/strict_numbers.py).

## 38. Practical example: decimal decoding

```python
import json
from decimal import Decimal


data = json.loads(
    '{"price": 19.90, "quantity": 3}',
    parse_float=Decimal,
)

print(data["price"])
print(type(data["price"]).__name__)
print(type(data["quantity"]).__name__)
```

Executable version: [`examples/decimal_decode.py`](examples/decimal_decode.py).

## 39. Practical example: reject duplicate object names

```python
import json


def reject_duplicate_keys(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON object name: {key}")
        result[key] = value
    return result


samples = [
    '{"topic": "JSON", "score": 88}',
    '{"topic": "JSON", "topic": "CSV"}',
]

for text in samples:
    try:
        data = json.loads(text, object_pairs_hook=reject_duplicate_keys)
    except ValueError as error:
        print(error)
    else:
        print(data)
```

Executable version: [`examples/reject_duplicate_keys.py`](examples/reject_duplicate_keys.py).

## 40. Exercise

Create a function called `decode_settings(text)` for an application configuration contract.

Requirements:

1. Parse the JSON string.
2. Reject `NaN`, `Infinity`, and `-Infinity`.
3. Reject duplicate object names.
4. Require the top-level value to be a dictionary.
5. Require exactly these fields: `theme`, `refresh_seconds`, and `enabled`.
6. Require `theme` to be a non-empty string.
7. Require `refresh_seconds` to be an integer from 1 through 3600. Remember that `bool` is a subclass of `int`, so reject booleans explicitly if they are not valid here.
8. Require `enabled` to be a boolean.
9. Return the validated dictionary.

Then create a second function, `encode_settings(data)`, that:

1. serializes with `allow_nan=False`;
2. uses `ensure_ascii=False`;
3. sorts keys;
4. uses compact separators.

Test at least these cases:

```text
valid settings
missing field
duplicate field
NaN value
wrong top-level type
refresh_seconds = true
refresh_seconds = 0
```

The important part is not only making valid input work. Make each boundary explicit enough that a future reader can explain **why** invalid input is rejected.

## 41. Quick reference

| Need | Tool / policy |
|---|---|
| Python value → JSON text | `json.dumps()` |
| JSON text / bytes → Python value | `json.loads()` |
| Read JSON from compatible text or binary file-like object | `json.load()` |
| Write JSON to text file-like object | `json.dump()` |
| Pretty output | `indent=2` or another explicit indent |
| Compact output | `separators=(",", ":")` |
| Stable key ordering | `sort_keys=True` |
| Keep non-ASCII characters visible | `ensure_ascii=False` |
| Reject non-finite floats when encoding | `allow_nan=False` |
| Reject `NaN` / infinities when decoding | `parse_constant=...` |
| Decode JSON floating-point numbers differently | `parse_float=...` |
| Decode integers differently | `parse_int=...` |
| Convert unsupported custom values | `default=...` |
| Reusable custom encoder | `cls=YourJSONEncoder` |
| Transform decoded JSON objects | `object_hook=...` |
| Inspect ordered object pairs / duplicates | `object_pairs_hook=...` |
| Decoder syntax diagnostics | `json.JSONDecodeError` |
| Validate / pretty-print from CLI on Python 3.14 | `python -m json` |
| Backward-compatible CLI form | `python -m json.tool` |

## 42. Design checklist

Before publishing a JSON interface, ask:

```text
What top-level shape is accepted?
Which fields are required?
Are duplicate names rejected?
Are NaN and infinities rejected?
What numeric precision is required?
How large may the document be?
How are custom types represented?
Is key ordering significant only for presentation, or for another protocol?
What character encoding carries the JSON text as bytes?
Is this one JSON document or a line-delimited format?
```

If those answers are explicit, the JSON boundary becomes much easier to test and maintain.

## References

- [Python 3.14 documentation: `json` — JSON encoder and decoder](https://docs.python.org/3.14/library/json.html)
- [Python 3.14 documentation: JSON command-line interface](https://docs.python.org/3.14/library/json.html#module-json.tool)
- [RFC 8259: The JavaScript Object Notation (JSON) Data Interchange Format](https://www.rfc-editor.org/rfc/rfc8259)

## Next chapter

Continue with [**Chapter 04: Controlling CSV Dialects and Tabular Text Contracts**](../04-csv/README.md). It deepens dialects, quoting, escaping, row-shape validation, sniffing, encoding boundaries, and spreadsheet-consumer considerations.
