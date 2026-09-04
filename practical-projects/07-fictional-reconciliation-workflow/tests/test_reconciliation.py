from decimal import Decimal

import pytest

from reconciliation import (
    ReconciliationItem,
    ReconciliationRecord,
    ReconciliationStatus,
    reconcile,
    render_text_report,
)


def record(reference_id: str, amount: str) -> ReconciliationRecord:
    return ReconciliationRecord(reference_id, Decimal(amount))


def test_record_trims_reference_id_and_canonicalizes_amount() -> None:
    item = record("  REF-001  ", "10")

    assert item.reference_id == "REF-001"
    assert item.amount == Decimal("10.00")
    assert item.amount.as_tuple().exponent == -2


@pytest.mark.parametrize("reference_id", ["", " ", "\t"])
def test_record_rejects_empty_reference_id(reference_id: str) -> None:
    with pytest.raises(ValueError, match="reference_id must not be empty"):
        record(reference_id, "10.00")


def test_record_rejects_non_string_reference_id() -> None:
    with pytest.raises(TypeError, match="reference_id must be a string"):
        ReconciliationRecord(101, Decimal("10.00"))  # type: ignore[arg-type]


def test_record_rejects_non_decimal_amount() -> None:
    with pytest.raises(TypeError, match="amount must be a Decimal"):
        ReconciliationRecord("REF-001", 10.00)  # type: ignore[arg-type]


@pytest.mark.parametrize("amount", ["NaN", "Infinity", "-Infinity"])
def test_record_rejects_non_finite_amount(amount: str) -> None:
    with pytest.raises(ValueError, match="amount must be finite"):
        record("REF-001", amount)


def test_record_rejects_more_than_two_decimal_places() -> None:
    with pytest.raises(ValueError, match="at most two decimal places"):
        record("REF-001", "10.001")


def test_record_normalizes_negative_zero() -> None:
    item = record("REF-001", "-0.00")

    assert item.amount == Decimal("0.00")
    assert f"{item.amount:.2f}" == "0.00"


def test_reconcile_matches_equal_records() -> None:
    report = reconcile(
        [record("REF-001", "150.00")],
        [record("REF-001", "150.00")],
    )

    item = report.items[0]
    assert item.status is ReconciliationStatus.MATCHED
    assert item.difference == Decimal("0.00")
    assert report.summary.matched == 1


def test_reconcile_detects_amount_mismatch_with_signed_difference() -> None:
    report = reconcile(
        [record("REF-001", "275.50")],
        [record("REF-001", "270.50")],
    )

    item = report.items[0]
    assert item.status is ReconciliationStatus.AMOUNT_MISMATCH
    assert item.difference == Decimal("5.00")
    assert report.summary.total_absolute_difference == Decimal("5.00")


def test_reconcile_preserves_negative_signed_difference() -> None:
    report = reconcile(
        [record("REF-001", "20.00")],
        [record("REF-001", "25.50")],
    )

    assert report.items[0].difference == Decimal("-5.50")
    assert report.summary.total_absolute_difference == Decimal("5.50")


def test_reconcile_detects_left_only_and_right_only() -> None:
    report = reconcile(
        [record("REF-001", "10.00")],
        [record("REF-002", "20.00")],
    )

    assert [item.status for item in report.items] == [
        ReconciliationStatus.LEFT_ONLY,
        ReconciliationStatus.RIGHT_ONLY,
    ]
    assert report.summary.left_only == 1
    assert report.summary.right_only == 1


def test_reconcile_sorts_results_by_reference_id() -> None:
    report = reconcile(
        [record("REF-003", "30.00"), record("REF-001", "10.00")],
        [record("REF-002", "20.00"), record("REF-003", "30.00")],
    )

    assert [item.reference_id for item in report.items] == [
        "REF-001",
        "REF-002",
        "REF-003",
    ]


def test_reconcile_accepts_single_pass_generators() -> None:
    left = (record(f"REF-{number}", f"{number}.00") for number in (1, 2))
    right = (record(f"REF-{number}", f"{number}.00") for number in (1, 2))

    report = reconcile(left, right)

    assert report.summary.matched == 2


def test_reconcile_rejects_duplicate_reference_within_left_source() -> None:
    with pytest.raises(ValueError, match="duplicate reference_id in Source A"):
        reconcile(
            [record("REF-001", "10.00"), record(" REF-001 ", "20.00")],
            [],
        )


def test_reconcile_rejects_duplicate_reference_within_right_source() -> None:
    with pytest.raises(ValueError, match="duplicate reference_id in Source B"):
        reconcile(
            [],
            [record("REF-001", "10.00"), record("REF-001", "20.00")],
        )


def test_reconcile_rejects_invalid_record_type() -> None:
    with pytest.raises(TypeError, match="must contain ReconciliationRecord"):
        reconcile([object()], [])  # type: ignore[list-item]


