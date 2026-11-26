# Relational Databases and SQL

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Previous](../17-api-contracts-authentication-and-authorization/README.md) · [Module index](../README.md) · [Next →](../19-joins-aggregations-and-data-relationships/README.md)
<!-- /chapter-navigation:top -->

## Prerequisites

- [technical-interview-preparation/13-context-managers](../../technical-interview-preparation/13-context-managers/README.md)
- [technical-interview-preparation/17-api-contracts-authentication-and-authorization](../../technical-interview-preparation/17-api-contracts-authentication-and-authorization/README.md)

## Relational model and constraints

A relational database organizes data in tables of rows and columns with relationships and constraints. A primary key identifies a row; UNIQUE constrains duplicates, NOT NULL requires a value, CHECK enforces a predicate, and foreign keys connect rows (next chapter). NULL represents missing/unknown information; use IS NULL, not = NULL. In SQL, comparisons with NULL generally yield unknown, and WHERE keeps true rows. A CHECK does not by itself prohibit NULL; combine it with NOT NULL where required.

SQLite is an embedded SQL database; Python's sqlite3 module works with a local file or :memory: database. Other engines differ in types, syntax, isolation and deployment. SQLite has flexible typing: declared INTEGER is not a universal strict type check, so the example checks stored type and positivity. SQL can coerce inputs before storage; validate domain types at the application boundary too.

```sql
CREATE TABLE lessons (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL UNIQUE,
    minutes INTEGER NOT NULL CHECK (minutes > 0)
);
INSERT INTO lessons(title, minutes) VALUES ('SQL', 20);
SELECT title, minutes FROM lessons
WHERE minutes <= 20 ORDER BY minutes, title;
```

Result: SQL, 20. CREATE changes schema; INSERT creates rows; SELECT reads; UPDATE changes selected rows; DELETE removes selected rows. UPDATE/DELETE without WHERE can affect every row. ORDER BY is needed for guaranteed order; LIMIT alone does not define which rows are first. Select required columns rather than fetching unnecessary data.

## Connect from Python

Use a connection and execute with placeholders for values, e.g. `db.execute("SELECT title FROM lessons WHERE minutes <= ?", (20,))`. A one-element tuple needs the comma. Fetch results with fetchall for small result sets; iterate a cursor for larger sets. The example explicitly uses autocommit=True for independent statements and contextlib.closing for resource release; the connection context manager does not close it. Transactions are taught in chapter 20.

## Practice

Add lessons, filter by duration, check deterministic ordering and verify duplicate title, null title and zero duration fail. Explain schema constraint versus application validation. Use local Python 3.13; no database server is needed.

**Quick reference:** model rows and keys; constrain integrity; query explicitly; bind values; close connections.

## Shared executable example

[lesson_catalog.py](examples/lesson_catalog.py)

`python technical-interview-preparation/18-relational-databases-and-sql/examples/lesson_catalog.py`

## Official references

- [docs.python.org/3.13/library/sqlite3.html](https://docs.python.org/3.13/library/sqlite3.html)
- [www.sqlite.org/lang_createtable.html](https://www.sqlite.org/lang_createtable.html)
- [www.sqlite.org/lang_select.html](https://www.sqlite.org/lang_select.html)

<!-- chapter-navigation:bottom -->
[← Previous](../17-api-contracts-authentication-and-authorization/README.md) · [Module index](../README.md) · [Next →](../19-joins-aggregations-and-data-relationships/README.md)
<!-- /chapter-navigation:bottom -->
