<div align="center">

# Working with Tabular Data Using `pandas`

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Back to External Libraries](../README.md) · [← Previous phase: `os` + `shutil`](../../standard-library/09-os-shutil/README.md)

Phase 9 begins where the standard library stops: adding third-party packages with their own release cycles, dependency contracts, and domain-specific abstractions.

`pandas` is the first external library because it connects directly to concepts already studied: lists, dictionaries, CSV, JSON, dates, files, functions, exceptions, paths, and data validation. The new challenge is not merely learning methods. It is learning to preserve **table semantics** while transformations become more expressive.

This chapter targets **pandas 3.0.x** and was researched against the official pandas **3.0.5** documentation. pandas 3.0 supports Python 3.11 and newer.

**Estimated study time:** 240–330 minutes.

## Learning goals

By the end of this chapter, you should be able to:

- explain when pandas is a better fit than built-in collections;
- create and inspect `Series` and `DataFrame` objects;
- reason about indexes, labels, alignment, columns, and dtypes;
- select rows and columns with brackets, `.loc`, and `.iloc`;
- build boolean masks and update rows safely;
- understand pandas 3.0 Copy-on-Write and why chained assignment is not valid;
- handle missing values with an explicit policy;
- parse numeric, string, and datetime columns deliberately;
- aggregate with `groupby()`, `agg()`, and `transform()`;
- combine tables with validated `merge()` and `concat()`;
- reshape data with `pivot_table()` and `melt()`;
- load and save CSV data with explicit schema decisions;
- prefer vectorized operations when they express the problem;
- recognize when `apply()` and row iteration are poor defaults;
- build deterministic, reviewable tabular-data pipelines.

## 1. Why `pandas` exists

`pandas` is a third-party library for labeled and tabular data. It is especially useful when data has rows, columns, labels, missing values, mixed column types, or needs filtering, grouping, joining, reshaping, and file-based input/output.

It does not replace Python collections. A list or dictionary is often better for small application state. `pandas` becomes attractive when the problem is primarily a data table and operations apply to columns or groups of rows.

## 2. External libraries introduce dependency contracts

Unlike the standard library, pandas must be installed into the Python environment that will run the code. The repository declares executable Phase 9 dependencies in `requirements-external.txt`.

A dependency contract answers questions such as:

```text
Which package is required?
Which versions are supported by the chapter?
Which Python versions are supported by that package?
How does CI reproduce the same environment?
Which behaviors changed between major versions?
```

This chapter deliberately targets pandas 3.0.x instead of pretending every historical pandas version behaves the same.

## 3. Install pandas in an isolated environment

A virtual environment keeps project dependencies separate from unrelated Python installations.

```bash
python -m venv .venv
```

Activate it according to your operating system, then install the repository dependency contract:

```bash
python -m pip install -r requirements-external.txt
```

The official pandas installation documentation also supports direct installation with `pip install pandas` and installation through conda-forge. A project dependency file is preferable here because it makes the study guide's executable contract reproducible.

## 4. Import pandas with the conventional alias

The pandas documentation and community convention use `pd`:

```python
import pandas as pd
```

Following the convention makes examples easier to compare with official documentation and other projects.

## 5. `Series` models one labeled dimension

A `Series` is a one-dimensional labeled data structure. It combines values with an index. A DataFrame column is commonly exposed as a `Series`.

```python
import pandas as pd


scores = pd.Series([8.5, 9.0, 7.5], index=["A", "B", "C"])
print(scores.loc["B"])
```

```text
9.0
```

A `Series` is not simply a list with more methods. Labels participate in selection and alignment.

## 6. `DataFrame` models a labeled table

A `DataFrame` is a two-dimensional table with labeled rows and columns. Different columns may have different dtypes, which makes it suitable for many spreadsheet-, SQL-, and CSV-like datasets.

```python
import pandas as pd


people = pd.DataFrame(
    {
        "name": ["Ana", "Bruno"],
        "age": [28, 34],
        "active": [True, False],
    }
)
print(people.shape)
```

```text
(2, 3)
```

A dictionary of equally sized sequences is one of the clearest constructors for small examples. Dictionary keys become column labels.

## 7. The index is part of the data model

The index labels rows. The default `RangeIndex` is often perfectly adequate. Use a meaningful custom index only when row labels genuinely participate in selection, alignment, or identity.

```python
import pandas as pd


temperatures = pd.Series([21.5, 19.0], index=["morning", "evening"])
print(temperatures.index.tolist())
```

```text
['morning', 'evening']
```

Do not convert every business identifier into an index automatically. A normal column is often easier to validate, merge, export, and explain.

