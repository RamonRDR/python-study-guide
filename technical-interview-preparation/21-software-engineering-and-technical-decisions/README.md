# Software Engineering and Technical Decisions

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Previous](../20-transactions-indexes-and-sql-safety/README.md) · [Module index](../README.md) · [Next →](../22-technical-interview-question-bank/README.md)
<!-- /chapter-navigation:top -->

## Prerequisites

- [manual-programming-practices/02-specification-driven-development](../../manual-programming-practices/02-specification-driven-development/README.md)
- [manual-programming-practices/03-test-driven-development](../../manual-programming-practices/03-test-driven-development/README.md)
- [technical-interview-preparation/08-encapsulation-abstraction-and-solid](../../technical-interview-preparation/08-encapsulation-abstraction-and-solid/README.md)
- [technical-interview-preparation/20-transactions-indexes-and-sql-safety](../../technical-interview-preparation/20-transactions-indexes-and-sql-safety/README.md)

## Decisions start with a requirement

Separate functional behavior from quality attributes (latency, reliability, maintainability, security, cost). Clarify constraints and acceptance examples before coding. SDD turns needs into specification, plan, tasks and observable criteria; TDD tests a behavior first, observes failure, implements, then refactors under green tests. Do not claim Red was observed without running it. ADR records context, alternatives, decision and consequences. Prefer a small maintainable design over premature abstractions.

For a fictional progress report, the requirement is to count unique completed lesson IDs for a supplied learner. Empty completion history returns zero, invalid IDs fail, storage failure propagates. The shared example injects a callable that loads IDs, so domain logic is testable without a real database. It is a read-only reporting rule, not an authenticated API. Authorization belongs at the protected boundary. Unit tests use fake loaders; integration tests for a real repository would verify query and mapping against a real database.

## Trade-offs and operation

| Decision | Question to ask |
| --- | --- |
| Modular monolith vs services | Is independent scaling/deployment worth network and operational complexity? |
| Cache vs direct read | What staleness, invalidation and memory budget are acceptable? |
| Sync vs async | Is measured workload waiting on I/O, and are dependencies compatible? |
| SQL vs another storage model | Which integrity, query and access patterns dominate? |

Define a baseline and measurable success; do not infer speed from architecture labels. Use version control with focused changes, CI automated checks, review and a tested deployment/rollback plan. Separate configuration from code, never commit secrets, and use least privilege. Observability combines structured logs, metrics and traces to investigate real failures; record useful context without private data, watch latency/errors and distinguish symptoms from causes. Deploy backward-compatible migrations deliberately; rollback of code may not undo data changes.

## Practice

Write acceptance cases for the report, compare direct database calls inside the rule with injected loader, record a short ADR and test a dependency failure. Explain one alternative, trade-off, measurement and rollback strategy. Study the dedicated Git guide separately for deeper platform workflows; no external prerequisite is required.

**Quick reference:** clarify; specify; test; choose by trade-offs; observe; review and verify.

## Shared executable example

[progress_report.py](examples/progress_report.py)

`python technical-interview-preparation/21-software-engineering-and-technical-decisions/examples/progress_report.py`

## Official references

- [docs.python.org/3.13/library/unittest.html](https://docs.python.org/3.13/library/unittest.html)
- [docs.python.org/3.13/library/logging.html](https://docs.python.org/3.13/library/logging.html)

<!-- chapter-navigation:bottom -->
[← Previous](../20-transactions-indexes-and-sql-safety/README.md) · [Module index](../README.md) · [Next →](../22-technical-interview-question-bank/README.md)
<!-- /chapter-navigation:bottom -->
