from decimal import Decimal

import pytest

from reconciliation import ReconciliationRecord, reconcile


@pytest.mark.parametrize(
    "reference_id",
    [
        "REF-001\n[RIGHT_ONLY] SPOOF",
        "REF-001\rSPOOF",
        "REF-001\tSPOOF",
        "REF-001\x00SPOOF",
    ],
)
def test_record_rejects_non_printable_reference_id(reference_id: str) -> None:
    with pytest.raises(ValueError, match="printable characters"):
        ReconciliationRecord(reference_id, Decimal("10.00"))


@pytest.mark.parametrize(
    ("left_name", "right_name"),
    [
        ("Source A\n[RIGHT_ONLY] SPOOF", "Source B"),
        ("Source A", "Source B\rSPOOF"),
        ("Source A\tSPOOF", "Source B"),
        ("Source A", "Source B\x00SPOOF"),
    ],
)
def test_reconcile_rejects_non_printable_source_names(
    left_name: str,
    right_name: str,
) -> None:
    with pytest.raises(ValueError, match="printable characters"):
        reconcile([], [], left_name=left_name, right_name=right_name)
