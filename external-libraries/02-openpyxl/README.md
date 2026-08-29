<div align="center">

# Automating Excel Workbooks with `openpyxl`

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Back to External Libraries](../README.md) · [← Previous: `pandas`](../01-pandas/README.md)

`pandas` treats spreadsheet-like data primarily as tables. `openpyxl` works at a different layer: the Excel workbook itself. It lets Python create, inspect, edit, format, and save Office Open XML workbooks while preserving workbook concepts such as worksheets, cells, formulas, styles, tables, validations, charts, and print settings.

This chapter targets **openpyxl 3.1.x** and was researched against the current 3.1 documentation and the stable **openpyxl 3.1.5** package published on PyPI. PyPI declares Python 3.8 or newer; this repository validates the examples on Python 3.13.

**Estimated study time:** 240–330 minutes.

## Learning goals

By the end of this chapter, you should be able to:

- explain when `openpyxl` is a better fit than `pandas` or the standard `csv` module;
- create, load, inspect, and save `.xlsx` workbooks;
- work safely with worksheets, cells, ranges, and row iteration;
- distinguish formulas from calculated values;
- understand what `data_only`, `read_only`, `write_only`, and `keep_vba` actually mean;
- apply reusable styles, number formats, dimensions, and freeze panes;
- create worksheet tables, validation rules, filters, comments, hyperlinks, and charts;
- understand the limits of merged cells, row/column movement, formula translation, VBA preservation, and round-trip fidelity;
- choose optimized modes for large workbooks;
- treat spreadsheet files as external input with explicit security and validation boundaries;
- combine `pandas` and `openpyxl` without confusing their responsibilities;
- build deterministic workbook automation that can be reviewed and tested without Microsoft Excel installed.

## 1. Why `openpyxl` exists

Excel workbooks contain more than rectangular data. They may contain several worksheets, formulas, formatting, tables, validation rules, merged regions, charts, comments, hyperlinks, print settings, and workbook metadata.

`openpyxl` is a third-party Python library for reading and writing Office Open XML spreadsheet files such as `.xlsx` and `.xlsm`.

Use it when the **workbook structure itself matters**.

## 2. `pandas` and `openpyxl` solve different problems

A useful distinction is:

```text
pandas   -> manipulate tabular data
openpyxl -> manipulate Excel workbook structure
```

If you need to group ten million rows, `pandas` is usually the stronger abstraction. If you need to set `B2` to a formula, freeze the first row, apply a number format, create a worksheet table, or preserve workbook layout, `openpyxl` is the more natural layer.

Many real workflows use both.

## 3. External libraries require a dependency contract

The repository declares executable Phase 9 dependencies in `requirements-external.txt`.

For this chapter the contract is:

```text
openpyxl >= 3.1 and < 3.2
```

Pinning a supported minor series avoids silently teaching against an unknown future API while still allowing compatible patch releases.

## 4. Install the dependency in an isolated environment

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it for your operating system, then install the repository contract:

```bash
python -m pip install -r requirements-external.txt
```

A direct `pip install openpyxl` is valid for experimentation, but a dependency file makes a project environment reproducible.

## 5. Know the workbook formats in scope

`openpyxl` is designed around Office Open XML workbook formats such as:

```text
.xlsx
.xlsm
.xltx
.xltm
```

It is not a general reader for every file Excel can open. In particular, legacy binary `.xls` files and `.xlsb` workbooks are different formats and require different tooling.

Treat the extension as part of your input contract.

## 6. Create a workbook

The central class is `Workbook`:

```python
from openpyxl import Workbook


workbook = Workbook()
worksheet = workbook.active
print(worksheet.title)
```

```text
Sheet
```

A normal new workbook begins with one active worksheet.

## 7. Give worksheets meaningful names

Rename the active sheet or create additional sheets explicitly:

```python
from openpyxl import Workbook


workbook = Workbook()
summary = workbook.active
summary.title = "Summary"
details = workbook.create_sheet("Details")
print(workbook.sheetnames)
```

```text
['Summary', 'Details']
```

