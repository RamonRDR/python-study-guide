from decimal import Decimal

from reconciliation import ReconciliationRecord, reconcile, render_text_report


def main() -> None:
    source_north = (
        ReconciliationRecord("REF-001", Decimal("150.00")),
        ReconciliationRecord("REF-002", Decimal("275.50")),
        ReconciliationRecord("REF-003", Decimal("100.00")),
    )
    source_south = (
        ReconciliationRecord("REF-001", Decimal("150.00")),
        ReconciliationRecord("REF-002", Decimal("270.50")),
        ReconciliationRecord("REF-004", Decimal("100.00")),
    )

    report = reconcile(
        source_north,
        source_south,
        left_name="Source North",
        right_name="Source South",
    )
    print(render_text_report(report), end="")


if __name__ == "__main__":
    main()
