from __future__ import annotations

import csv
import json
from dataclasses import dataclass
from datetime import date
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
from pathlib import Path
from typing import Iterable, Mapping

CENT = Decimal("0.01")


def parse_date(value: date | str) -> date:
    """Return a date from a date object or ISO YYYY-MM-DD text."""
    if isinstance(value, date):
        return value

    try:
        return date.fromisoformat(value)
    except (TypeError, ValueError) as exc:
        raise ValueError("date must use YYYY-MM-DD") from exc


def normalize_text(value: str, field_name: str) -> str:
    """Strip surrounding whitespace and reject blank text."""
    if not isinstance(value, str):
        raise TypeError(f"{field_name} must be text")

    normalized = value.strip()
    if not normalized:
        raise ValueError(f"{field_name} cannot be blank")
    return normalized


def parse_amount(value: Decimal | str | int) -> Decimal:
    """Return a positive two-decimal Decimal amount."""
    try:
        amount = value if isinstance(value, Decimal) else Decimal(str(value))
    except (InvalidOperation, ValueError) as exc:
        raise ValueError("amount must be a valid decimal number") from exc

    if not amount.is_finite():
        raise ValueError("amount must be finite")
    if amount <= 0:
        raise ValueError("amount must be greater than zero")

    return amount.quantize(CENT, rounding=ROUND_HALF_UP)


@dataclass(frozen=True, slots=True)
class Expense:
    """One validated expense record."""

    spent_on: date
    description: str
    category: str
    amount: Decimal

    @classmethod
    def create(
        cls,
        spent_on: date | str,
        description: str,
        category: str,
        amount: Decimal | str | int,
    ) -> "Expense":
        return cls(
            spent_on=parse_date(spent_on),
            description=normalize_text(description, "description"),
            category=normalize_text(category, "category"),
            amount=parse_amount(amount),
        )

    def to_record(self) -> dict[str, str]:
        return {
            "spent_on": self.spent_on.isoformat(),
            "description": self.description,
            "category": self.category,
            "amount": format(self.amount, ".2f"),
        }

    @classmethod
    def from_record(cls, record: Mapping[str, object]) -> "Expense":
        required = {"spent_on", "description", "category", "amount"}
        missing = required.difference(record)
        if missing:
            missing_fields = ", ".join(sorted(missing))
            raise ValueError(f"missing expense field(s): {missing_fields}")

        return cls.create(
            spent_on=record["spent_on"],
            description=record["description"],
            category=record["category"],
            amount=record["amount"],
        )


class ExpenseTracker:
    """In-memory collection with persistence and reporting helpers."""

    def __init__(self, expenses: Iterable[Expense] = ()) -> None:
        self._expenses = list(expenses)

    @property
    def expenses(self) -> tuple[Expense, ...]:
        return tuple(self._expenses)

    def add(
        self,
        spent_on: date | str,
        description: str,
        category: str,
        amount: Decimal | str | int,
    ) -> Expense:
        expense = Expense.create(spent_on, description, category, amount)
        self._expenses.append(expense)
        return expense

    def filter_by_category(self, category: str) -> tuple[Expense, ...]:
        target = normalize_text(category, "category").casefold()
        return tuple(
            expense
            for expense in self._expenses
            if expense.category.casefold() == target
        )

    def total(self, category: str | None = None) -> Decimal:
        selected = self._expenses if category is None else self.filter_by_category(category)
        return sum((expense.amount for expense in selected), start=Decimal("0.00"))

    def totals_by_category(self) -> dict[str, Decimal]:
        totals: dict[str, Decimal] = {}
        canonical_names: dict[str, str] = {}

        for expense in self._expenses:
            key = expense.category.casefold()
            display_name = canonical_names.setdefault(key, expense.category)
            totals[display_name] = totals.get(display_name, Decimal("0.00")) + expense.amount

        return totals

    def save_json(self, path: str | Path) -> Path:
        target = Path(path)
        target.parent.mkdir(parents=True, exist_ok=True)
        payload = [expense.to_record() for expense in self._expenses]
        target.write_text(
            json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
        return target

    @classmethod
    def load_json(cls, path: str | Path) -> "ExpenseTracker":
        source = Path(path)
        try:
            payload = json.loads(source.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            raise ValueError("expense file contains invalid JSON") from exc

        if not isinstance(payload, list):
            raise ValueError("expense file must contain a JSON list")

        expenses: list[Expense] = []
        for index, record in enumerate(payload, start=1):
            if not isinstance(record, dict):
                raise ValueError(f"expense record {index} must be a JSON object")
            expenses.append(Expense.from_record(record))

        return cls(expenses)

    def export_csv(self, path: str | Path) -> Path:
        target = Path(path)
        target.parent.mkdir(parents=True, exist_ok=True)

        with target.open("w", encoding="utf-8", newline="") as file:
            writer = csv.DictWriter(
                file,
                fieldnames=["spent_on", "description", "category", "amount"],
            )
            writer.writeheader()
            writer.writerows(expense.to_record() for expense in self._expenses)

        return target