Sheet names are part of workbook navigation and may also appear in formulas and defined names.

## 8. Select a worksheet by name

Use mapping-style access:

```python
from openpyxl import Workbook


workbook = Workbook()
workbook.active.title = "Summary"
worksheet = workbook["Summary"]
print(worksheet.title)
```

Avoid relying on a sheet's physical position when its name is the real contract.

## 9. Cells use Excel-style coordinates

Cells can be accessed with coordinates such as `A1`:

```python
from openpyxl import Workbook


workbook = Workbook()
worksheet = workbook.active
worksheet["A1"] = "status"
worksheet["B1"] = "ready"
print(worksheet["B1"].value)
```

```text
ready
```

Coordinates are convenient when workbook layout is fixed and meaningful.

## 10. `cell()` uses one-based row and column indexes

Programmatic generation often fits `Worksheet.cell()` better:

```python
from openpyxl import Workbook


workbook = Workbook()
worksheet = workbook.active
worksheet.cell(row=2, column=3, value=42)
print(worksheet["C2"].value)
```

```text
42
```

Excel rows and columns are one-based in this API.

## 11. Accessing cells can create them in memory

A normal worksheet creates cell objects when they are first accessed. That means a loop over an unnecessarily huge coordinate range can allocate many cells even if you never assign useful data.

Do not scan a million-by-million rectangle merely to discover which cells exist.

Use known ranges, worksheet dimensions, or optimized read mode when appropriate.

## 12. Append complete rows

For row-oriented output, `append()` is usually clearer than assigning every coordinate:

```python
from openpyxl import Workbook


workbook = Workbook()
worksheet = workbook.active
worksheet.append(["item", "quantity"])
worksheet.append(["Cable", 3])
worksheet.append(["Adapter", 2])
print(worksheet.max_row)
```

```text
3
```

This works well for exports assembled one record at a time.

## 13. Iterate rows instead of hard-coding every cell

`iter_rows()` exposes a rectangular region:

```python
from openpyxl import Workbook


workbook = Workbook()
worksheet = workbook.active
worksheet.append(["name", "score"])
worksheet.append(["A", 8])
worksheet.append(["B", 9])

for row in worksheet.iter_rows(min_row=2, values_only=True):
    print(row)
```

```text
('A', 8)
('B', 9)
```

`values_only=True` returns Python values instead of `Cell` objects when cell metadata is unnecessary.

## 14. Iterate columns only when the access pattern needs them

Normal worksheets also support `iter_cols()`. Row iteration is often more natural for record-like data, while column iteration is useful when a workbook rule is column-oriented.

Optimized read-only mode has a narrower API, so do not design every workflow around methods that are unavailable there.

## 15. Worksheet dimensions are a hint, not a business rule

Properties such as `max_row`, `max_column`, and `calculate_dimension()` describe the worksheet's apparent used region.

They do not prove that every cell inside that region contains meaningful data.

Blank but formatted cells, stale workbook metadata, or third-party generators can make dimensions larger or smaller than expected.

## 16. Save to a new path deliberately

A workbook is persisted with `save()`:

```python
from pathlib import Path
from tempfile import TemporaryDirectory

from openpyxl import Workbook


with TemporaryDirectory() as temp_dir:
    path = Path(temp_dir) / "report.xlsx"
    workbook = Workbook()
    workbook.active["A1"] = "ready"
    workbook.save(path)
    print(path.exists())
```

```text
True
```

For production automation, prefer a deliberate output path over casually overwriting the source workbook.

## 17. Load an existing workbook

Use `load_workbook()`:

```python
from pathlib import Path
from tempfile import TemporaryDirectory

from openpyxl import Workbook, load_workbook


with TemporaryDirectory() as temp_dir:
    path = Path(temp_dir) / "input.xlsx"
    workbook = Workbook()
    workbook.active["A1"] = "loaded"
    workbook.save(path)

    reloaded = load_workbook(path)
    print(reloaded.active["A1"].value)
    reloaded.close()
```

```text
loaded
```

