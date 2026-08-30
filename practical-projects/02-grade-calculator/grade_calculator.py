from __future__ import annotations

from dataclasses import dataclass
from decimal import Context, Decimal, InvalidOperation, ROUND_HALF_UP
from typing import Iterable

HUNDRED = Decimal("100.00")
ZERO = Decimal("0.00")
TWO_DECIMAL_PLACES = Decimal("0.01")


def normalize_text(value: str, field_name: str) -> str:
    """Strip surrounding whitespace and reject blank text."""
    if not isinstance(value, str):
        raise TypeError(f"{field_name} must be text")

    normalized = value.strip()
    if not normalized:
        raise ValueError(f"{field_name} cannot be blank")
    return normalized


def _decimal_context_for(value: Decimal) -> Context:
    """Return a local context large enough to quantize the supplied value."""
    digits = len(value.as_tuple().digits)
    if value.is_zero():
        precision = max(digits + 2, 4)
    else:
        expanded_precision = value.adjusted() + 3
        precision = max(digits + 2, expanded_precision, 4)
    return Context(prec=precision, rounding=ROUND_HALF_UP)


def parse_percentage(
    value: Decimal | str | int,
    field_name: str,
    *,
    allow_zero: bool,
) -> Decimal:
    """Return a finite percentage from 0 to 100 using two decimal places."""
    if isinstance(value, bool):
        raise TypeError(f"{field_name} must be a decimal number")

    try:
        amount = value if isinstance(value, Decimal) else Decimal(str(value))
    except (InvalidOperation, ValueError) as exc:
        raise ValueError(f"{field_name} must be a valid decimal number") from exc

    if not amount.is_finite():
        raise ValueError(f"{field_name} must be finite")
    if amount < 0 or (amount == 0 and not allow_zero):
        comparison = "between 0 and 100" if allow_zero else "greater than 0 and at most 100"
        raise ValueError(f"{field_name} must be {comparison}")
    if amount > 100:
        raise ValueError(f"{field_name} must be at most 100")

    try:
        rounded = amount.quantize(
            TWO_DECIMAL_PLACES,
            context=_decimal_context_for(amount),
        )
    except InvalidOperation as exc:
        raise ValueError(
            f"{field_name} cannot be represented with two decimal places"
        ) from exc

    if rounded < 0 or (rounded == 0 and not allow_zero):
        comparison = "between 0 and 100" if allow_zero else "round to at least 0.01"
        raise ValueError(f"{field_name} must be {comparison}")
    if rounded > 100:
        raise ValueError(f"{field_name} must be at most 100")
    return rounded


def _to_hundredths(value: Decimal) -> int:
    """Convert a validated two-decimal Decimal to an exact integer."""
    decimal_tuple = value.as_tuple()
    if decimal_tuple.exponent != -2:
        raise ValueError("normalized percentage must have exactly two decimal places")

    coefficient = 0
    for digit in decimal_tuple.digits:
        coefficient = coefficient * 10 + digit

    return -coefficient if decimal_tuple.sign else coefficient


def _from_hundredths(value: int) -> Decimal:
    """Build an exact two-decimal Decimal without using arithmetic context."""
    digits = tuple(int(digit) for digit in str(abs(value)))
    sign = 1 if value < 0 else 0
    return Decimal((sign, digits, -2))


def _round_ratio_half_up(numerator: int, denominator: int) -> int:
    """Round a non-negative integer ratio to the nearest integer, half up."""
    quotient, remainder = divmod(numerator, denominator)
    if remainder * 2 >= denominator:
        quotient += 1
    return quotient


@dataclass(frozen=True, slots=True)
class GradeBand:
    """One letter-grade boundary."""

    label: str
    minimum_score: Decimal

    def __post_init__(self) -> None:
        object.__setattr__(self, "label", normalize_text(self.label, "label"))
        object.__setattr__(
            self,
            "minimum_score",
            parse_percentage(self.minimum_score, "minimum_score", allow_zero=True),
        )

    @classmethod
    def create(
        cls,
        label: str,
        minimum_score: Decimal | str | int,
    ) -> "GradeBand":
        return cls(label=label, minimum_score=minimum_score)


@dataclass(frozen=True, slots=True)
class GradePolicy:
    """Configurable letter-grade and passing-score rules."""

    bands: tuple[GradeBand, ...]
    passing_score: Decimal = Decimal("60.00")

    def __post_init__(self) -> None:
        normalized_bands = tuple(self.bands)
        if not normalized_bands:
            raise ValueError("grade policy must contain at least one band")
        if not all(isinstance(band, GradeBand) for band in normalized_bands):
            raise TypeError("bands must contain GradeBand values")

        labels = [band.label.casefold() for band in normalized_bands]
        if len(labels) != len(set(labels)):
            raise ValueError("grade band labels must be unique")

        thresholds = [_to_hundredths(band.minimum_score) for band in normalized_bands]
        if thresholds != sorted(thresholds, reverse=True):
            raise ValueError("grade bands must be ordered from highest to lowest")
        if len(thresholds) != len(set(thresholds)):
            raise ValueError("grade band minimum scores must be unique")
        if thresholds[-1] != 0:
            raise ValueError("the lowest grade band must start at 0.00")

        object.__setattr__(self, "bands", normalized_bands)
        object.__setattr__(
            self,
            "passing_score",
            parse_percentage(self.passing_score, "passing_score", allow_zero=True),
        )

    def classify(self, score: Decimal | str | int) -> str:
        """Return the label for a validated score."""
        normalized_score = parse_percentage(score, "score", allow_zero=True)
        score_hundredths = _to_hundredths(normalized_score)

        for band in self.bands:
            if score_hundredths >= _to_hundredths(band.minimum_score):
                return band.label

        raise RuntimeError("grade policy does not cover the validated score")

    def is_passing(self, score: Decimal | str | int) -> bool:
        """Return whether a validated score meets the passing boundary."""
        normalized_score = parse_percentage(score, "score", allow_zero=True)
        return _to_hundredths(normalized_score) >= _to_hundredths(self.passing_score)


