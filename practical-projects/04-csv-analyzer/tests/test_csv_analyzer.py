from datetime import date
from decimal import Decimal
from io import StringIO

import pytest

from csv_analyzer import (
    EXPECTED_HEADERS,
    CsvFormatError,
    CsvLoadResult,
    CsvSchemaError,
    FieldIssue,
    IncidentRecord,
    IncidentSummary,
    RejectedRow,
    Severity,
    filter_incidents,
    format_analysis,
    load_incident_csv,
    normalize_service,
    parse_boolean,
    parse_incident_csv,
    parse_incident_csv_text,
    parse_iso_date,
    parse_non_negative_integer,
    parse_positive_integer,
    parse_severity,
    summarize_incidents,
)

HEADER = ",".join(EXPECTED_HEADERS)
VALID_ROWS = """event_id,service,severity,duration_minutes,resolved,occurred_on
101,Payments,high,45,true,2026-08-01
102,Portal,medium,20,true,2026-08-02
103,Payments,critical,90,false,2026-08-03
104,Data Sync,low,10,true,2026-08-04
"""


@pytest.mark.parametrize("value", ["1", " 42 ", "0007"])
def test_parse_positive_integer_accepts_ascii_digits(value):
    assert parse_positive_integer(value, "event_id") > 0


@pytest.mark.parametrize("value", ["", "0", "-1", "1.5", "１２"])
def test_parse_positive_integer_rejects_invalid_values(value):
    with pytest.raises(ValueError):
        parse_positive_integer(value, "event_id")


def test_parse_positive_integer_requires_text():
    with pytest.raises(TypeError):
        parse_positive_integer(1, "event_id")


@pytest.mark.parametrize(
    ("value", "expected"),
    [("0", 0), (" 15 ", 15), ("001", 1)],
)
def test_parse_non_negative_integer(value, expected):
    assert parse_non_negative_integer(value, "duration_minutes") == expected


@pytest.mark.parametrize("value", ["-1", "1.2", "", "１２"])
def test_parse_non_negative_integer_rejects_invalid_values(value):
    with pytest.raises(ValueError):
        parse_non_negative_integer(value, "duration_minutes")


def test_normalize_service_collapses_whitespace():
    assert normalize_service("  Data   Sync ") == "Data Sync"


def test_normalize_service_rejects_blank():
    with pytest.raises(ValueError):
        normalize_service(" \t ")


def test_normalize_service_rejects_long_value():
    with pytest.raises(ValueError):
        normalize_service("x" * 61)


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        ("LOW", Severity.LOW),
        (" medium ", Severity.MEDIUM),
        ("Critical", Severity.CRITICAL),
    ],
)
def test_parse_severity_is_case_insensitive(value, expected):
    assert parse_severity(value) is expected


def test_parse_severity_rejects_unknown_value():
    with pytest.raises(ValueError, match="severity must be one of"):
        parse_severity("urgent")


@pytest.mark.parametrize(
    ("value", "expected"),
    [("true", True), (" FALSE ", False)],
)
def test_parse_boolean_uses_strict_true_false(value, expected):
    assert parse_boolean(value, "resolved") is expected


@pytest.mark.parametrize("value", ["yes", "1", "", "truthy"])
def test_parse_boolean_rejects_other_spellings(value):
    with pytest.raises(ValueError):
        parse_boolean(value, "resolved")


def test_parse_iso_date_accepts_leap_day():
    assert parse_iso_date("2024-02-29", "occurred_on") == date(2024, 2, 29)


@pytest.mark.parametrize(
    "value",
    ["2026-2-01", "20260201", "2026-02-30", "２０２６-01-01"],
)
def test_parse_iso_date_rejects_non_contract_values(value):
    with pytest.raises(ValueError):
        parse_iso_date(value, "occurred_on")


def test_incident_record_normalizes_service():
    record = IncidentRecord(
        1,
        "  Data  Sync ",
        Severity.HIGH,
        5,
        True,
        date(2026, 1, 1),
    )
    assert record.service == "Data Sync"


@pytest.mark.parametrize(
    "kwargs",
    [
        {"event_id": 0},
        {"duration_minutes": -1},
        {"resolved": 1},
        {"severity": "high"},
        {"occurred_on": "2026-01-01"},
    ],
)
def test_incident_record_validates_direct_constructor(kwargs):
    data = {
        "event_id": 1,
        "service": "Portal",
        "severity": Severity.HIGH,
        "duration_minutes": 5,
        "resolved": True,
        "occurred_on": date(2026, 1, 1),
    }
    data.update(kwargs)
    with pytest.raises((TypeError, ValueError)):
        IncidentRecord(**data)


def test_parse_valid_csv():
    result = parse_incident_csv_text(VALID_ROWS)
    assert result.valid_count == 4
    assert result.rejected_count == 0
    assert result.records[2].severity is Severity.CRITICAL


def test_parse_csv_accepts_utf8_bom_in_header_text():
    result = parse_incident_csv_text("\ufeff" + VALID_ROWS)
    assert result.valid_count == 4


def test_parse_csv_stream_api():
    assert parse_incident_csv(StringIO(VALID_ROWS)).data_row_count == 4