Closing is especially important for read-only workbooks and is a good explicit habit for file-backed resources.

## 18. A round trip can lose unsupported workbook features

Opening a complex workbook and saving it again is not guaranteed to preserve every artifact created by Excel or another application.

The official tutorial explicitly warns that openpyxl does not read every possible workbook item and that some shapes can be lost during load/save round trips.

Therefore:

```text
load -> edit one cell -> save
```

is not automatically a lossless transformation for an arbitrary workbook.

## 19. `read_only=True` is a different operating mode

Large workbooks can consume substantial memory. Read-only mode lazily streams worksheet content:

```python
from openpyxl import load_workbook


workbook = load_workbook("large.xlsx", read_only=True, data_only=True)
worksheet = workbook["Data"]
for row in worksheet.iter_rows(values_only=True):
    process = row
workbook.close()
```

The example is intentionally illustrative rather than executable because it depends on an external file.

Read-only worksheets are not normal editable worksheets.

## 20. Read-only mode must be closed explicitly

The official optimized-mode documentation calls out `close()` for read-only workbooks.

Use a `try/finally` boundary when later processing can fail:

```python
from openpyxl import load_workbook


workbook = load_workbook("large.xlsx", read_only=True)
try:
    worksheet = workbook.active
    for row in worksheet.iter_rows(values_only=True):
        process = row
finally:
    workbook.close()
```

Resource cleanup should survive exceptions.

## 21. Read-only dimensions can be wrong

Lazy reading depends on dimension metadata stored in the workbook. Some producer applications write incorrect dimensions.

The documentation recommends checking `calculate_dimension()` and, when you know the metadata is wrong, using `reset_dimensions()` on a read-only worksheet.

Do this only when you have an external reason to know the stored dimensions are incorrect.

## 22. `write_only=True` is optimized for streaming output

Write-only workbooks are created differently:

```python
from openpyxl import Workbook


workbook = Workbook(write_only=True)
worksheet = workbook.create_sheet("Data")
worksheet.append(["id", "value"])
worksheet.append([1, 10])
worksheet.append([2, 20])
```

Unlike a normal `Workbook()`, a write-only workbook starts without a worksheet. You create one explicitly.

## 23. Write-only mode is append-oriented

A write-only worksheet is designed for sequential output. Rows are added with `append()` instead of arbitrary read/write cell access.

This is a strong fit for large exports where records arrive in order and old rows do not need to be edited again.

## 24. A write-only workbook can only be saved once

The optimized-mode documentation states that a write-only workbook can be saved only once.

That means the workflow should be designed as:

```text
configure workbook -> append rows -> save once
```

not:

```text
save -> append more -> save again
```

Create workbook-level settings that must appear before cell data before you begin streaming rows.

## 25. Choose normal, read-only, and write-only modes intentionally

| Need | Prefer |
|---|---|
| edit arbitrary cells | normal workbook |
| inspect styles, charts, images, and full workbook structure | normal workbook |
| stream a very large existing worksheet | `read_only=True` |
| stream a very large new export | `Workbook(write_only=True)` |
| repeatedly save while editing | normal workbook |

Optimized modes trade capabilities for lower memory use.

## 26. Python values are converted to spreadsheet cell values

Cells can store common Python values such as strings, numbers, booleans, dates, datetimes, and formulas represented as strings beginning with `=`.

Keep your own domain validation separate. The fact that a value can be stored in a cell does not mean it is valid for your application.

## 27. Dates are values plus number formats

Excel stores date/time values with spreadsheet date semantics and displays them using number formats.

When you assign a Python `datetime`, openpyxl applies a date-time-compatible format automatically:

```python
from datetime import datetime

from openpyxl import Workbook


workbook = Workbook()
worksheet = workbook.active
worksheet["A1"] = datetime(2026, 8, 29, 14, 30)
print(worksheet["A1"].is_date)
```

```text
True
```

Do not treat the displayed text in Excel as the only representation that matters.

## 28. Excel has two date systems

Spreadsheet dates may use the 1900 or 1904 date system depending on workbook settings and history.