## 8. Label alignment is powerful and can surprise you

When pandas combines labeled objects, it generally aligns values by index labels rather than blindly by physical position.

```python
import pandas as pd


left = pd.Series([10, 20], index=["a", "b"])
right = pd.Series([1, 2], index=["b", "c"])
print((left + right).to_dict())
```

The shared label `b` receives a value from both objects. Labels present on only one side become missing in the result.

Treat the index as data, not decoration. Unexpected labels can change arithmetic, joins, assignments, and comparisons.

## 9. Inspect columns and dtypes early

A reliable data workflow inspects what was loaded before transforming it. `columns` reveals labels and `dtypes` reveals the dtype chosen for each column.

```python
import pandas as pd


table = pd.DataFrame({"label": ["x", "y"], "count": [1, 2]})
print(table.columns.tolist())
print(table.dtypes.astype(str).to_dict())
```

pandas 3.0 changed an important default: columns containing only strings are inferred as the dedicated `str` dtype instead of the historical generic `object` dtype.

That is one reason this chapter states its pandas version explicitly.

## 10. `shape`, `size`, and `ndim` answer different questions

```python
import pandas as pd


table = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
print(table.shape, table.size, table.ndim)
```

```text
(3, 2) 6 2
```

- `shape` returns `(rows, columns)`;
- `size` returns the number of cells;
- `ndim` returns the number of dimensions.

These are structural facts, not validation by themselves.

## 11. Previewing data is useful but not validation

`head()` and `tail()` are quick inspection tools. `sample()` can also reveal patterns away from the first rows, but use `random_state` when reproducible output matters.

```python
import pandas as pd


table = pd.DataFrame({"value": [10, 20, 30, 40]})
print(table.sample(2, random_state=7)["value"].tolist())
```

A preview does not prove that required columns exist, dtypes are correct, identifiers are unique, or values fall inside allowed ranges.

## 12. `info()` and `describe()` answer different inspection questions

`DataFrame.info()` summarizes row count, column names, non-null counts, dtypes, and approximate memory use. It is useful for human inspection.

`describe()` summarizes statistics such as count, mean, spread, and extrema for appropriate columns.

```python
import pandas as pd


values = pd.DataFrame({"amount": [10.0, 20.0, 30.0]})
print(values["amount"].describe()[["count", "mean", "max"]].to_dict())
```

Neither function understands the business meaning of the data. A negative amount may be mathematically valid but invalid for a particular dataset. An identifier may be numeric-looking but meaningless to average.

## 13. Select one column with brackets

`df["column"]` returns a `Series`.

```python
import pandas as pd


table = pd.DataFrame({"unit price": [10.0, 12.5]})
prices = table["unit price"]
print(type(prices).__name__)
```

```text
Series
```

Prefer bracket syntax over attribute access such as `df.column`. Column names may contain spaces, conflict with DataFrame attributes, or be chosen dynamically.

## 14. Select multiple columns with a list

Passing a list of column labels returns a DataFrame and preserves the requested column order.

```python
import pandas as pd


table = pd.DataFrame({"a": [1], "b": [2], "c": [3]})
subset = table[["c", "a"]]
print(subset.columns.tolist())
```

```text
['c', 'a']
```

This distinction matters: a string selects one column as `Series`; a list of strings selects a table-shaped `DataFrame`.

## 15. Use `.loc` for label-based selection

`.loc` selects by labels and boolean conditions.

```python
import pandas as pd


table = pd.DataFrame({"status": ["new", "done"], "value": [5, 8]}, index=["a", "b"])
print(table.loc["b", "value"])
```

```text
8
```

`.loc` is also the preferred tool for conditional assignment because target rows and columns can be expressed in one operation.

## 16. Use `.iloc` for positional selection

`.iloc` selects by integer position, independent of index labels.

```python
import pandas as pd


table = pd.DataFrame({"name": ["first", "second", "third"]}, index=[10, 20, 30])
print(table.iloc[1, 0])
```

```text
second
```

Use `.iloc` when position itself is meaningful. Do not use it merely because label-based selection feels unfamiliar.

## 17. Label slices and positional slices have different boundaries

With `.loc`, a label slice includes the stop label when it exists. With `.iloc`, slicing follows normal Python positional slicing and excludes the stop position.

```python
import pandas as pd


table = pd.DataFrame({"value": [10, 20, 30]}, index=["a", "b", "c"])
print(table.loc["a":"b", "value"].tolist())
print(table.iloc[0:2, 0].tolist())
```

```text
[10, 20]
[10, 20]
```

The two examples happen to return the same values for different reasons. Keep the two mental models separate.