def test_parse_csv_requires_readable_stream():
    with pytest.raises(TypeError):
        parse_incident_csv("not-a-stream")


def test_parse_csv_text_requires_string():
    with pytest.raises(TypeError):
        parse_incident_csv_text(b"bytes")


def test_schema_requires_header():
    with pytest.raises(CsvSchemaError, match="header row"):
        parse_incident_csv_text("")


def test_schema_requires_exact_header_order():
    text = (
        "service,event_id,severity,duration_minutes,resolved,occurred_on\n"
        "Portal,1,high,5,true,2026-01-01\n"
    )
    with pytest.raises(CsvSchemaError, match="headers must be exactly"):
        parse_incident_csv_text(text)


def test_schema_rejects_duplicate_headers():
    text = (
        "event_id,service,severity,duration_minutes,resolved,resolved\n"
        "1,Portal,high,5,true,2026-01-01\n"
    )
    with pytest.raises(CsvSchemaError, match="must be unique"):
        parse_incident_csv_text(text)


def test_malformed_csv_raises_format_error():
    text = HEADER + '\n1,"Portal,high,5,true,2026-01-01\n'
    with pytest.raises(CsvFormatError):
        parse_incident_csv_text(text)


def test_invalid_fields_are_collected_on_one_rejected_row():
    text = HEADER + "\n0, ,urgent,-2,yes,2026-02-30\n"
    result = parse_incident_csv_text(text)
    rejected = result.rejected_rows[0]
    assert result.valid_count == 0
    assert rejected.row_number == 2
    assert {issue.field for issue in rejected.issues} == {
        "event_id",
        "service",
        "severity",
        "duration_minutes",
        "resolved",
        "occurred_on",
    }


def test_missing_trailing_value_is_rejected():
    result = parse_incident_csv_text(
        HEADER + "\n1,Portal,high,5,true\n"
    )
    assert result.rejected_count == 1
    assert any(
        issue.field == "occurred_on"
        for issue in result.rejected_rows[0].issues
    )


def test_extra_value_is_rejected():
    result = parse_incident_csv_text(
        HEADER + "\n1,Portal,high,5,true,2026-01-01,extra\n"
    )
    assert any(
        issue.field == "_row" for issue in result.rejected_rows[0].issues
    )


def test_duplicate_valid_event_id_rejects_later_row_only():
    text = (
        HEADER
        + "\n1,Portal,high,5,true,2026-01-01"
        + "\n1,Data Sync,low,7,false,2026-01-02\n"
    )
    result = parse_incident_csv_text(text)
    assert result.valid_count == 1
    assert result.rejected_count == 1
    assert "duplicated" in result.rejected_rows[0].issues[0].message


def test_invalid_event_id_does_not_reserve_id_for_later_valid_row():
    text = (
        HEADER
        + "\n1,Portal,urgent,5,true,2026-01-01"
        + "\n1,Data Sync,low,7,false,2026-01-02\n"
    )
    result = parse_incident_csv_text(text)
    assert result.valid_count == 1
    assert result.records[0].service == "Data Sync"


def test_blank_physical_lines_are_ignored_by_csv_reader():
    result = parse_incident_csv_text(
        HEADER + "\n\n1,Portal,high,5,true,2026-01-01\n"
    )
    assert result.valid_count == 1


def test_load_incident_csv_reads_utf8_bom_file(tmp_path):
    path = tmp_path / "incidents.csv"
    path.write_text("\ufeff" + VALID_ROWS, encoding="utf-8")
    assert load_incident_csv(path).valid_count == 4


def test_load_incident_csv_propagates_missing_file(tmp_path):
    with pytest.raises(FileNotFoundError):
        load_incident_csv(tmp_path / "missing.csv")


def test_summary_of_valid_rows():
    summary = summarize_incidents(
        parse_incident_csv_text(VALID_ROWS).records
    )
    assert summary.total_records == 4
    assert summary.resolved_records == 3
    assert summary.unresolved_records == 1
    assert summary.total_duration_minutes == 165
    assert summary.average_duration_minutes == Decimal("41.25")
    assert summary.longest_duration_minutes == 90
    assert summary.severity_counts == (
        (Severity.LOW, 1),
        (Severity.MEDIUM, 1),
        (Severity.HIGH, 1),
        (Severity.CRITICAL, 1),
    )
    assert summary.service_counts == (
        ("Data Sync", 1),
        ("Payments", 2),
        ("Portal", 1),
    )


def test_summary_rounds_half_up_exactly():
    records = tuple(
        IncidentRecord(
            index + 1,
            "A",
            Severity.LOW,
            duration,
            True,
            date(2026, 1, index + 1),
        )
        for index, duration in enumerate((0, 1, 1, 0, 1, 0, 0, 0))
    )
    assert (
        summarize_incidents(records).average_duration_minutes
        == Decimal("0.38")
    )


def test_summary_empty_collection_is_deterministic():
    summary = summarize_incidents(())
    assert summary.total_records == 0
    assert summary.average_duration_minutes == Decimal("0.00")
    assert summary.longest_duration_minutes == 0
    assert summary.service_counts == ()
    assert all(count == 0 for _, count in summary.severity_counts)


