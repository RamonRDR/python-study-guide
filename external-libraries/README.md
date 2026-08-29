<div align="center">

# Phase 9: External Libraries

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Back to repository](../README.md)

Phase 9 introduces third-party packages after the Python language and standard-library foundations are complete.

External libraries add a new engineering responsibility: **dependency contracts**. A program now depends not only on Python, but also on package versions, installation state, release notes, and compatibility boundaries.

## Status

> ✅ **Complete**

## Learning path

1. ✅ [`pandas`: Working with Tabular Data](01-pandas/README.md)
2. ✅ [`openpyxl`: Automating Excel Workbooks](02-openpyxl/README.md)
3. ✅ [`requests`: Consuming HTTP APIs](03-requests/README.md)
4. ✅ [`pytest`: Engineering Automated Tests](04-pytest/README.md)

## Dependency contract

Published executable examples from this phase use the dependencies declared in [`requirements-external.txt`](../requirements-external.txt). Repository CI installs that file before executing approved external-library examples.

The published contracts target **pandas 3.0.x**, **openpyxl 3.1.x**, **Requests 2.34.x**, and **pytest 9.1.x**. pandas 3.0 supports Python 3.11+, PyPI declares Python 3.8+ for openpyxl 3.1.5, and Requests 2.34.2 plus pytest 9.1.1 require Python 3.10+. This repository validates the examples on Python 3.13.

## What this phase established

Phase 9 moved from the Python standard library into four third-party engineering boundaries: tabular-data transformation, Excel workbook automation, HTTP/API clients, and automated testing. Each chapter treats the library as a versioned dependency with explicit behavior, safety, and validation contracts.

The next phase is **Phase 10: Practical Projects**.
