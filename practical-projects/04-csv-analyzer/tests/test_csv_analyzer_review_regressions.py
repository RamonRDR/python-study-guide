from decimal import Decimal

import pytest

from csv_analyzer import IncidentSummary, Severity


def _two_record_counts():
    severity_counts = tuple(
        (severity, 2 if severity is Severity.LOW else 0)
        for severity in Severity
    )
    service_counts = (("Portal", 2),)
    return severity_counts, service_counts


def test_incident_summary_enforces_minimum_longest_duration():
    severity_counts, service_counts = _two_record_counts()

    with pytest.raises(ValueError, match="too small"):
        IncidentSummary(
            total_records=2,
            resolved_records=1,
            unresolved_records=1,
            total_duration_minutes=10,
            average_duration_minutes=Decimal("5.00"),
            longest_duration_minutes=1,
            severity_counts=severity_counts,
            service_counts=service_counts,
        )


def test_incident_summary_normalizes_average_to_two_decimals():
    severity_counts, service_counts = _two_record_counts()

    for average in (Decimal("5"), Decimal("5.0"), Decimal("5.000")):
        summary = IncidentSummary(
            total_records=2,
            resolved_records=1,
            unresolved_records=1,
            total_duration_minutes=10,
            average_duration_minutes=average,
            longest_duration_minutes=5,
            severity_counts=severity_counts,
            service_counts=service_counts,
        )

        assert summary.average_duration_minutes == Decimal("5.00")
        assert str(summary.average_duration_minutes) == "5.00"