def test_reconcile_rejects_non_iterable_source() -> None:
    with pytest.raises(TypeError, match="Source A must be an iterable"):
        reconcile(None, [])  # type: ignore[arg-type]


@pytest.mark.parametrize(
    ("left_name", "right_name", "message"),
    [
        ("", "Source B", "left_name must not be empty"),
        ("Source A", " ", "right_name must not be empty"),
        ("Same", "Same", "must be different"),
    ],
)
def test_reconcile_validates_source_names(
    left_name: str,
    right_name: str,
    message: str,
) -> None:
    with pytest.raises(ValueError, match=message):
        reconcile([], [], left_name=left_name, right_name=right_name)


def test_reconcile_rejects_non_string_source_name() -> None:
    with pytest.raises(TypeError, match="left_name must be a string"):
        reconcile([], [], left_name=123)  # type: ignore[arg-type]


def test_reconcile_trims_source_names() -> None:
    report = reconcile([], [], left_name="  Source A  ", right_name=" Source B ")

    assert report.left_name == "Source A"
    assert report.right_name == "Source B"


def test_empty_reconciliation_has_zeroed_summary() -> None:
    report = reconcile([], [])

    assert report.items == ()
    assert report.summary.total_items == 0
    assert report.summary.matched == 0
    assert report.summary.amount_mismatches == 0
    assert report.summary.left_only == 0
    assert report.summary.right_only == 0
    assert report.summary.total_absolute_difference == Decimal("0.00")


def test_summary_counts_all_statuses_and_absolute_difference() -> None:
    report = reconcile(
        [
            record("REF-001", "10.00"),
            record("REF-002", "30.00"),
            record("REF-003", "40.00"),
        ],
        [
            record("REF-001", "10.00"),
            record("REF-002", "25.00"),
            record("REF-004", "12.00"),
        ],
    )

    assert report.summary.total_items == 4
    assert report.summary.matched == 1
    assert report.summary.amount_mismatches == 1
    assert report.summary.left_only == 1
    assert report.summary.right_only == 1
    assert report.summary.total_absolute_difference == Decimal("5.00")


def test_reference_matching_is_case_sensitive() -> None:
    report = reconcile(
        [record("ref-001", "10.00")],
        [record("REF-001", "10.00")],
    )

    assert [item.status for item in report.items] == [
        ReconciliationStatus.RIGHT_ONLY,
        ReconciliationStatus.LEFT_ONLY,
    ]


def test_reconciliation_item_rejects_inconsistent_left_only_shape() -> None:
    left = record("REF-001", "10.00")
    right = record("REF-001", "10.00")

    with pytest.raises(ValueError, match="left_only requires only a left record"):
        ReconciliationItem(
            reference_id="REF-001",
            status=ReconciliationStatus.LEFT_ONLY,
            left=left,
            right=right,
            difference=None,
        )


def test_reconciliation_item_rejects_wrong_difference() -> None:
    left = record("REF-001", "15.00")
    right = record("REF-001", "10.00")

    with pytest.raises(ValueError, match="difference must equal"):
        ReconciliationItem(
            reference_id="REF-001",
            status=ReconciliationStatus.AMOUNT_MISMATCH,
            left=left,
            right=right,
            difference=Decimal("4.00"),
        )


def test_render_text_report_is_deterministic() -> None:
    report = reconcile(
        [
            record("REF-001", "150.00"),
            record("REF-002", "275.50"),
            record("REF-003", "100.00"),
        ],
        [
            record("REF-001", "150.00"),
            record("REF-002", "270.50"),
            record("REF-004", "100.00"),
        ],
        left_name="Source North",
        right_name="Source South",
    )

    assert render_text_report(report) == (
        "Reconciliation Report\n"
        "Sources: Source North vs Source South\n"
        "\n"
        "[MATCHED] REF-001: 150.00 == 150.00\n"
        "[AMOUNT_MISMATCH] REF-002: Source North=275.50, "
        "Source South=270.50, difference=5.00\n"
        "[LEFT_ONLY] REF-003: Source North=100.00\n"
        "[RIGHT_ONLY] REF-004: Source South=100.00\n"
        "\n"
        "Summary\n"
        "Total items: 4\n"
        "Matched: 1\n"
        "Amount mismatches: 1\n"
        "Left only: 1\n"
        "Right only: 1\n"
        "Total absolute difference: 5.00\n"
    )


def test_render_empty_report_is_stable() -> None:
    report = reconcile([], [], left_name="North", right_name="South")

    assert render_text_report(report) == (
        "Reconciliation Report\n"
        "Sources: North vs South\n"
        "\n"
        "\n"
        "Summary\n"
        "Total items: 0\n"
        "Matched: 0\n"
        "Amount mismatches: 0\n"
        "Left only: 0\n"
        "Right only: 0\n"
        "Total absolute difference: 0.00\n"
    )


def test_render_text_report_rejects_wrong_type() -> None:
    with pytest.raises(TypeError, match="ReconciliationReport"):
        render_text_report(object())  # type: ignore[arg-type]