## 18. Boolean masks filter rows

A comparison against a `Series` produces a boolean `Series`. Using that mask with `.loc` keeps rows where the condition is true.

```python
import pandas as pd


orders = pd.DataFrame({"amount": [50, 120, 80]})
mask = orders["amount"] >= 80
print(orders.loc[mask, "amount"].tolist())
```

```text
[120, 80]
```

Masks are one of the most important bridges between Python boolean logic and table-oriented operations.

## 19. Combine masks with `&`, `|`, and `~`

Use element-wise boolean operators for `Series` conditions and parenthesize each comparison.

```python
import pandas as pd


orders = pd.DataFrame(
    {"status": ["paid", "paid", "pending"], "amount": [50, 150, 200]}
)
mask = (orders["status"] == "paid") & (orders["amount"] >= 100)
print(orders.loc[mask, "amount"].tolist())
```

```text
[150]
```

Python's scalar `and` and `or` do not express row-by-row logic for a pandas `Series`.

## 20. Assign through the object you intend to change

When updating a DataFrame, express the row selector and destination column in one `.loc` operation.

```python
import pandas as pd


orders = pd.DataFrame({"amount": [50, 150], "priority": ["normal", "normal"]})
orders.loc[orders["amount"] >= 100, "priority"] = "high"
print(orders["priority"].tolist())
```

```text
['normal', 'high']
```

This pattern is explicit and compatible with pandas 3.0 Copy-on-Write semantics.

## 21. Copy-on-Write is the pandas 3.0 rule

In pandas 3.0, objects derived through indexing or methods behave like copies from the user's perspective. Mutating a derived object does not mutate the original object.

```python
import pandas as pd


original = pd.DataFrame({"value": [1, 2, 3]})
subset = original["value"]
subset.iloc[0] = 99

print(original["value"].tolist())
print(subset.tolist())
```

```text
[1, 2, 3]
[99, 2, 3]
```

Under the hood, pandas may share memory until a write requires a copy. The important contract for application code is the observable behavior.

## 22. Chained assignment is not a valid update strategy

Code such as this uses multiple indexing steps:

```text
df["value"][mask] = 10
```

In pandas 3.0, chained assignment does not update the original DataFrame. The old ambiguity that produced `SettingWithCopyWarning` has been replaced by a simpler rule: modify the object itself in one operation.

```python
import pandas as pd


table = pd.DataFrame({"value": [1, 2, 3]})
table.loc[table["value"] >= 2, "value"] = 10
print(table["value"].tolist())
```

```text
[1, 10, 10]
```

This is a major migration point from older pandas material found on the internet.

## 23. Create derived columns with vectorized expressions

Column expressions operate over whole `Series` objects and are usually clearer than writing a Python loop for every row.

```python
import pandas as pd


sales = pd.DataFrame({"units": [2, 3], "unit_price": [10.0, 12.5]})
sales["total"] = sales["units"] * sales["unit_price"]
print(sales["total"].tolist())
```

```text
[20.0, 37.5]
```

This is one of the central pandas habits: express a transformation in terms of columns when the rule itself is column-oriented.

## 24. `assign()` is useful in method chains

`assign()` returns a DataFrame with added or replaced columns.

```python
import pandas as pd


sales = pd.DataFrame({"units": [2, 3], "price": [5.0, 8.0]})
result = sales.assign(total=lambda frame: frame["units"] * frame["price"])
print(result["total"].tolist())
```

```text
[10.0, 24.0]
```

Use it when a pipeline becomes easier to read by keeping transformations chained. Direct assignment remains perfectly valid when it is clearer.

## 25. Rename, drop, and sort with intent

`rename()` can normalize awkward external column names. `drop()` removes rows or columns. `sort_values()` and `sort_index()` make ordering explicit.

```python
import pandas as pd


table = pd.DataFrame({"Order Amount": [20, 10], "temporary_note": ["b", "a"]})
clean = (
    table.rename(columns={"Order Amount": "amount"})
    .drop(columns=["temporary_note"])
    .sort_values("amount")
)
print(clean["amount"].tolist())
```

```text
[10, 20]
```

A dropped field may be impossible to reconstruct later. A sort may be required for deterministic reports. These operations encode policy, not merely formatting.

## 26. Missing data needs an explicit policy

Missing values can mean unknown, not applicable, not collected, invalid, delayed, or intentionally blank. Those meanings are not interchangeable.

Before calling `dropna()` or `fillna()`, decide what absence means for each relevant column.

```python
import pandas as pd


table = pd.DataFrame({"value": [1.0, None, 3.0], "label": ["a", "b", None]})
print(table.isna().sum().to_dict())
```

