"""Deterministic reconciliation for two fictional record sources."""

from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal
from enum import StrEnum
from typing import Iterable


MAX_INTEGER_DIGITS = 100


class ReconciliationStatus(StrEnum):
    """Possible outcomes for one reference during reconciliation."""

    MATCHED = "matched"
    AMOUNT_MISMATCH = "amount_mismatch"
    LEFT_ONLY = "left_only"
    RIGHT_ONLY = "right_only"


def _digits_to_int(digits: tuple[int, ...]) -> int:
    """Build an integer coefficient from Decimal digits without context math."""

    coefficient = 0
    for digit in digits:
        coefficient = coefficient * 10 + digit
    return coefficient


def _integer_digit_count(value: Decimal) -> int:
    """Return the number of digits in the integer part without expansion."""

    _, digits, exponent = value.as_tuple()
    if not any(digits):
        return 1
    return max(1, len(digits) + exponent)


def _validate_amount_magnitude(value: Decimal) -> None:
    """Reject monetary inputs beyond the project's explicit size boundary."""

    if _integer_digit_count(value) > MAX_INTEGER_DIGITS:
        raise ValueError(
            f"amount must have at most {MAX_INTEGER_DIGITS} integer digits"
        )


def _decimal_to_cents(value: Decimal) -> int:
    """Convert an exact cent-representable Decimal to integer cents.

    The conversion uses only the Decimal coefficient and exponent, so its
    result is independent of the active Decimal arithmetic context. For
    sub-cent exponents, discarded positions are inspected from the existing
    digit tuple instead of materializing a potentially enormous power of ten.
    External record values are magnitude-checked before calling this helper.
    """

    sign, digits, exponent = value.as_tuple()
    coefficient = _digits_to_int(digits)

    if coefficient == 0:
        return 0

    if exponent >= -2:
        cents = coefficient * (10 ** (exponent + 2))
    else:
        discarded_places = -2 - exponent
        if discarded_places >= len(digits):
            raise ValueError("amount must have at most two decimal places")

        split_at = len(digits) - discarded_places
        if any(digits[split_at:]):
            raise ValueError("amount must have at most two decimal places")
        cents = _digits_to_int(digits[:split_at])

    return -cents if sign else cents


def _cents_to_decimal(cents: int) -> Decimal:
    """Build a two-decimal Decimal without context or integer-string limits."""

    if cents == 0:
        return Decimal("0.00")

    magnitude = Decimal(abs(cents))
    digits = magnitude.as_tuple().digits
    sign = 1 if cents < 0 else 0
    return Decimal((sign, digits, -2))


def _subtract_amounts(left: Decimal, right: Decimal) -> Decimal:
    """Return an exact signed difference for canonical monetary amounts."""

    return _cents_to_decimal(_decimal_to_cents(left) - _decimal_to_cents(right))


def _validate_printable_text(value: str, *, field_name: str) -> str:
    """Normalize surrounding whitespace and reject non-printable content."""

    normalized = value.strip()
    if not normalized:
        raise ValueError(f"{field_name} must not be empty")
    if not normalized.isprintable():
        raise ValueError(f"{field_name} must contain only printable characters")
    return normalized


@dataclass(frozen=True, slots=True)
class ReconciliationRecord:
    """One validated monetary record selected for reconciliation."""

    reference_id: str
    amount: Decimal

    def __post_init__(self) -> None:
        if not isinstance(self.reference_id, str):
            raise TypeError("reference_id must be a string")
        if not isinstance(self.amount, Decimal):
            raise TypeError("amount must be a Decimal")

        normalized_id = _validate_printable_text(
            self.reference_id,
            field_name="reference_id",
        )

        if not self.amount.is_finite():
            raise ValueError("amount must be finite")

        _validate_amount_magnitude(self.amount)
        cents = _decimal_to_cents(self.amount)
        normalized_amount = _cents_to_decimal(cents)

        object.__setattr__(self, "reference_id", normalized_id)
        object.__setattr__(self, "amount", normalized_amount)


