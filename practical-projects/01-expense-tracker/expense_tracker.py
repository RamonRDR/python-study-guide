from __future__ import annotations

import csv
import json
import re
from dataclasses import dataclass
from datetime import date, datetime
from decimal import Context, Decimal, InvalidOperation, ROUND_HALF_UP
from pathlib import Path
from typing import Iterable, Mapping

CENT = Decimal("0.01")
DATE_TEXT_PATTERN = re.compile(r"\d{4}-\d{2}-\d{2}\Z")


def parse_date(value: date | str) -> date:
    """Return a plain date from a date object or strict YYYY-MM-DD text."""
    if isinstance(value, datetime):
        raise ValueError("date must not include a time component")
    if isinstance(value, date):
        return value
    if not isinstance(value, str) or DATE_TEXT_PATTERN.fullmatch(value) is None:
        raise ValueError("date must use YYYY-MM-DD")

    try:
        return date.fromisoformat(value)
    except ValueError as exc:
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

    decimal_tuple = amount.as_tuple()
    precision = max(
        28,
        len(decimal_tuple.digits),
        amount.adjusted() + 3,
    )
    amount_context = Context(prec=precision, rounding=ROUND_HALF_UP)

    try:
        rounded = amount.quantize(CENT, context=amount_context)
    except InvalidOperation as exc:
        raise ValueError("amount cannot be represented with two decimal places") from exc

    if rounded <= 0:
        raise ValueError("amount must round to at least 0.01")
    return rounded


def _amount_to_cents(amount: Decimal) -> int:
    """Convert a validated two-decimal amount to an exact integer cent count."""
    decimal_tuple = amount.as_tuple()
    if decimal_tuple.exponent != -2:
        raise ValueError("normalized amount must have exactly two decimal places")

    coefficient = 0
    for digit in decimal_tuple.digits:
        coefficient = coefficient * 10 + digit

    return -coefficient if decimal_tuple.sign else coefficient


def _cents_to_amount(cents: int) -> Decimal:
    """Build an exact two-decimal Decimal without using arithmetic context."""
    digits = tuple(int(digit) for digit in str(abs(cents)))
    sign = 1 if cents < 0 else 0
    return Decimal((sign, digits, -2))


def _sum_amounts(amounts: Iterable[Decimal]) -> Decimal:
    """Sum validated amounts exactly by aggregating arbitrary-precision cents."""
    total_cents = sum(_amount_to_cents(amount) for amount in amounts)
    return _cents_to_amount(total_cents)


@dataclass(frozen=True, slots=True)
class Expense:
    """One validated expense record."""

    spent_on: date
    description: str
    category: str
    amount: Decimal

    def __post_init__(self) -> None:
        """Enforce invariants even when callers use the dataclass constructor."""
        object.__setattr__(self, "spent_on", parse_date(self.spent_on))
        object.__setattr__(
            self,
            "description",
            normalize_text(self.description, "description"),
        )
        object.__setattr__(
            self,
            "category",
            normalize_text(self.category, "category"),
        )
        object.__setattr__(self, "amount", parse_amount(self.amount))

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
        return _sum_amounts(expense.amount for expense in selected)

    def totals_by_category(self) -> dict[str, Decimal]:
        totals_in_cents: dict[str, int] = {}
        canonical_names: dict[str, str] = {}

        for expense in self._expenses:
            key = expense.category.casefold()
            display_name = canonical_names.setdefault(key, expense.category)
            totals_in_cents[display_name] = (
                totals_in_cents.get(display_name, 0)
                + _amount_to_cents(expense.amount)
            )

        return {
            category: _cents_to_amount(total_cents)
            for category, total_cents in totals_in_cents.items()
        }

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