```text
{'value': 1, 'label': 1}
```

Counting missing values is observation. Dropping or filling them is a transformation that requires a rule.

## 27. `dropna()` discards observations

`dropna()` is correct only when the affected observations are genuinely disposable under the data contract.

```python
import pandas as pd


table = pd.DataFrame({"id": [1, 2, 3], "amount": [10.0, None, 30.0]})
complete = table.dropna(subset=["amount"])
print(complete["id"].tolist())
```

```text
[1, 3]
```

Using `dropna()` with no subset can remove rows because of fields that were not important to the current operation.

## 28. `fillna()` inserts a chosen meaning

Replacing an unknown amount with zero asserts that zero is the correct interpretation.

```python
import pandas as pd


table = pd.DataFrame({"discount": [0.1, None, 0.2]})
filled = table["discount"].fillna(0.0)
print(filled.tolist())
```

```text
[0.1, 0.0, 0.2]
```

Document fill rules because they change the dataset, not just its appearance.

## 29. Dtypes are part of the schema

A column that looks numeric may have been loaded as text. A date may still be a string. An identifier may need to remain textual even when every value contains only digits.

Use `astype()` when values are already valid for the target dtype:

```python
import pandas as pd


table = pd.DataFrame({"units": ["1", "2", "3"]})
table["units"] = table["units"].astype("int64")
print(table["units"].sum())
```

```text
6
```

Choose types according to meaning and operations, not appearance alone.

## 30. `to_numeric()` makes parsing policy explicit

`pd.to_numeric()` is useful when numeric parsing may fail.

```python
import pandas as pd


raw = pd.Series(["10", "invalid", "30"])
parsed = pd.to_numeric(raw, errors="coerce")
print(parsed.isna().sum())
```

```text
1
```

`errors="coerce"` converts invalid entries into missing values. That is only safe when the workflow subsequently audits and handles the newly missing values.

## 31. String operations are vectorized under `.str`

The `.str` accessor applies string operations to a `Series`.

```python
import pandas as pd


names = pd.Series(["  Alpha ", "BETA  "])
normalized = names.str.strip().str.lower()
print(normalized.tolist())
```

```text
['alpha', 'beta']
```

Normalize text only when normalization matches the domain contract. Lowercasing identifiers or preserving/discarding whitespace can change meaning.

## 32. Parse datetimes before using datetime semantics

Use `pd.to_datetime()` when text should become actual datetime values.

```python
import pandas as pd


dates = pd.to_datetime(pd.Series(["2026-08-01", "2026-08-03"]), format="%Y-%m-%d")
print((dates.iloc[1] - dates.iloc[0]).days)
```

```text
2
```

The `.dt` accessor then exposes vectorized components:

```python
import pandas as pd


dates = pd.to_datetime(pd.Series(["2026-01-15", "2026-02-20"]))
print(dates.dt.month.tolist())
```

```text
[1, 2]
```

Ambiguous date formats should be controlled explicitly instead of guessed.

## 33. Duplicates require a definition

Two rows are duplicates only relative to chosen columns. `duplicated()` and `drop_duplicates()` accept `subset` so the workflow can express the actual uniqueness key.

```python
import pandas as pd


table = pd.DataFrame(
    {"id": [1, 1, 2], "note": ["first", "repeated", "other"]}
)
print(table.duplicated(subset=["id"]).tolist())
```

```text
[False, True, False]
```

Do not deduplicate entire rows when the real rule is uniqueness by an identifier.

## 34. Frequency and summary methods are compact diagnostics

`value_counts()` exposes category frequency. `nunique()` counts distinct non-missing values by default. Reductions such as `sum()`, `mean()`, `min()`, `max()`, and `count()` summarize columns.

```python
import pandas as pd


statuses = pd.Series(["paid", "pending", "paid", "paid"])
print(statuses.value_counts().sort_index().to_dict())
```

```text
{'paid': 3, 'pending': 1}
```

A frequency is evidence about the observed dataset, not proof that every observed category is allowed.

## 35. `groupby()` implements split-apply-combine

`groupby()` splits rows by one or more keys, applies aggregation or transformation, and combines results.

```python
import pandas as pd


sales = pd.DataFrame(
    {"category": ["A", "B", "A"], "amount": [10, 20, 30]}
)
summary = sales.groupby("category")["amount"].sum()
print(summary.to_dict())
```

```text
{'A': 40, 'B': 20}
```

Grouping is one of pandas' central tools because many analytical questions are really "calculate something per category, customer, date, region, or other key."