@dataclass(frozen=True, slots=True)
class ReconciliationItem:
    """Reconciliation outcome for exactly one reference id."""

    reference_id: str
    status: ReconciliationStatus
    left: ReconciliationRecord | None
    right: ReconciliationRecord | None
    difference: Decimal | None

    def __post_init__(self) -> None:
        if not isinstance(self.reference_id, str) or not self.reference_id:
            raise ValueError("reference_id must be a non-empty string")
        if not self.reference_id.isprintable():
            raise ValueError("reference_id must contain only printable characters")
        if not isinstance(self.status, ReconciliationStatus):
            raise TypeError("status must be a ReconciliationStatus")

        if self.difference is not None and not isinstance(self.difference, Decimal):
            raise TypeError("difference must be a Decimal or None")

        for record in (self.left, self.right):
            if record is not None and record.reference_id != self.reference_id:
                raise ValueError(
                    "item reference_id must match every attached record"
                )

        if self.status is ReconciliationStatus.LEFT_ONLY:
            if (
                self.left is None
                or self.right is not None
                or self.difference is not None
            ):
                raise ValueError("left_only requires only a left record")
            return

        if self.status is ReconciliationStatus.RIGHT_ONLY:
            if (
                self.left is not None
                or self.right is None
                or self.difference is not None
            ):
                raise ValueError("right_only requires only a right record")
            return

        if self.left is None or self.right is None or self.difference is None:
            raise ValueError(
                "matched comparisons require both records and a difference"
            )

        expected_difference = _subtract_amounts(self.left.amount, self.right.amount)
        if self.difference != expected_difference:
            raise ValueError("difference must equal left amount minus right amount")

        if self.status is ReconciliationStatus.MATCHED and self.difference != Decimal(
            "0.00"
        ):
            raise ValueError("matched items require a zero difference")
        if (
            self.status is ReconciliationStatus.AMOUNT_MISMATCH
            and self.difference == Decimal("0.00")
        ):
            raise ValueError("amount_mismatch items require a non-zero difference")


@dataclass(frozen=True, slots=True)
class ReconciliationSummary:
    """Aggregate counts for one reconciliation run."""

    total_items: int
    matched: int
    amount_mismatches: int
    left_only: int
    right_only: int
    total_absolute_difference: Decimal


@dataclass(frozen=True, slots=True)
class ReconciliationReport:
    """Complete immutable result for one pair of fictional sources."""

    left_name: str
    right_name: str
    items: tuple[ReconciliationItem, ...]
    summary: ReconciliationSummary

    def __post_init__(self) -> None:
        left_label = _validate_source_name(self.left_name, field_name="left_name")
        right_label = _validate_source_name(self.right_name, field_name="right_name")
        if left_label == right_label:
            raise ValueError("left_name and right_name must be different")

        object.__setattr__(self, "left_name", left_label)
        object.__setattr__(self, "right_name", right_label)


def _validate_source_name(name: str, *, field_name: str) -> str:
    if not isinstance(name, str):
        raise TypeError(f"{field_name} must be a string")
    return _validate_printable_text(name, field_name=field_name)


def _index_records(
    records: Iterable[ReconciliationRecord],
    *,
    source_name: str,
) -> dict[str, ReconciliationRecord]:
    index: dict[str, ReconciliationRecord] = {}

    try:
        iterator = iter(records)
    except TypeError as exc:
        raise TypeError(f"{source_name} must be an iterable of records") from exc

    for record in iterator:
        if not isinstance(record, ReconciliationRecord):
            raise TypeError(
                f"{source_name} must contain ReconciliationRecord values"
            )
        if record.reference_id in index:
            raise ValueError(
                f"duplicate reference_id in {source_name}: {record.reference_id}"
            )
        index[record.reference_id] = record

    return index


def _build_summary(
    items: Iterable[ReconciliationItem],
) -> ReconciliationSummary:
    item_tuple = tuple(items)

    matched = sum(
        item.status is ReconciliationStatus.MATCHED for item in item_tuple
    )
    amount_mismatches = sum(
        item.status is ReconciliationStatus.AMOUNT_MISMATCH
        for item in item_tuple
    )
    left_only = sum(
        item.status is ReconciliationStatus.LEFT_ONLY for item in item_tuple
    )
    right_only = sum(
        item.status is ReconciliationStatus.RIGHT_ONLY for item in item_tuple
    )
    total_absolute_difference_cents = sum(
        abs(_decimal_to_cents(item.difference))
        for item in item_tuple
        if item.status is ReconciliationStatus.AMOUNT_MISMATCH
        and item.difference is not None
    )
    total_absolute_difference = _cents_to_decimal(
        total_absolute_difference_cents
    )

    return ReconciliationSummary(
        total_items=len(item_tuple),
        matched=matched,
        amount_mismatches=amount_mismatches,
        left_only=left_only,
        right_only=right_only,
        total_absolute_difference=total_absolute_difference,
    )


