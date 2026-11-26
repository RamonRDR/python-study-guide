# Transactions, Indexes and SQL Safety

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Previous](../19-joins-aggregations-and-data-relationships/README.md) · [Module index](../README.md) · [Next →](../21-software-engineering-and-technical-decisions/README.md)
<!-- /chapter-navigation:top -->

## Prerequisites

- [technical-interview-preparation/19-joins-aggregations-and-data-relationships](../../technical-interview-preparation/19-joins-aggregations-and-data-relationships/README.md)
- [technical-interview-preparation/15-exceptions-testing-and-debugging-review](../../technical-interview-preparation/15-exceptions-testing-and-debugging-review/README.md)

## Transactions and integrity

A transaction groups operations into a unit: commit accepts changes; rollback abandons uncommitted changes. ACID: atomicity (all or none), consistency (valid constraints/invariants), isolation (concurrent transaction visibility rules), durability (committed changes survive failures under the database/storage guarantees). Isolation levels and failure guarantees differ by engine; an in-memory database is not durable across process exit. Avoid holding transactions open during network calls. Constraints are useful backstops, not substitutes for business rules.

The example transfers integer credits between two distinct accounts. It checks source and available balance in one conditional UPDATE, checks affected rows, credits the target and rolls back if the target does not exist. A nonnegative integer balance is constrained in the database. The caller supplies a dedicated connection with autocommit=False, no unrelated pending writes, and commits setup before calling. Python 3.13's connection context manager commits on successful exit and rolls back on exception (or commit failure); it does not close the connection. With autocommit=True it does not provide this transaction boundary. Do not reuse the example as a nested transaction API or production financial system.

## Indexes and query planning

An index is an auxiliary data structure that can speed lookups, joins or ordering when the planner chooses it. It costs storage and write maintenance; not every column deserves an index. Composite index column order matters for query patterns. An index is not a guarantee of faster execution. Inspect a representative query plan (SQLite EXPLAIN QUERY PLAN) and measure; small tables may legitimately be scanned.

```sql
CREATE INDEX idx_accounts_name ON accounts(name);
EXPLAIN QUERY PLAN SELECT id FROM accounts WHERE name = 'A';
```

Do not assert an exact plan string across engine versions or data distributions.

## SQL safety

Bind input values with parameters, not string concatenation or f-strings. Placeholders do not bind table/column identifiers; use fixed SQL or an allowlist mapping to trusted identifiers. Least privilege and separate application validation remain necessary. The example's find_account uses a bound string; quote-containing input remains data, not query syntax.

## Practice

Transfer 3 credits from balances 10 and 2; expect 7 and 5. Then transfer to a missing target and verify both balances stay unchanged. Test insufficient funds, same account, invalid amount and a quote-containing lookup. Explain why rolling back after the debit is essential.

**Quick reference:** atomic changes; explicit transaction ownership; parameterize values; measure indexes; test failure paths.

## Shared executable example

[credit_transfer.py](examples/credit_transfer.py)

`python technical-interview-preparation/20-transactions-indexes-and-sql-safety/examples/credit_transfer.py`

## Official references

- [docs.python.org/3.13/library/sqlite3.html](https://docs.python.org/3.13/library/sqlite3.html)
- [www.sqlite.org/lang_transaction.html](https://www.sqlite.org/lang_transaction.html)
- [www.sqlite.org/queryplanner.html](https://www.sqlite.org/queryplanner.html)

<!-- chapter-navigation:bottom -->
[← Previous](../19-joins-aggregations-and-data-relationships/README.md) · [Module index](../README.md) · [Next →](../21-software-engineering-and-technical-decisions/README.md)
<!-- /chapter-navigation:bottom -->