## 36. Named aggregation makes the output schema explicit

Named aggregation lets the output state both the source column and the operation.

```python
import pandas as pd


sales = pd.DataFrame(
    {"category": ["A", "A", "B"], "amount": [10.0, 30.0, 20.0]}
)
summary = sales.groupby("category", as_index=False).agg(
    total=("amount", "sum"),
    average=("amount", "mean"),
)
print(summary.to_dict(orient="records"))
```

```text
[{'category': 'A', 'total': 40.0, 'average': 20.0}, {'category': 'B', 'total': 20.0, 'average': 20.0}]
```

A stable output schema makes later validation, export, and testing easier.

## 37. `transform()` keeps results aligned to original rows

Unlike a normal aggregation, `transform()` returns a result aligned to the original row index.

```python
import pandas as pd


sales = pd.DataFrame({"team": ["A", "A", "B"], "score": [10, 20, 30]})
sales["team_total"] = sales.groupby("team")["score"].transform("sum")
print(sales["team_total"].tolist())
```

```text
[30, 30, 30]
```

This is useful when a group-level statistic must remain beside each observation.

## 38. `merge()` combines tables by keys

`merge()` is pandas' database-style join operation.

```python
import pandas as pd


orders = pd.DataFrame({"customer_id": [1, 2], "amount": [10, 20]})
customers = pd.DataFrame({"customer_id": [1, 2], "name": ["A", "B"]})
result = orders.merge(customers, on="customer_id", how="left")
print(result["name"].tolist())
```

```text
['A', 'B']
```

A merge that runs without error can still be logically wrong if keys are duplicated unexpectedly.

## 39. Validate merge cardinality

The `validate` argument can assert relationships such as `one_to_one`, `one_to_many`, `many_to_one`, or `many_to_many`.

```python
import pandas as pd


orders = pd.DataFrame({"customer_id": [1, 1], "amount": [10, 20]})
customers = pd.DataFrame({"customer_id": [1], "name": ["A"]})
result = orders.merge(
    customers,
    on="customer_id",
    how="left",
    validate="many_to_one",
)
print(len(result))
```

```text
2
```

When cardinality is part of the data contract, validating it turns accidental key duplication into a visible failure instead of silent row multiplication.

## 40. `concat()` stacks compatible objects

`pd.concat()` combines pandas objects along an axis. Concatenating rows is common when multiple files share the same schema.

```python
import pandas as pd


first = pd.DataFrame({"id": [1, 2]})
second = pd.DataFrame({"id": [3]})
combined = pd.concat([first, second], ignore_index=True)
print(combined["id"].tolist())
```

```text
[1, 2, 3]
```

After concatenation, decide whether original index labels must be preserved or reset.

## 41. `pivot_table()` summarizes into a matrix

A pivot table groups data across row and column dimensions and aggregates values.

```python
import pandas as pd


sales = pd.DataFrame(
    {
        "region": ["north", "north", "south"],
        "product": ["A", "B", "A"],
        "amount": [10, 20, 30],
    }
)
pivot = sales.pivot_table(
    index="region",
    columns="product",
    values="amount",
    aggfunc="sum",
    fill_value=0,
)
print(pivot.loc["north", "B"])
```

```text
20
```

Use a pivot table when the desired output is itself a summary matrix.

## 42. `melt()` converts wide data to long form

Long-form data often makes grouping and visualization easier.

```python
import pandas as pd


wide = pd.DataFrame({"item": ["A"], "jan": [10], "feb": [20]})
long = wide.melt(id_vars="item", var_name="month", value_name="amount")
print(long.to_dict(orient="records"))
```

```text
[{'item': 'A', 'month': 'jan', 'amount': 10}, {'item': 'A', 'month': 'feb', 'amount': 20}]
```

`melt()` is especially useful when repeated columns actually represent values of one conceptual variable.

## 43. `read_csv()` turns delimited text into a DataFrame

`pd.read_csv()` is one of pandas' most important I/O functions.

```python
from io import StringIO

import pandas as pd


source = StringIO("id,amount\n1,10.5\n2,20.0\n")
table = pd.read_csv(source)
print(table.shape)
```

```text
(2, 2)
```

pandas infers a schema unless you provide stronger instructions. Inference is convenience, not a business contract.

## 44. Control CSV parsing when the schema is known

Useful `read_csv()` arguments include `usecols`, `dtype`, `parse_dates`, `na_values`, `encoding`, and delimiter-related settings.