def reconcile(
    left_records: Iterable[ReconciliationRecord],
    right_records: Iterable[ReconciliationRecord],
    *,
    left_name: str = "Source A",
    right_name: str = "Source B",
) -> ReconciliationReport:
    """Compare two record collections by reference id and exact amount.

    Reference identifiers are matched exactly after surrounding whitespace is
    removed by ``ReconciliationRecord``. Amount differences use the explicit
    contract ``left.amount - right.amount``.
    """

    left_label = _validate_source_name(left_name, field_name="left_name")
    right_label = _validate_source_name(right_name, field_name="right_name")
    if left_label == right_label:
        raise ValueError("left_name and right_name must be different")

    left_index = _index_records(left_records, source_name=left_label)
    right_index = _index_records(right_records, source_name=right_label)

    items: list[ReconciliationItem] = []
    for reference_id in sorted(left_index.keys() | right_index.keys()):
        left = left_index.get(reference_id)
        right = right_index.get(reference_id)

        if left is None:
            items.append(
                ReconciliationItem(
                    reference_id=reference_id,
                    status=ReconciliationStatus.RIGHT_ONLY,
                    left=None,
                    right=right,
                    difference=None,
                )
            )
            continue

        if right is None:
            items.append(
                ReconciliationItem(
                    reference_id=reference_id,
                    status=ReconciliationStatus.LEFT_ONLY,
                    left=left,
                    right=None,
                    difference=None,
                )
            )
            continue

        difference = _subtract_amounts(left.amount, right.amount)
        status = (
            ReconciliationStatus.MATCHED
            if difference == Decimal("0.00")
            else ReconciliationStatus.AMOUNT_MISMATCH
        )
        items.append(
            ReconciliationItem(
                reference_id=reference_id,
                status=status,
                left=left,
                right=right,
                difference=difference,
            )
        )

    item_tuple = tuple(items)
    return ReconciliationReport(
        left_name=left_label,
        right_name=right_label,
        items=item_tuple,
        summary=_build_summary(item_tuple),
    )


def render_text_report(report: ReconciliationReport) -> str:
    """Render a stable, human-readable reconciliation report."""

    if not isinstance(report, ReconciliationReport):
        raise TypeError("report must be a ReconciliationReport")

    lines = [
        "Reconciliation Report",
        f"Sources: {report.left_name} vs {report.right_name}",
        "",
    ]

    for item in report.items:
        if item.status is ReconciliationStatus.MATCHED:
            assert item.left is not None
            assert item.right is not None
            lines.append(
                f"[MATCHED] {item.reference_id}: "
                f"{item.left.amount:.2f} == {item.right.amount:.2f}"
            )
        elif item.status is ReconciliationStatus.AMOUNT_MISMATCH:
            assert item.left is not None
            assert item.right is not None
            assert item.difference is not None
            lines.append(
                f"[AMOUNT_MISMATCH] {item.reference_id}: "
                f"{report.left_name}={item.left.amount:.2f}, "
                f"{report.right_name}={item.right.amount:.2f}, "
                f"difference={item.difference:.2f}"
            )
        elif item.status is ReconciliationStatus.LEFT_ONLY:
            assert item.left is not None
            lines.append(
                f"[LEFT_ONLY] {item.reference_id}: "
                f"{report.left_name}={item.left.amount:.2f}"
            )
        else:
            assert item.right is not None
            lines.append(
                f"[RIGHT_ONLY] {item.reference_id}: "
                f"{report.right_name}={item.right.amount:.2f}"
            )

    summary = report.summary
    lines.extend(
        [
            "",
            "Summary",
            f"Total items: {summary.total_items}",
            f"Matched: {summary.matched}",
            f"Amount mismatches: {summary.amount_mismatches}",
            f"Left only: {summary.left_only}",
            f"Right only: {summary.right_only}",
            (
                "Total absolute difference: "
                f"{summary.total_absolute_difference:.2f}"
            ),
        ]
    )
    return "\n".join(lines) + "\n"
