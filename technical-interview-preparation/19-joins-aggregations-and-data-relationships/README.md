# Joins, Aggregations and Data Relationships

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Previous](../18-relational-databases-and-sql/README.md) · [Module index](../README.md) · [Next →](../20-transactions-indexes-and-sql-safety/README.md)
<!-- /chapter-navigation:top -->

## Prerequisites

- [technical-interview-preparation/18-relational-databases-and-sql](../../technical-interview-preparation/18-relational-databases-and-sql/README.md)

## Relationships and join cardinality

One-to-many: one group has many tasks, each task belongs to one group. A foreign key prevents dangling references when enforcement is enabled. Many-to-many uses a junction table (e.g. enrollment with learner_id and lesson_id as a composite primary key). One-to-one can use a unique foreign key. Normalization separates repeated facts to reduce update anomalies; denormalization is a deliberate trade-off, not a default performance fix. In SQLite enable foreign_keys per connection before any transaction and verify it.

INNER JOIN keeps matching rows. LEFT JOIN keeps every left row and fills unmatched right columns with NULL. More than one matching child yields more than one row; joining multiple one-to-many relationships can multiply counts. Group at the correct grain or preaggregate. The example counts completed tasks for every group, even groups with no tasks or no completed tasks.

```sql
SELECT groups.name, COUNT(tasks.id)
FROM groups LEFT JOIN tasks
    ON groups.id = tasks.group_id AND tasks.done = 1
GROUP BY groups.id, groups.name
ORDER BY groups.name, groups.id;
```

A filter in ON limits matches while preserving left rows; putting tasks.done = 1 in WHERE removes null-extended rows. COUNT(*) counts rows including a null-extended row; COUNT(column) excludes NULL. Use the non-null child ID here.

## Aggregations

SUM totals non-null values, AVG averages them, MIN/MAX find extrema; COUNT counts as above. Empty input can yield NULL for SUM/AVG; decide whether COALESCE(..., 0) matches the business meaning. WHERE filters rows before grouping; HAVING filters groups after aggregation (e.g. HAVING COUNT(tasks.id) >= 2). GROUP BY the stable identifier, not only a nonunique display name. SQL results have no guaranteed order without ORDER BY.

## Practice

Create three groups: two completed tasks for A, only incomplete tasks for B and no tasks for C. Expect A=2, B=0, C=0. Move the filter to WHERE and observe the missing groups in your own copy. Test a task referring to a nonexistent group and explain why enforcement matters.

**Quick reference:** join on keys; choose cardinality; filter at the correct stage; count non-null children.

## Shared executable example

[group_progress.py](examples/group_progress.py)

`python technical-interview-preparation/19-joins-aggregations-and-data-relationships/examples/group_progress.py`

## Official references

- [www.sqlite.org/lang_select.html](https://www.sqlite.org/lang_select.html)
- [www.sqlite.org/lang_aggfunc.html](https://www.sqlite.org/lang_aggfunc.html)
- [www.sqlite.org/foreignkeys.html](https://www.sqlite.org/foreignkeys.html)

<!-- chapter-navigation:bottom -->
[← Previous](../18-relational-databases-and-sql/README.md) · [Module index](../README.md) · [Next →](../20-transactions-indexes-and-sql-safety/README.md)
<!-- /chapter-navigation:bottom -->
