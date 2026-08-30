from decimal import Decimal, Inexact, localcontext

import pytest

from grade_calculator import (
    Assessment,
    GradeBand,
    GradeCalculator,
    GradePolicy,
    format_report,
    parse_percentage,
)


def test_parse_percentage_rounds_half_up() -> None:
    assert parse_percentage("89.995", "score", allow_zero=True) == Decimal("90.00")


def test_parse_percentage_isolated_from_caller_decimal_context() -> None:
    with localcontext() as context:
        context.prec = 3
        context.traps[Inexact] = True
        assert parse_percentage("25.905", "score", allow_zero=True) == Decimal("25.91")


@pytest.mark.parametrize("value", ["1E2", Decimal("1E2")])
def test_parse_percentage_accepts_scientific_notation_at_upper_bound(
    value: str | Decimal,
) -> None:
    assert parse_percentage(value, "score", allow_zero=True) == Decimal("100.00")


@pytest.mark.parametrize("value", ["NaN", "Infinity", "-0.01", "100.01"])
def test_parse_percentage_rejects_invalid_scores(value: str) -> None:
    with pytest.raises(ValueError):
        parse_percentage(value, "score", allow_zero=True)


def test_parse_percentage_rejects_bool() -> None:
    with pytest.raises(TypeError, match="decimal number"):
        parse_percentage(True, "score", allow_zero=True)


def test_positive_percentage_rejects_value_that_rounds_to_zero() -> None:
    with pytest.raises(ValueError, match="at least 0.01"):
        parse_percentage("0.004", "weight", allow_zero=False)


def test_assessment_constructor_enforces_normalization() -> None:
    assessment = Assessment("  Quiz  ", Decimal("87.235"), Decimal("10"))

    assert assessment.name == "Quiz"
    assert assessment.score == Decimal("87.24")
    assert assessment.weight == Decimal("10.00")


def test_grade_policy_rejects_duplicate_labels() -> None:
    with pytest.raises(ValueError, match="labels must be unique"):
        GradePolicy(
            bands=(
                GradeBand.create("A", "90"),
                GradeBand.create("a", "0"),
            )
        )


def test_grade_policy_rejects_unordered_thresholds() -> None:
    with pytest.raises(ValueError, match="highest to lowest"):
        GradePolicy(
            bands=(
                GradeBand.create("B", "80"),
                GradeBand.create("A", "90"),
                GradeBand.create("F", "0"),
            )
        )


def test_grade_policy_requires_zero_floor() -> None:
    with pytest.raises(ValueError, match="start at 0.00"):
        GradePolicy(
            bands=(
                GradeBand.create("A", "90"),
                GradeBand.create("F", "50"),
            )
        )


@pytest.mark.parametrize(
    ("score", "expected"),
    [
        ("100", "A"),
        ("90", "A"),
        ("89.99", "B"),
        ("80", "B"),
        ("70", "C"),
        ("60", "D"),
        ("59.99", "F"),
        ("0", "F"),
    ],
)
def test_default_policy_classifies_boundaries(score: str, expected: str) -> None:
    calculator = GradeCalculator()
    assert calculator.policy.classify(score) == expected


def test_add_rejects_weight_above_100_without_mutation() -> None:
    calculator = GradeCalculator()
    calculator.add("Project", "90", "80")

    with pytest.raises(ValueError, match="cannot exceed 100.00"):
        calculator.add("Final", "95", "20.01")

    assert len(calculator.assessments) == 1
    assert calculator.total_weight() == Decimal("80.00")


def test_average_requires_at_least_one_assessment() -> None:
    with pytest.raises(ValueError, match="without assessments"):
        GradeCalculator().average()


def test_partial_average_is_normalized_over_entered_weight() -> None:
    calculator = GradeCalculator()
    calculator.add("Quiz", "80", "10")
    calculator.add("Project", "100", "30")

    report = calculator.report()

    assert report.total_weight == Decimal("40.00")
    assert report.remaining_weight == Decimal("60.00")
    assert report.average == Decimal("95.00")
    assert report.letter_grade == "A"
    assert report.complete is False
    assert report.passed is None


def test_weighted_average_rounds_half_up_with_integer_arithmetic() -> None:
    calculator = GradeCalculator()
    calculator.add("Assessment A", "89.99", "33.33")
    calculator.add("Assessment B", "90.00", "66.67")

    assert calculator.average() == Decimal("90.00")


def test_final_report_requires_exactly_100_percent_weight() -> None:
    calculator = GradeCalculator()
    calculator.add("Project", "90", "99.99")

    with pytest.raises(ValueError, match="exactly 100.00"):
        calculator.final_report()


def test_final_report_calculates_grade_and_pass_status() -> None:
    calculator = GradeCalculator()
    calculator.add("Homework", "82.50", "20")
    calculator.add("Midterm", "91", "30")
    calculator.add("Project", "88.25", "20")
    calculator.add("Final exam", "94", "30")

    report = calculator.final_report()

    assert report.average == Decimal("89.65")
    assert report.letter_grade == "B"
    assert report.complete is True
    assert report.passed is True
    assert report.remaining_weight == Decimal("0.00")


def test_custom_policy_changes_classification_and_passing_rule() -> None:
    policy = GradePolicy(
        bands=(
            GradeBand.create("Excellent", "85"),
            GradeBand.create("Satisfactory", "70"),
            GradeBand.create("Needs Improvement", "0"),
        ),
        passing_score=Decimal("70"),
    )
    calculator = GradeCalculator(policy)
    calculator.add("Coursework", "72", "100")

    report = calculator.final_report()

    assert report.letter_grade == "Satisfactory"
    assert report.passed is True


def test_constructor_rejects_invalid_assessment_iterable_without_partial_state() -> None:
    valid = Assessment.create("Quiz", "80", "20")

    with pytest.raises(TypeError, match="Assessment values"):
        GradeCalculator(assessments=(valid, "not-an-assessment"))


def test_constructor_rejects_overweight_assessment_collection() -> None:
    first = Assessment.create("Project", "90", "60")
    second = Assessment.create("Final", "95", "40.01")

    with pytest.raises(ValueError, match="cannot exceed 100.00"):
        GradeCalculator(assessments=(first, second))


def test_assessments_property_does_not_expose_internal_list() -> None:
    calculator = GradeCalculator()
    calculator.add("Quiz", "80", "10")

    assert isinstance(calculator.assessments, tuple)


def test_format_report_is_deterministic() -> None:
    calculator = GradeCalculator()
    calculator.add("Coursework", "72", "100")

    assert format_report(calculator.final_report()) == "\n".join(
        (
            "assessments: 1",
            "weight: 100.00",
            "remaining: 0.00",
            "average: 72.00",
            "letter: C",
            "status: complete",
            "passed: yes",
        )
    )