Let the workbook and openpyxl manage workbook date conversion instead of manually adding a fixed number of days to serial values.

Manual serial arithmetic is an easy way to create off-by-one and epoch errors.

## 29. Formulas are stored as formulas

Assign a formula string beginning with `=`:

```python
from openpyxl import Workbook


workbook = Workbook()
worksheet = workbook.active
worksheet["A1"] = 10
worksheet["A2"] = 20
worksheet["A3"] = "=SUM(A1:A2)"
print(worksheet["A3"].value)
```

```text
=SUM(A1:A2)
```

The cell contains a formula expression, not a Python calculation.

## 30. `openpyxl` does not calculate formulas

This is one of the most important boundaries in the library.

`openpyxl` can read and write formula expressions, but it is not an Excel calculation engine. Writing `=SUM(A1:A2)` does not cause openpyxl to compute `30`.

If your Python workflow requires the result now, calculate the value in Python or use a separate calculation engine with a documented contract.

## 31. `data_only=True` reads cached formula results

When loading a workbook, `data_only` controls whether formula cells expose the formula or the value cached the last time a spreadsheet application calculated the workbook.

```text
load_workbook(path, data_only=False) -> formula text
load_workbook(path, data_only=True)  -> cached result, if available
```

A newly created workbook may have no cached calculated value at all.

Do not mistake `data_only=True` for “calculate formulas now.”

## 32. Formula names are written in English

The openpyxl formula documentation states that function names must use their English names and arguments use commas.

For example:

```python
from openpyxl import Workbook


workbook = Workbook()
worksheet = workbook.active
worksheet["A1"] = "=SUM(1,2,3)"
print(worksheet["A1"].value)
```

```text
=SUM(1,2,3)
```

Do not generate locale-specific formula syntax from how Excel happens to display formulas on one machine.

## 33. Styles are workbook objects, not display strings

Common style components include:

```text
Font
PatternFill / GradientFill
Border
Alignment
Protection
number_format
```

The style model is explicit because an Excel cell's appearance is composed from several independent properties.

## 34. Apply a font, fill, and alignment

```python
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill


workbook = Workbook()
worksheet = workbook.active
cell = worksheet["A1"]
cell.value = "Header"
cell.font = Font(bold=True)
cell.fill = PatternFill(fill_type="solid", fgColor="D9EAF7")
cell.alignment = Alignment(horizontal="center")
print(cell.font.bold)
```

```text
True
```

Formatting should communicate structure, not compensate for unclear data.

## 35. Cell styles are effectively immutable after assignment

The official styles documentation explains that assigned cell-style components are shared and cannot be mutated in place.

This is intentionally invalid:

```text
a1.font.italic = True
```

Assign a new `Font` object instead:

```python
from openpyxl import Workbook
from openpyxl.styles import Font


workbook = Workbook()
worksheet = workbook.active
worksheet["A1"].font = Font(color="FF0000")
worksheet["A1"].font = Font(color="FF0000", italic=True)
print(worksheet["A1"].font.italic)
```

```text
True
```

## 36. Reuse style objects instead of creating thousands of variants

If many cells share the same visual role, reuse the same style definition or a `NamedStyle`.

Generating slightly different style objects for every cell can inflate the workbook's style table and file size.

Treat styles as a controlled vocabulary: header, currency, date, warning, input, output.

## 37. Number formats change display, not the underlying value

```python
from openpyxl import Workbook


workbook = Workbook()
worksheet = workbook.active
worksheet["A1"] = 0.125
worksheet["A1"].number_format = "0.00%"
print(worksheet["A1"].value)
```

```text
0.125
```

Excel may display `12.50%`, but the stored numeric value remains `0.125`.

This distinction matters when another program reads the workbook.

## 38. Named styles make repeated formatting explicit

```python
from openpyxl import Workbook
from openpyxl.styles import Font, NamedStyle


workbook = Workbook()
worksheet = workbook.active
header = NamedStyle(name="header")
header.font = Font(bold=True)
workbook.add_named_style(header)
worksheet["A1"].style = "header"
print(worksheet["A1"].style)
```