DEFAULT_POLICY = GradePolicy(
    bands=(
        GradeBand.create("A", "90"),
        GradeBand.create("B", "80"),
        GradeBand.create("C", "70"),
        GradeBand.create("D", "60"),
        GradeBand.create("F", "0"),
    ),
    passing_score=Decimal("60.00"),
)


@dataclass(frozen=True, slots=True)
class Assessment:
    """One validated graded assessment and its course weight."""

    name: str
    score: Decimal
    weight: Decimal

    def __post_init__(self) -> None:
        object.__setattr__(self, "name", normalize_text(self.name, "name"))
        object.__setattr__(
            self,
            "score",
            parse_percentage(self.score, "score", allow_zero=True),
        )
        object.__setattr__(
            self,
            "weight",
            parse_percentage(self.weight, "weight", allow_zero=False),
        )

    @classmethod
    def create(
        cls,
        name: str,
        score: Decimal | str | int,
        weight: Decimal | str | int,
    ) -> "Assessment":
        return cls(name=name, score=score, weight=weight)


@dataclass(frozen=True, slots=True)
class GradeReport:
    """Read-only snapshot of the calculator's current grading state."""

    assessment_count: int
    total_weight: Decimal
    remaining_weight: Decimal
    average: Decimal
    letter_grade: str
    complete: bool
    passed: bool | None


class GradeCalculator:
    """Aggregate weighted assessments under one explicit grade policy."""

    def __init__(
        self,
        policy: GradePolicy = DEFAULT_POLICY,
        assessments: Iterable[Assessment] = (),
    ) -> None:
        if not isinstance(policy, GradePolicy):
            raise TypeError("policy must be a GradePolicy")

        self._policy = policy
        self._assessments: list[Assessment] = []
        for assessment in assessments:
            self._append_validated(assessment)

    @property
    def policy(self) -> GradePolicy:
        return self._policy

    @property
    def assessments(self) -> tuple[Assessment, ...]:
        return tuple(self._assessments)

    def _append_validated(self, assessment: Assessment) -> None:
        if not isinstance(assessment, Assessment):
            raise TypeError("assessments must contain Assessment values")

        next_weight = self._total_weight_hundredths() + _to_hundredths(assessment.weight)
        if next_weight > 10000:
            raise ValueError("total assessment weight cannot exceed 100.00")
        self._assessments.append(assessment)

    def add(
        self,
        name: str,
        score: Decimal | str | int,
        weight: Decimal | str | int,
    ) -> Assessment:
        """Validate and append one assessment without allowing overweight totals."""
        assessment = Assessment.create(name, score, weight)
        self._append_validated(assessment)
        return assessment

    def _total_weight_hundredths(self) -> int:
        return sum(_to_hundredths(item.weight) for item in self._assessments)

    def total_weight(self) -> Decimal:
        return _from_hundredths(self._total_weight_hundredths())

    def remaining_weight(self) -> Decimal:
        return _from_hundredths(10000 - self._total_weight_hundredths())

    def average(self) -> Decimal:
        """Return the weighted average normalized over assessments entered so far."""
        total_weight = self._total_weight_hundredths()
        if total_weight == 0:
            raise ValueError("cannot calculate an average without assessments")

        weighted_total = sum(
            _to_hundredths(item.score) * _to_hundredths(item.weight)
            for item in self._assessments
        )
        average_hundredths = _round_ratio_half_up(weighted_total, total_weight)
        return _from_hundredths(average_hundredths)

    def report(self) -> GradeReport:
        """Return a progress report; pass/fail is final only at 100% weight."""
        average = self.average()
        total_weight = self.total_weight()
        complete = _to_hundredths(total_weight) == 10000

        return GradeReport(
            assessment_count=len(self._assessments),
            total_weight=total_weight,
            remaining_weight=self.remaining_weight(),
            average=average,
            letter_grade=self._policy.classify(average),
            complete=complete,
            passed=self._policy.is_passing(average) if complete else None,
        )

    def final_report(self) -> GradeReport:
        """Return a final report only when assessments cover exactly 100%."""
        if self._total_weight_hundredths() != 10000:
            raise ValueError("final report requires exactly 100.00 total weight")
        return self.report()


def format_report(report: GradeReport) -> str:
    """Render a deterministic human-readable report without side effects."""
    status = "complete" if report.complete else "in progress"
    passed = "n/a" if report.passed is None else ("yes" if report.passed else "no")
    return "\n".join(
        (
            f"assessments: {report.assessment_count}",
            f"weight: {report.total_weight:.2f}",
            f"remaining: {report.remaining_weight:.2f}",
            f"average: {report.average:.2f}",
            f"letter: {report.letter_grade}",
            f"status: {status}",
            f"passed: {passed}",
        )
    )