def test_summary_requires_records():
    with pytest.raises(TypeError):
        summarize_incidents([object()])


def test_service_counts_are_case_insensitive_but_keep_first_display_form():
    records = (
        IncidentRecord(
            1,
            "Portal",
            Severity.LOW,
            1,
            True,
            date(2026, 1, 1),
        ),
        IncidentRecord(
            2,
            "portal",
            Severity.HIGH,
            2,
            False,
            date(2026, 1, 2),
        ),
    )
    assert summarize_incidents(records).service_counts == (("Portal", 2),)


def test_filter_by_severity():
    records = parse_incident_csv_text(VALID_ROWS).records
    assert [
        item.event_id
        for item in filter_incidents(
            records,
            severity=Severity.CRITICAL,
        )
    ] == [103]


def test_filter_by_resolved():
    records = parse_incident_csv_text(VALID_ROWS).records
    assert [
        item.event_id
        for item in filter_incidents(records, resolved=False)
    ] == [103]


def test_filter_by_service_is_case_insensitive():
    records = parse_incident_csv_text(VALID_ROWS).records
    assert [
        item.event_id
        for item in filter_incidents(records, service=" payments ")
    ] == [101, 103]


def test_filter_combines_criteria():
    records = parse_incident_csv_text(VALID_ROWS).records
    matches = filter_incidents(
        records,
        severity=Severity.HIGH,
        resolved=True,
        service="Payments",
    )
    assert [item.event_id for item in matches] == [101]


def test_filter_rejects_invalid_option_types():
    records = parse_incident_csv_text(VALID_ROWS).records
    with pytest.raises(TypeError):
        filter_incidents(records, severity="high")
    with pytest.raises(TypeError):
        filter_incidents(records, resolved=1)


def test_format_analysis_is_deterministic():
    text = VALID_ROWS + "105,Portal,urgent,5,true,2026-08-05\n"
    result = parse_incident_csv_text(text)
    assert format_analysis(
        result,
        summarize_incidents(result.records),
    ) == "\n".join(
        (
            "data rows: 5",
            "valid: 4",
            "rejected: 1",
            "resolved: 3",
            "unresolved: 1",
            "total duration: 165",
            "average duration: 41.25",
            "longest duration: 90",
        )
    )


def test_format_analysis_requires_matching_summary():
    result = parse_incident_csv_text(VALID_ROWS)
    with pytest.raises(ValueError, match="must match"):
        format_analysis(
            result,
            summarize_incidents(result.records[:1]),
        )


def test_value_objects_validate_their_contracts():
    with pytest.raises(ValueError):
        FieldIssue("", "problem")
    with pytest.raises(ValueError):
        RejectedRow(1, (FieldIssue("x", "problem"),))
    with pytest.raises(ValueError):
        RejectedRow(2, ())
    with pytest.raises(TypeError):
        CsvLoadResult((object(),), ())


def test_incident_summary_rejects_inconsistent_counts():
    with pytest.raises(ValueError):
        IncidentSummary(
            2,
            2,
            1,
            5,
            Decimal("2.50"),
            5,
            (),
            (),
        )


def test_incident_summary_requires_all_severities_in_order():
    with pytest.raises(ValueError, match="every Severity"):
        IncidentSummary(
            0,
            0,
            0,
            0,
            Decimal("0.00"),
            0,
            (),
            (),
        )


def test_incident_summary_rejects_duplicate_service_keys():
    severity_counts = tuple(
        (severity, 2 if severity is Severity.LOW else 0)
        for severity in Severity
    )
    with pytest.raises(ValueError, match="unique case-insensitive"):
        IncidentSummary(
            2,
            1,
            1,
            2,
            Decimal("1.00"),
            1,
            severity_counts,
            (("Portal", 1), ("portal", 1)),
        )


def test_incident_summary_rejects_inconsistent_average():
    severity_counts = tuple(
        (severity, 1 if severity is Severity.LOW else 0)
        for severity in Severity
    )
    with pytest.raises(ValueError, match="average_duration_minutes must match"):
        IncidentSummary(
            1,
            1,
            0,
            5,
            Decimal("99.00"),
            5,
            severity_counts,
            (("Portal", 1),),
        )


def test_incident_summary_rejects_impossible_longest_duration():
    severity_counts = tuple(
        (severity, 2 if severity is Severity.LOW else 0)
        for severity in Severity
    )
    with pytest.raises(ValueError, match="cannot exceed"):
        IncidentSummary(
            2,
            1,
            1,
            5,
            Decimal("2.50"),
            6,
            severity_counts,
            (("Portal", 2),),
        )


def test_incident_summary_rejects_non_normalized_service_names():
    severity_counts = tuple(
        (severity, 1 if severity is Severity.LOW else 0)
        for severity in Severity
    )
    for service in ("   ", " Portal "):
        with pytest.raises(ValueError):
            IncidentSummary(
                1,
                1,
                0,
                5,
                Decimal("5.00"),
                5,
                severity_counts,
                ((service, 1),),
            )
