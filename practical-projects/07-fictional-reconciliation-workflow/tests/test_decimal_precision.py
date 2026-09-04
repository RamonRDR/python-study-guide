from decimal import Decimal, localcontext

import pytest

from reconciliation import ReconciliationRecord, reconcile


def record(reference_id: str, amount: str) -> ReconciliationRecord:
    return ReconciliationRecord(reference_id, Decimal(amount))


def test_record_accepts_valid_amount_under_low_decimal_precision() -> None:
    with localcontext() as context:
        context.prec = 3
        item = ReconciliationRecord("REF-001", Decimal("10.00"))

    assert item.amount == Decimal("10.00")
    assert item.amount.as_tuple().exponent == -2


def test_record_accepts_large_exact_amount_beyond_default_precision() -> None:
    amount = Decimal("99999999999999999999999999.99")

    item = ReconciliationRecord("REF-001", amount)

    assert item.amount == amount
    assert item.amount.as_tuple().exponent == -2


def test_record_rejects_extreme_subcent_exponent_without_large_power() -> None:
    amount = Decimal("1e-1000000000")

    with pytest.raises(ValueError, match="at most two decimal places"):
        ReconciliationRecord("REF-001", amount)


def test_reconcile_preserves_difference_beyond_decimal_context_precision() -> None:
    amount = "99999999999999999999999999.99"

    report = reconcile(
        [record("REF-001", amount)],
        [record("REF-001", f"-{amount}")],
    )

    assert report.items[0].difference == Decimal(
        "199999999999999999999999999.98"
    )


def test_summary_preserves_sum_beyond_decimal_context_precision() -> None:
    amount = "99999999999999999999999999.99"

    report = reconcile(
        [
            record("REF-001", amount),
            record("REF-002", amount),
        ],
        [
            record("REF-001", "0.00"),
            record("REF-002", "0.00"),
        ],
    )

    assert report.summary.total_absolute_difference == Decimal(
        "199999999999999999999999999.98"
    )