```text
header
```

Once a named style has been assigned to a cell, later changes to the `NamedStyle` do not retroactively restyle that cell.

## 39. Column width and row height are layout metadata

```python
from openpyxl import Workbook


workbook = Workbook()
worksheet = workbook.active
worksheet.column_dimensions["A"].width = 24
worksheet.row_dimensions[1].height = 30
print(worksheet.column_dimensions["A"].width)
```

```text
24.0
```

Do not assume openpyxl will reproduce Excel's interactive AutoFit behavior merely from content.

## 40. Freeze panes preserve context while scrolling

```python
from openpyxl import Workbook


workbook = Workbook()
worksheet = workbook.active
worksheet.freeze_panes = "A2"
print(worksheet.freeze_panes)
```

```text
A2
```

`A2` freezes rows above row 2, so the first row remains visible.

## 41. Merged cells have one real value cell

When a range is merged, only the top-left cell is the normal value-bearing cell. Other positions become merged-cell placeholders.

```python
from openpyxl import Workbook


workbook = Workbook()
worksheet = workbook.active
worksheet.merge_cells("A1:C1")
worksheet["A1"] = "Quarterly report"
print(worksheet["A1"].value)
```

```text
Quarterly report
```

Merged cells are presentation structure, not a substitute for normalized tabular data.

## 42. Insert and delete operations do not manage all dependencies

`insert_rows()`, `delete_rows()`, `insert_cols()`, and `delete_cols()` can shift cells.

The official documentation notes that openpyxl does not manage every dependency that may reference the affected cells, such as formulas, tables, or charts.

A structural edit can therefore require application-specific repair logic.

## 43. `move_range()` can translate some formulas, not every reference

`move_range(..., translate=True)` can translate formulas inside the moved cells.

However, references to those cells from other cells or defined names are not automatically updated by that operation.

Do not equate “cells moved” with “workbook semantics repaired.”

## 44. Worksheet tables add Excel table semantics

A worksheet table is more than a colored range. It has a name and a defined cell reference:

```python
from openpyxl import Workbook
from openpyxl.worksheet.table import Table


workbook = Workbook()
worksheet = workbook.active
worksheet.append(["item", "amount"])
worksheet.append(["A", 10])
worksheet.append(["B", 20])
table = Table(displayName="SalesTable", ref="A1:B3")
worksheet.add_table(table)
print(list(worksheet.tables.keys()))
```

```text
['SalesTable']
```

Tables are useful when downstream Excel users expect structured references and table-aware formatting.

## 45. Table names and headers are contracts

Table display names must be valid and unique within the relevant workbook namespace. The openpyxl table documentation also requires table column headings to be strings.

Validate headers before constructing a table rather than relying on Excel to repair malformed output later.

## 46. Filters describe workbook behavior; they do not filter Python data

Auto filters can be configured so spreadsheet applications know which rows should be shown under filter criteria.

That is different from filtering records in Python before writing them.

If a report must physically contain only approved rows, filter the Python data first. If users need interactive filtering inside Excel, configure an Excel table or auto filter as presentation behavior.

## 47. Data validation rules are written, not enforced by openpyxl

The official validation documentation is explicit: validators are not enforced or evaluated by openpyxl.

```python
from openpyxl import Workbook
from openpyxl.worksheet.datavalidation import DataValidation


workbook = Workbook()
worksheet = workbook.active
validation = DataValidation(type="list", formula1='"open,closed"')
worksheet.add_data_validation(validation)
validation.add("A2:A20")
print(len(worksheet.data_validations.dataValidation))
```

```text
1
```

The rule becomes workbook metadata that Excel or another compatible application can enforce interactively.

## 48. Conditional formatting is also workbook behavior

Conditional formatting rules tell a spreadsheet application how to format cells when conditions are met.

Do not use conditional formatting as a hidden replacement for data validation. A red cell may communicate an error to a human, but your Python program should still validate critical input explicitly.

## 49. Charts reference worksheet data

