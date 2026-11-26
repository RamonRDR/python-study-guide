"""Demonstrate atomic transfers, parameter binding and a lookup index."""
from contextlib import closing
import sqlite3


def create_accounts(db: sqlite3.Connection) -> None:
    db.execute("""
        CREATE TABLE accounts (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            balance INTEGER NOT NULL CHECK (
                typeof(balance) = 'integer' AND balance >= 0
            )
        )
    """)
    db.execute("CREATE INDEX idx_accounts_name ON accounts(name)")


def transfer(db: sqlite3.Connection, source: int, target: int, amount: int) -> None:
    if (type(source) is not int or type(target) is not int
            or type(amount) is not int or amount <= 0 or source == target):
        raise ValueError("invalid transfer")
    # The caller supplies a dedicated connection with autocommit=False
    # and no unrelated pending writes; this function owns the transaction.
    if db.autocommit is not False:
        raise ValueError("transfer requires autocommit=False")
    with db:
        debit = db.execute("""
            UPDATE accounts SET balance = balance - ?
            WHERE id = ? AND balance >= ?
        """, (amount, source, amount))
        if debit.rowcount != 1:
            raise ValueError("missing source or insufficient balance")
        credit = db.execute("""
            UPDATE accounts SET balance = balance + ? WHERE id = ?
        """, (amount, target))
        if credit.rowcount != 1:
            raise ValueError("missing target")


def balances(db: sqlite3.Connection) -> list[tuple]:
    return db.execute("SELECT id, balance FROM accounts ORDER BY id").fetchall()


def find_account(db: sqlite3.Connection, name: str) -> list[tuple]:
    return db.execute("SELECT id FROM accounts WHERE name = ? ORDER BY id", (name,)).fetchall()


if __name__ == "__main__":
    with closing(sqlite3.connect(":memory:", autocommit=False)) as db:
        create_accounts(db)
        db.executemany("INSERT INTO accounts VALUES (?, ?, ?)", [(1, "A", 10), (2, "B", 2)])
        db.commit()
        transfer(db, 1, 2, 3)
        print(balances(db))
        try:
            transfer(db, 1, 99, 2)
        except ValueError:
            print(balances(db))