```python
from io import StringIO

import pandas as pd


source = StringIO("code,date,amount\n001,2026-08-01,10.5\n")
table = pd.read_csv(
    source,
    dtype={"code": "str"},
    parse_dates=["date"],
)
print(table.loc[0, "code"])
print(table.loc[0, "date"].year)
```

```text
001
2026
```

Giving pandas known schema information reduces accidental inference and documents expectations near the input boundary.

## 45. Identifiers often belong to string dtype

A code such as `00123` may look numeric but have no arithmetic meaning. Parsing it as an integer destroys leading zeros.

```python
import pandas as pd


codes = pd.Series(["001", "010"], dtype="str")
print(codes.tolist())
```

```text
['001', '010']
```

Model identifiers according to semantics, not the characters they happen to contain.

## 46. `to_csv()` should make index policy explicit

For ordinary tables whose index is only an internal row label, `index=False` prevents an extra index column from appearing on re-import.

```python
from io import StringIO

import pandas as pd


table = pd.DataFrame({"id": [1], "value": [10]})
buffer = StringIO()
table.to_csv(buffer, index=False)
print(buffer.getvalue().strip())
```

```text
id,value
1,10
```

If the index carries real information, export it intentionally instead of always disabling it.

## 47. Method chains make transformation order visible

A short chain can read like a pipeline: filter, derive, sort, group, export.

```python
import pandas as pd


orders = pd.DataFrame(
    {"status": ["paid", "pending", "paid"], "amount": [30, 50, 20]}
)
result = (
    orders.loc[orders["status"] == "paid"]
    .assign(taxed=lambda frame: frame["amount"] * 1.1)
    .sort_values("amount")
)
print(result["amount"].tolist())
```

```text
[20, 30]
```

Long chains can become difficult to debug. Break them into named stages when the intent stops being obvious.

## 48. Prefer vectorized operations to Python row loops

When a calculation can be expressed as `Series` arithmetic, comparisons, `.str`, `.dt`, or built-in reductions, prefer that form.

```python
import pandas as pd


table = pd.DataFrame({"quantity": [2, 3], "price": [4.0, 5.0]})
table["total"] = table["quantity"] * table["price"]
print(table["total"].tolist())
```

```text
[8.0, 15.0]
```

Vectorization communicates table intent and usually lets pandas/NumPy perform work more efficiently than repeated Python calls.

## 49. `apply()` is not automatically vectorization

`Series.apply()` and row-wise `DataFrame.apply()` can be useful for custom Python logic, but they may execute a Python function repeatedly.

Before using `apply()`, ask whether pandas already provides a native operation for the transformation.

Use `apply()` because custom logic is genuinely needed, not because it looks shorter than a loop.

## 50. Avoid `iterrows()` for ordinary transformations

Row iteration is sometimes necessary at external side-effect boundaries, but ordinary filtering, calculations, aggregations, and assignments normally have better column-oriented forms.

A row returned by `iterrows()` is a `Series` representation. Do not treat it as a mutable handle for updating the original DataFrame.

## 51. `.copy()` still has a deliberate role

Copy-on-Write means defensive copies are no longer required merely to silence the old `SettingWithCopyWarning`.

Use `.copy()` when an eager independent copy is itself part of the design or lifetime contract.

```python
import pandas as pd


original = pd.DataFrame({"value": [1, 2]})
independent = original.copy()
independent.loc[0, "value"] = 99
print(original["value"].tolist())
```

```text
[1, 2]
```

## 52. DataFrame errors should stay visible

Common failures include:

```text
KeyError
ValueError
pandas.errors.ParserError
pandas.errors.MergeError
```

Do not catch broad exceptions merely to keep a pipeline moving. A partially transformed table can be more dangerous than a visible failure.

Validation failures should stop a workflow when continuing would make the output untrustworthy.

## 53. Practical example: build a small sales table

```python
import pandas as pd


data = {
    "product": ["Notebook", "Keyboard", "Mouse"],
    "units": [2, 5, 8],
    "unit_price": [3500.0, 180.0, 95.0],
}

sales = pd.DataFrame(data)
sales["total"] = sales["units"] * sales["unit_price"]

print(f"shape: {sales.shape}")
print(f"columns: {sales.columns.tolist()}")
print(f"grand total: {sales['total'].sum():.2f}")
```

```text
shape: (3, 4)
columns: ['product', 'units', 'unit_price', 'total']
grand total: 8660.00
```

This example mirrors `examples/dataframe_basics.py` and demonstrates construction, inspection, a derived column, and aggregation.

## 54. Practical example: filter and assign safely

