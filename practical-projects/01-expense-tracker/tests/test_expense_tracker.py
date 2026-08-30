from decimal import Decimal

import pytest

from expense_tracker import Expense, ExpenseTracker, parse_amount


def test_expense_create_normalizes_fields() -> None:
    expense = Expense.create("2026-08-29", "  Lunch  ", " Food ", "25.905")

    assert expense.spent_on.isoformat() == "2026-08-29"
    assert expense.description == "Lunch"
    assert expense.category == "Food"
    assert expense.amount == Decimal("25.91")


@pytest.mark.parametrize("value", ["0", "-1", "NaN", "Infinity"])
def test_parse_amount_rejects_invalid_values(value: str) -> None:
    with pytest.raises(ValueError):
        parse_amount(value)


def test_parse_amount_normalizes_quantize_failure() -> None:
    with pytest.raises(ValueError, match="two decimal places"):
        parse_amount("1" + "0" * 100)


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
