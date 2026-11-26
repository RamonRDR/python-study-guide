"""Teach simple SQLite table constraints and ordered selection."""
from contextlib import closing
import sqlite3


def create_catalog(db: sqlite3.Connection) -> None:
    db.execute("""
        CREATE TABLE lessons (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL UNIQUE,
            minutes INTEGER NOT NULL CHECK (
                typeof(minutes) = 'integer' AND minutes > 0
            )
        )
    """)


def add_lesson(db: sqlite3.Connection, title: str, minutes: int) -> None:
    db.execute("INSERT INTO lessons(title, minutes) VALUES (?, ?)", (title, minutes))


def short_lessons(db: sqlite3.Connection, maximum: int) -> list[tuple]:
    return db.execute("""
        SELECT title, minutes FROM lessons
        WHERE minutes <= ? ORDER BY minutes, title
    """, (maximum,)).fetchall()


if __name__ == "__main__":
    with closing(sqlite3.connect(":memory:", autocommit=True)) as db:
        create_catalog(db)
        add_lesson(db, "Python", 30)
        add_lesson(db, "SQL", 20)
        print(short_lessons(db, 20))
