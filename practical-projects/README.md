<div align="center">

# Practical Projects

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Back to repository home](../README.md)

Phase 10 combines concepts from the previous phases into complete, testable workflows. Projects emphasize requirements, design decisions, implementation, validation, extension paths, and portfolio communication.

## Status

> 🚧 **In progress**

## Project path

1. ✅ [Expense Tracker](01-expense-tracker/README.md)
2. ✅ [Grade Calculator](02-grade-calculator/README.md)
3. ✅ [User Registration](03-user-registration/README.md)
4. ✅ [CSV Analyzer](04-csv-analyzer/README.md)
5. ✅ [Report Generator](05-report-generator/README.md)
6. 🚧 [File Organizer](06-file-organizer/README.md)
7. ⏳ Fictional Reconciliation Workflow
8. ⏳ Simulated Automation Flow

## Project contract

Each project should include:

- explicit requirements;
- design notes and trade-offs;
- working implementation;
- deterministic demonstration when appropriate;
- automated tests for important behavior;
- explanation of failure paths;
- extension challenges;
- portfolio discussion.

Project 01 establishes the integration pattern with validated monetary records and persistence. Project 02 extends it with configurable grading policies, exact weighted aggregation, explicit partial/final states, structured reporting, and boundary-focused pytest coverage. Project 03 adds canonical identity-like data, duplicate prevention, secondary lookup indexes, safe indexed-field updates, and explicit user lifecycle transitions without introducing authentication. Project 04 adds exact CSV schemas, typed conversion, structural-versus-row failure handling, partial-success parsing, duplicate row identifiers, deterministic filtering, and aggregation without hiding ingestion behavior behind pandas. Project 05 turns validated operational records into deterministic reporting artifacts with explicit date windows, exact summary metrics, TXT/Markdown renderers, and UTF-8 file output while keeping aggregation, presentation, and persistence separate. Project 06 adds shallow filesystem discovery, suffix classification, immutable move planning, explicit collision policies, symlink boundaries, execution-time revalidation, and exact no-replace destination protection before files are organized into category folders.
