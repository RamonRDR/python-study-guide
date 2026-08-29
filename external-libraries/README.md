<div align="center">

# Phase 9: External Libraries

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Back to repository](../README.md)

Phase 9 introduces third-party packages after the Python language and standard-library foundations are complete.

External libraries add a new engineering responsibility: **dependency contracts**. A program now depends not only on Python, but also on package versions, installation state, release notes, and compatibility boundaries.

## Status

> 🚧 **In progress**

## Learning path

1. ✅ [`pandas`: Working with Tabular Data](01-pandas/README.md)
2. ⏳ `openpyxl`: Excel workbook automation
3. ⏳ `requests`: HTTP clients and API consumption
4. ⏳ `pytest`: automated testing

## Dependency contract

Published executable examples from this phase use the dependencies declared in [`requirements-external.txt`](../requirements-external.txt). Repository CI installs that file before executing approved external-library examples.

The pandas chapter targets **pandas 3.0.x**. pandas 3.0 supports Python 3.11+, while this repository continues to validate examples on Python 3.13.

## Why this phase comes now

The earlier phases established collections, functions, errors, files, modules, CSV/JSON, dates, paths, logging, iteration, decimal arithmetic, and filesystem contracts. External libraries should build on those skills rather than replace them.

The next planned chapter is **`openpyxl`**.