`openpyxl.chart` can build charts from worksheet ranges. A typical workflow creates a chart, defines `Reference` objects for data and categories, and anchors the chart on a worksheet.

Charts are presentation objects over worksheet data. Test the underlying numbers separately from the chart layout.

## 50. Images introduce an optional Pillow dependency

The image API can insert raster images into worksheets, but image handling depends on Pillow.

Because this chapter's executable contract does not require images, Pillow is not added merely for a decorative example.

Add optional dependencies only when the project actually needs the feature.

## 51. Comments and hyperlinks are cell metadata

Cells can contain comments and hyperlinks in addition to values and styles.

Use these features when they provide useful human context, but keep essential machine-readable information in normal cells or structured data rather than hiding it in comments.

## 52. Defined names can represent workbook-level references

Excel defined names can point to cells, ranges, constants, or formulas and may have workbook or worksheet scope.

They are useful for workbook contracts, but they also create another dependency layer when cells are moved or sheets are renamed.

Inspect defined names before performing structural edits on complex templates.

## 53. Worksheet protection is not encryption

Cell and worksheet protection controls spreadsheet editing behavior. It is not a substitute for encrypting sensitive files or enforcing server-side authorization.

Treat workbook protection as a user-interface constraint, not a security boundary.

## 54. Print settings are part of the workbook product

Page orientation, margins, print areas, print titles, and scaling can matter when an `.xlsx` file is intended to become a PDF or printed report.

For a data-exchange workbook, these settings may be irrelevant. For a human-facing report, they may be part of the acceptance criteria.

## 55. Understand the important `load_workbook()` flags

Common flags include:

```text
read_only=True  -> lazy, lower-memory reading
data_only=True  -> cached formula results instead of formula text
keep_vba=True   -> preserve VBA content when possible
keep_links=True -> preserve cached external-link data
rich_text=True  -> preserve rich text formatting in cells
```

Each flag changes the contract. Do not turn them on merely because they sound safer or more complete.

## 56. `keep_vba=True` preserves VBA; it does not let Python edit it

The official tutorial says VBA elements can be preserved but are still not editable through openpyxl.

If a macro-enabled `.xlsm` workbook must round-trip with VBA intact, use the matching extension and `keep_vba=True`, then test the actual artifact.

Preservation is not execution, inspection, or modification.

## 57. Template and extension mismatches can corrupt expectations

Workbook type, filename extension, and VBA/template settings should agree.

Saving a macro-enabled workbook under the wrong extension or ignoring its VBA contract can produce a file that Excel rejects or that silently loses functionality.

Treat the source and destination workbook types explicitly.

## 58. Untrusted workbooks are a security boundary

An `.xlsx` file is a ZIP package containing XML and related resources. PyPI's openpyxl project page warns that openpyxl does not guard by default against XML quadratic-blowup or billion-laughs attacks and recommends `defusedxml` for protection.

For trusted, repository-generated examples this is not required. For services that accept arbitrary uploaded workbooks, threat modeling and hardened XML parsing belong in the design.

## 59. Invalid files should fail visibly

`load_workbook()` may reject malformed or non-conforming OOXML files.

Catch exceptions only when you can add useful context, then preserve the failure:

```python
from pathlib import Path
from zipfile import BadZipFile

from openpyxl import load_workbook
from openpyxl.utils.exceptions import InvalidFileException


def read_sheet_names(path: Path) -> list[str]:
    try:
        workbook = load_workbook(path, read_only=True)
    except (BadZipFile, InvalidFileException, OSError) as exc:
        raise RuntimeError(f"Could not open workbook: {path.name}") from exc

    try:
        return workbook.sheetnames
    finally:
        workbook.close()
```

Do not convert every workbook error into an empty report.

## 60. Prefer output validation over “save succeeded”

A successful `save()` proves that bytes were written. It does not prove that the workbook satisfies your business or presentation contract.

Useful post-save checks include:

```text
file exists
expected sheet names exist
required cells contain expected values or formulas
expected table names exist
expected validations exist
critical number formats/styles are present
workbook reopens successfully
```

