from datetime import date, datetime
from decimal import Decimal, Inexact, localcontext

import pytest

from expense_tracker import Expense, ExpenseTracker, parse_amount, parse_date


def test_expense_create_normalizes_fields() -> None:
    expense = Expense.create("2026-08-29", "  Lunch  ", " Food ", "25.905")

    assert expense.spent_on.isoformat() == "2026-08-29"
    assert expense.description == "Lunch"
    assert expense.category == "Food"
    assert expense.amount == Decimal("25.91")


def test_direct_expense_constructor_enforces_validation() -> None:
    with pytest.raises(ValueError, match="greater than zero"):
        Expense(
            spent_on=date(2026, 8, 29),
            description="Lunch",
            category="Food",
            amount=Decimal("-1.00"),
        )


@pytest.mark.parametrize("value", ["20260829", "2026-W35-6", "2026-8-29"])
def test_parse_date_requires_exact_yyyy_mm_dd_text(value: str) -> None:
    with pytest.raises(ValueError, match="YYYY-MM-DD"):
        parse_date(value)


def test_parse_date_rejects_datetime_values() -> None:
    with pytest.raises(ValueError, match="time component"):
        parse_date(datetime(2026, 8, 29, 12, 30))


@pytest.mark.parametrize("value", ["0", "-1", "NaN", "Infinity"])
def test_parse_amount_rejects_invalid_values(value: str) -> None:
    with pytest.raises(ValueError):
        parse_amount(value)


def test_parse_amount_isolated_from_caller_decimal_context() -> None:
    with localcontext() as context:
        context.prec = 3
        context.traps[Inexact] = True

        assert parse_amount("25.40") == Decimal("25.40")
        assert parse_amount("25.905") == Decimal("25.91")


def test_parse_amount_rejects_positive_value_that_rounds_to_zero() -> None:
    with pytest.raises(ValueError, match="at least 0.01"):
        parse_amount("0.004")


def test_parse_amount_normalizes_quantize_failure() -> None:
    with pytest.raises(ValueError, match="two decimal places"):
        parse_amount("1e1000000")


def test_invalid_add_does_not_mutate_tracker() -> None:
    tracker = ExpenseTracker()

    with pytest.raises(ValueError):
        tracker.add("2026-08-29", "Lunch", "Food", "0")

    assert tracker.expenses == ()


def test_tracker_totals_and_case_insensitive_filtering() -> None:
    tracker = ExpenseTracker()
    tracker.add("2026-08-28", "Bus", "Transport", "12.00")
    tracker.add("2026-08-29", "Lunch", "Food", "25.40")
    tracker.add("2026-08-29", "Snack", "food", "4.60")

    assert tracker.total() == Decimal("42.00")
    assert tracker.total("FOOD") == Decimal("30.00")
    assert len(tracker.filter_by_category("food")) == 2
    assert tracker.totals_by_category() == {
        "Transport": Decimal("12.00"),
        "Food": Decimal("30.00"),
    }


def test_large_amount_aggregation_preserves_every_cent() -> None:
    tracker = ExpenseTracker()
    large_amount = "99999999999999999999999999.99"
    expected_total = Decimal("199999999999999999999999999.98")

    tracker.add("2026-08-28", "License A", "Software", large_amount)
    tracker.add("2026-08-29", "License B", "software", large_amount)

    assert tracker.total() == expected_total
    assert tracker.total("SOFTWARE") == expected_total
    assert tracker.totals_by_category() == {"Software": expected_total}


def test_json_round_trip(tmp_path) -> None:
    tracker = ExpenseTracker()
    tracker.add("2026-08-29", "Book", "Study", "79.90")

    json_path = tracker.save_json(tmp_path / "data" / "expenses.json")
    loaded = ExpenseTracker.load_json(json_path)

    assert loaded.expenses == tracker.expenses


def test_load_json_rejects_wrong_top_level_shape(tmp_path) -> None:
    path = tmp_path / "expenses.json"
    path.write_text('{"amount": "10.00"}', encoding="utf-8")

    with pytest.raises(ValueError, match="JSON list"):
        ExpenseTracker.load_json(path)


def test_load_json_rejects_missing_required_field(tmp_path) -> None:
    path = tmp_path / "expenses.json"
    path.write_text(
        '[{"spent_on":"2026-08-29","description":"Book","category":"Study"}]',
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="amount"):
        ExpenseTracker.load_json(path)


def test_export_csv_writes_header_and_rows(tmp_path) -> None:
    tracker = ExpenseTracker()
    tracker.add("2026-08-29", "Lunch", "Food", "25.40")
    tracker.add("2026-08-29", "Bus", "Transport", "12.00")

    csv_path = tracker.export_csv(tmp_path / "expenses.csv")
    lines = csv_path.read_text(encoding="utf-8").splitlines()

    assert lines == [
        "spent_on,description,category,amount",
        "2026-08-29,Lunch,Food,25.40",
        "2026-08-29,Bus,Transport,12.00",
    ]