```python
import pandas as pd


orders = pd.DataFrame(
    {
        "order_id": [101, 102, 103, 104],
        "status": ["paid", "pending", "paid", "paid"],
        "amount": [120.0, 80.0, 250.0, 90.0],
    }
)

orders["priority"] = "normal"
orders.loc[
    (orders["status"] == "paid") & (orders["amount"] >= 200),
    "priority",
] = "high"

selected = orders.loc[
    orders["status"] == "paid",
    ["order_id", "priority"],
]
print(selected.to_dict(orient="records"))
```

```text
[{'order_id': 101, 'priority': 'normal'}, {'order_id': 103, 'priority': 'high'}, {'order_id': 104, 'priority': 'normal'}]
```

The update happens directly on `orders` through `.loc`, which is the pandas 3.0-safe pattern.

## 55. Practical example: grouped summary

```python
import pandas as pd


transactions = pd.DataFrame(
    {
        "category": ["books", "games", "books", "games", "office"],
        "amount": [40.0, 120.0, 35.0, 80.0, 25.0],
    }
)

summary = (
    transactions.groupby("category", as_index=False)
    .agg(
        total_amount=("amount", "sum"),
        transaction_count=("amount", "size"),
    )
    .sort_values("category")
)

print(summary.to_dict(orient="records"))
```

The named output columns form a stable summary schema. The final sort makes the example deterministic.

## 56. Practical example: validated merge

```python
import pandas as pd


orders = pd.DataFrame(
    {
        "order_id": [1, 2, 3],
        "customer_id": [10, 20, 10],
        "amount": [50.0, 80.0, 30.0],
    }
)
customers = pd.DataFrame(
    {
        "customer_id": [10, 20],
        "customer": ["Aster", "Boreal"],
    }
)

report = orders.merge(
    customers,
    on="customer_id",
    how="left",
    validate="many_to_one",
)
report = report[["order_id", "customer", "amount"]].sort_values("order_id")

print(report.to_dict(orient="records"))
```

`validate="many_to_one"` documents that many orders may reference one customer while the customer lookup must keep unique keys.

## 57. Practical example: deterministic CSV pipeline

```python
from pathlib import Path
from tempfile import TemporaryDirectory

import pandas as pd


with TemporaryDirectory() as temp_dir:
    workspace = Path(temp_dir)
    source = workspace / "orders.csv"
    destination = workspace / "paid_orders.csv"

    source.write_text(
        "order_id,date,status,amount\n"
        "1,2026-08-01,paid,120.50\n"
        "2,2026-08-02,pending,80.00\n"
        "3,2026-08-03,paid,250.00\n",
        encoding="utf-8",
    )

    orders = pd.read_csv(source, parse_dates=["date"])
    paid_orders = orders.loc[orders["status"] == "paid"].sort_values("order_id")
    paid_orders.to_csv(destination, index=False)

    print(f"rows: {len(paid_orders)}")
    print(f"total: {paid_orders['amount'].sum():.2f}")
    print(f"saved: {destination.name}")
```

```text
rows: 2
total: 370.50
saved: paid_orders.csv
```

The temporary directory keeps the example safe, `parse_dates` establishes datetime semantics at input, sorting stabilizes the result, and `index=False` keeps the CSV schema deliberate.

## 58. Common mistakes

Avoid these patterns:

- treating pandas as a replacement for every list or dictionary;
- trusting inferred dtypes without inspection;
- converting identifiers to numbers because they contain digits;
- using chained assignment instead of one `.loc` update;
- calling `dropna()` or `fillna()` without defining missing-value meaning;
- joining tables without checking key uniqueness or cardinality;
- relying on incidental row order;
- using `iterrows()` for calculations that have vectorized forms;
- using `apply()` before checking native pandas operations;
- exporting an internal index accidentally;
- swallowing parsing or merge errors and continuing with partial data;
- copying older pandas 1.x/2.x advice without checking pandas 3.0 behavior.

## 59. Decision table

| Requirement | Prefer |
|---|---|
| one labeled column | `Series` |
| labeled table | `DataFrame` |
| label-based selection | `.loc` |
| position-based selection | `.iloc` |
| conditional row filter | boolean mask + `.loc` |
| conditional update | one `.loc[...] = ...` assignment |
| parse numeric text | `pd.to_numeric()` |
| parse datetime text | `pd.to_datetime()` / `parse_dates` |
| inspect missing values | `isna()` |
| remove rows under a defined missing-data rule | `dropna()` |
| fill missing values under a defined rule | `fillna()` |
| aggregate by group | `groupby()` + `agg()` |
| group statistic beside each row | `groupby()` + `transform()` |
| database-style key join | `merge()` + `validate=` when known |
| stack compatible tables | `concat()` |
| summary matrix | `pivot_table()` |
| wide-to-long reshape | `melt()` |
| load CSV | `read_csv()` |
| save CSV | `to_csv(index=...)` |