For important templates, open the generated artifact in the target spreadsheet application during acceptance testing too.

## 61. Example: create a workbook and preserve a formula

[`examples/workbook_basics.py`](examples/workbook_basics.py) creates a temporary workbook, adds tabular rows and formulas, saves it, reloads it with formulas visible, and verifies the workbook structure.

Expected output:

```text
sheet: Summary
rows: 3
formula: =B2*C2
```

The example tests what openpyxl actually owns: formula text and workbook structure, not formula calculation.

## 62. Example: stream rows from a workbook

[`examples/load_and_iterate.py`](examples/load_and_iterate.py) writes a small workbook, reopens it with `read_only=True`, iterates values, and computes a Python total.

Expected output:

```text
orders: 3
total: 100.00
```

This deliberately separates workbook reading from business calculation.

## 63. Example: create a styled report

[`examples/styled_report.py`](examples/styled_report.py) applies a reusable header treatment, number format, freeze pane, and column widths, then reloads the workbook to verify the persisted metadata.

Expected output:

```text
header bold: True
number format: #,##0.00
freeze panes: A2
```

A deterministic workbook test can inspect metadata without launching Excel.

## 64. Example: tables and validation rules

[`examples/table_and_validation.py`](examples/table_and_validation.py) creates an Excel table and a list validation rule, saves the workbook, reloads it, and verifies that both structures exist.

Expected output:

```text
tables: ['CatalogTable']
validations: 1
```

Remember that the validation rule is stored, not executed, by openpyxl.

## 65. Example: write-only export

[`examples/write_only_export.py`](examples/write_only_export.py) streams rows into a write-only workbook, saves once, then reopens the result in read-only mode for verification.

Expected output:

```text
rows: 3
sum: 60
```

This models the lifecycle of a large sequential export without relying on a large fixture file.

## 66. Common mistakes, decision guide, exercise, and references

Avoid these mistakes:

- using `openpyxl` for heavy table analytics that belong in `pandas`;
- expecting `.xls` or `.xlsb` support from an `.xlsx` library;
- assuming `data_only=True` recalculates formulas;
- overwriting a complex source workbook before verifying round-trip fidelity;
- treating worksheet dimensions as proof of valid data;
- using normal mode for huge streaming workloads without considering memory;
- forgetting to close read-only workbooks;
- saving a write-only workbook more than once;
- mutating assigned styles in place;
- creating thousands of nearly identical style variants;
- confusing Excel number formats with stored numeric values;
- assuming row/column insertion repairs formulas, tables, charts, and defined names automatically;
- expecting data validation to be enforced by openpyxl;
- treating worksheet protection as security;
- preserving VBA without testing the `.xlsm` artifact;
- accepting untrusted workbooks without an XML security strategy;
- considering `save()` alone sufficient verification.

### Decision table

| Requirement | Prefer |
|---|---|
| data filtering/grouping/joining | `pandas` |
| raw CSV exchange | `csv` or `pandas` |
| create/edit `.xlsx` workbook structure | `openpyxl` |
| arbitrary cell edits | normal workbook |
| large sequential read | `read_only=True` |
| large sequential write | `Workbook(write_only=True)` |
| formula text | normal load / `data_only=False` |
| cached formula value | `data_only=True` |
| preserve VBA container | `keep_vba=True` + `.xlsm` contract |
| repeated formatting | reused style objects / `NamedStyle` |
| interactive Excel validation | `DataValidation` |
| machine validation | Python validation before writing |

### Quick reference

```text
from openpyxl import Workbook, load_workbook

wb = Workbook()
ws = wb.active
ws = wb["SheetName"]
wb.create_sheet("Details")

ws["A1"] = "value"
ws.cell(row=1, column=1, value="value")
ws.append([...])
ws.iter_rows(values_only=True)

wb.save(path)
wb = load_workbook(path)
wb = load_workbook(path, read_only=True, data_only=True)
wb.close()

ws.freeze_panes = "A2"
ws.column_dimensions["A"].width = 20
ws["B2"].number_format = "#,##0.00"

ws.merge_cells("A1:C1")
ws.unmerge_cells("A1:C1")

ws.add_table(...)
ws.add_data_validation(...)
```

