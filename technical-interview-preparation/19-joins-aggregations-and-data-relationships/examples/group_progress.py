"""Count matching children without dropping empty parent groups."""
from contextlib import closing
import sqlite3


def create_tables(db: sqlite3.Connection) -> None:
    # Enable enforcement outside a transaction, on this connection.
    db.execute("PRAGMA foreign_keys = ON")
    if db.execute("PRAGMA foreign_keys").fetchone() != (1,):
        raise RuntimeError("foreign key enforcement is required")
    db.execute("CREATE TABLE groups (id INTEGER PRIMARY KEY, name TEXT NOT NULL)")
    db.execute("""
        CREATE TABLE tasks (
            id INTEGER PRIMARY KEY,
            group_id INTEGER NOT NULL REFERENCES groups(id),
            done INTEGER NOT NULL CHECK (done IN (0, 1))
        )
    """)


def completed_by_group(db: sqlite3.Connection) -> list[tuple]:
    return db.execute("""
        SELECT groups.name, COUNT(tasks.id)
        FROM groups LEFT JOIN tasks
            ON groups.id = tasks.group_id AND tasks.done = 1
        GROUP BY groups.id, groups.name
        ORDER BY groups.name, groups.id
    """).fetchall()


if __name__ == "__main__":
    with closing(sqlite3.connect(":memory:", autocommit=True)) as db:
        create_tables(db)
        db.executemany("INSERT INTO groups VALUES (?, ?)", [(1, "A"), (2, "B")])
        db.execute("INSERT INTO tasks VALUES (?, ?, ?)", (1, 1, 1))
        print(completed_by_group(db))