## 60. Quick reference

```text
import pandas as pd

pd.Series(...)
pd.DataFrame(...)

df.shape
df.columns
df.dtypes
df.head()
df.info()
df.describe()

df["column"]
df[["column_a", "column_b"]]
df.loc[...]
df.iloc[...]

df.assign(...)
df.rename(...)
df.drop(...)
df.sort_values(...)
df.sort_index(...)

df.isna()
df.dropna(...)
df.fillna(...)
df.astype(...)
pd.to_numeric(...)
pd.to_datetime(...)

series.str...
series.dt...
series.value_counts()
series.nunique()

df.groupby(...)
df.agg(...)
df.transform(...)

df.merge(...)
pd.concat(...)
df.pivot_table(...)
df.melt(...)

pd.read_csv(...)
df.to_csv(...)
```

## 61. Design checklist

Before accepting a pandas transformation, ask:

- What is the expected input schema?
- Which columns are identifiers, numbers, text, dates, or categories?
- Is the index meaningful or merely positional?
- Could label alignment change the result?
- Are missing values allowed, and what do they mean?
- Is dtype inference acceptable at this boundary?
- Are conditional updates performed directly with `.loc`?
- Is merge cardinality known and validated?
- Can row order vary, and should the result be sorted?
- Is a vectorized operation available?
- Does `apply()` or row iteration genuinely require Python-level logic?
- Will an export accidentally include the index?
- Are failures visible rather than silently coerced?
- Is the pandas version contract documented?
- Does the code rely on pre-pandas-3.0 copy/view assumptions?

## 62. Exercise

Build a fictional order-analysis pipeline:

1. Create or load a CSV with `order_id`, `customer_id`, `date`, `status`, `category`, and `amount`.
2. Preserve identifiers as strings if leading zeros are allowed.
3. Parse `date` as datetime.
4. Validate required columns before transforming data.
5. Parse `amount` numerically and detect invalid entries.
6. Report missing values by column.
7. Keep only `paid` rows without a Python row loop.
8. Create a derived `month` column from the datetime values.
9. Produce a grouped summary by `category` with total, mean, and transaction count.
10. Join the orders to a fictional customer table and validate the expected merge cardinality.
11. Sort report output explicitly.
12. Save the final summary without exporting an accidental index.
13. Make expected data-quality failures visible rather than swallowing them.

Extension challenges:

- compare a vectorized solution with an `apply()` solution;
- build a wide pivot table;
- convert it back to long form with `melt()`;
- add tests for row counts, totals, key uniqueness, dtypes, and merge cardinality;
- document which transformations change the row count and why.

## 63. Connections to earlier Python concepts

`pandas` builds on concepts already studied:

- **lists and dictionaries:** constructors and result conversions;
- **functions:** reusable transformation steps;
- **boolean logic:** row masks;
- **exceptions:** visible I/O, conversion, and join failures;
- **files and context managers:** CSV and other data boundaries;
- **`pathlib`:** path objects work naturally with pandas I/O;
- **`datetime`:** pandas extends date/time work to columns;
- **CSV and JSON:** pandas adds a table-oriented layer over data formats;
- **`decimal`:** representation choices still matter; floating-point columns do not replace exact-decimal domain requirements;
- **`logging`:** operational pipelines should report useful context without hiding exceptions;
- **`os` and `shutil`:** filesystem discovery and movement often surround a pandas transformation pipeline.

## 64. References

Primary references used for this chapter:

- [pandas 3.0.5 documentation](https://pandas.pydata.org/docs/)
- [pandas User Guide](https://pandas.pydata.org/docs/user_guide/)
- [pandas package overview](https://pandas.pydata.org/docs/getting_started/overview.html)
- [Getting started tutorials](https://pandas.pydata.org/docs/getting_started/intro_tutorials/)
- [Copy-on-Write](https://pandas.pydata.org/docs/user_guide/copy_on_write.html)
- [pandas 3.0.0 release notes](https://pandas.pydata.org/docs/whatsnew/v3.0.0.html)

The official documentation identifies pandas 3.0.5 as the current stable documentation used for this chapter, and pandas 3.0 requires Python 3.11 or newer.

## 65. Next chapter

This chapter opens **Phase 9: External Libraries**.

The next planned library is **`openpyxl`**, focused on programmatic Excel workbook operations.

Before moving on, practice pandas with datasets small enough to inspect manually. A table library becomes useful only when you can still reason about what each transformation should do.