### Design checklist

Before accepting workbook automation, ask:

- What workbook formats are allowed?
- Is the file trusted or user-supplied?
- Must unsupported workbook artifacts survive a round trip?
- Is the source allowed to be overwritten?
- Which sheets, cells, tables, and names form the contract?
- Do formulas need formula text or calculated values?
- Who is responsible for calculation?
- Are cached formula values fresh enough?
- Is normal, read-only, or write-only mode appropriate?
- Are workbook resources closed?
- Are styles reused intentionally?
- Are number formats separated from stored values?
- Can structural edits break references?
- Are validation rules merely UI behavior or real business validation?
- Does VBA need preservation?
- Does the output reopen successfully?
- Are key workbook structures verified after saving?

### Exercise

Build a fictional monthly operations workbook:

1. Create an `.xlsx` file with `Summary` and `Transactions` sheets.
2. Add a header row and at least ten fictional transaction rows.
3. Use explicit Python `date` or `datetime` values for dates.
4. Add an Excel formula to the summary sheet.
5. Explain why your test should verify the formula text rather than expect openpyxl to calculate it.
6. Format money cells with a number format.
7. Reuse a header style instead of creating unrelated formatting per cell.
8. Freeze the transaction header row.
9. Create an Excel table over the transaction data.
10. Add a list validation rule to a status column.
11. Save to a new path.
12. Reopen the workbook and verify required sheet names, formula text, table name, validation count, and one critical style.
13. Add a read-only inspection function that computes a Python total from the saved rows.
14. Make failures visible with useful exception context.

Extension challenges:

- create a chart from the summary values;
- add a defined name and inspect it after reload;
- compare normal and write-only export designs;
- process a pandas `DataFrame` and write only the presentation layer with openpyxl;
- design a safe `.xlsm` round-trip test using `keep_vba=True` without attempting to edit the VBA project.

### Connections to earlier concepts

`openpyxl` builds directly on earlier material:

- **functions and modules:** isolate workbook generation and validation steps;
- **exceptions:** report malformed or incompatible workbook input;
- **`pathlib`:** model workbook source and destination paths;
- **dates:** store Python temporal values with spreadsheet number formats;
- **`decimal`:** decide explicitly how exact monetary domain values cross into Excel numeric cells;
- **`logging`:** record workbook paths, sheet names, row counts, and failures without hiding exceptions;
- **`os` and `shutil`:** discover, stage, copy, and archive workbook files safely;
- **`pandas`:** transform tabular data before openpyxl builds the final Excel presentation.

### Primary references

- [openpyxl documentation](https://openpyxl.readthedocs.io/)
- [openpyxl tutorial](https://openpyxl.readthedocs.io/en/stable/tutorial.html)
- [Optimised Modes](https://openpyxl.readthedocs.io/en/stable/optimized.html)
- [Working with styles](https://openpyxl.readthedocs.io/en/stable/styles.html)
- [Worksheet tables](https://openpyxl.readthedocs.io/en/stable/worksheet_tables.html)
- [Data validation](https://openpyxl.readthedocs.io/en/stable/validation.html)
- [Worksheet editing](https://openpyxl.readthedocs.io/en/stable/editing_worksheets.html)
- [openpyxl on PyPI](https://pypi.org/project/openpyxl/)

At the time this chapter was prepared, PyPI listed openpyxl 3.1.5 as the latest stable release. The curriculum targets the 3.1.x series rather than relying on an unbounded future version.

## 67. Next chapter

Phase 9 now has two practical data/workbook layers:

```text
pandas   -> transform tabular data
openpyxl -> construct and maintain Excel workbooks
```

Continue with **[`requests`: Consuming HTTP APIs](../03-requests/README.md)**, where the boundary moves from local files to HTTP services and APIs.

Before moving on, practice by generating workbooks that you can inspect manually and validate automatically. Spreadsheet automation becomes reliable when both the data contract and the workbook contract are explicit.
