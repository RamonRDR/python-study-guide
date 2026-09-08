from decimal import Decimal

import pytest

from reconciliation import ReconciliationItem, ReconciliationStatus


class AttachmentLookalike:
    """Object that mimics record attributes without being a domain record."""

    reference_id = "REF-001"
    amount = Decimal("10.00")


@pytest.mark.parametrize(
    ("status", "left", "right", "message"),
    [
        (
            ReconciliationStatus.LEFT_ONLY,
            AttachmentLookalike(),
            None,
            "left must be a ReconciliationRecord or None",
        ),
        (
            ReconciliationStatus.RIGHT_ONLY,
            None,
            AttachmentLookalike(),
            "right must be a ReconciliationRecord or None",
        ),
    ],
)
def test_reconciliation_item_rejects_non_record_attachments(
    status: ReconciliationStatus,
    left: object | None,
    right: object | None,
    message: str,
) -> None:
    with pytest.raises(TypeError, match=message):
        ReconciliationItem(
            reference_id="REF-001",
            status=status,
            left=left,  # type: ignore[arg-type]
            right=right,  # type: ignore[arg-type]
            difference=None,
        )
