from decimal import Decimal

from reconciliation import ReconciliationRecord, reconcile


def record(reference_id: str, amount: str) -> ReconciliationRecord:
    return ReconciliationRecord(reference_id, Decimal(amount))


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
