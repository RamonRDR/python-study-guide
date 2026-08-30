from dataclasses import replace
from datetime import date, datetime
from decimal import Decimal

import pytest

from report_generator import (
    MAX_TEAM_LENGTH,
    MAX_TITLE_LENGTH,
    ActivityRecord,
    OperationalReport,
    ReportFormat,
    ReportSummary,
    ReportWindow,
    WorkStatus,
    build_report,
    render_markdown_report,
    render_report,
    render_text_report,
    summarize_activities,
    write_report,
)


def make_record(
    activity_id: int,
    *,
    team: str = "Accounting",
    status: WorkStatus = WorkStatus.COMPLETED,
    duration_minutes: int = 30,
    occurred_on: date = date(2026, 8, 1),
) -> ActivityRecord:
    return ActivityRecord(
        activity_id=activity_id,
        team=team,
        status=status,
        duration_minutes=duration_minutes,
        occurred_on=occurred_on,
    )


def make_report() -> OperationalReport:
    records = (
        make_record(
            103,
            team="Tax",
            status=WorkStatus.BLOCKED,
            duration_minutes=20,
            occurred_on=date(2026, 8, 3),
        ),
        make_record(
            101,
            team="Accounting",
            status=WorkStatus.COMPLETED,
            duration_minutes=30,
            occurred_on=date(2026, 8, 1),
        ),
        make_record(
            102,
            team="Accounting",
            status=WorkStatus.IN_PROGRESS,
            duration_minutes=10,
            occurred_on=date(2026, 8, 2),
        ),
        make_record(
            104,
            team="Treasury",
            status=WorkStatus.COMPLETED,
            duration_minutes=40,
            occurred_on=date(2026, 7, 31),
        ),
    )
    return build_report(
        records,
        title="August Operations",
        start_date=date(2026, 8, 1),
        end_date=date(2026, 8, 31),
    )


def test_activity_record_normalizes_team_whitespace() -> None:
    record = make_record(1, team="  Shared   Services  ")
    assert record.team == "Shared Services"


@pytest.mark.parametrize("activity_id", [0, -1])
def test_activity_record_rejects_non_positive_id(activity_id: int) -> None:
    with pytest.raises(ValueError, match="greater than zero"):
        make_record(activity_id)


@pytest.mark.parametrize("activity_id", [True, 1.5, "1", None])
def test_activity_record_rejects_non_integer_id(activity_id: object) -> None:
    with pytest.raises(TypeError, match="activity_id must be an integer"):
        make_record(activity_id)  # type: ignore[arg-type]


@pytest.mark.parametrize("team", ["", "   ", "\n\t"])
def test_activity_record_rejects_blank_team(team: str) -> None:
    with pytest.raises(ValueError, match="team cannot be blank"):
        make_record(1, team=team)


def test_activity_record_rejects_team_over_limit() -> None:
    with pytest.raises(ValueError, match=f"at most {MAX_TEAM_LENGTH}"):
        make_record(1, team="x" * (MAX_TEAM_LENGTH + 1))


def test_activity_record_rejects_non_text_team() -> None:
    with pytest.raises(TypeError, match="team must be text"):
        make_record(1, team=123)  # type: ignore[arg-type]


def test_activity_record_rejects_plain_string_status() -> None:
    with pytest.raises(TypeError, match="status must be a WorkStatus"):
        make_record(1, status="completed")  # type: ignore[arg-type]


@pytest.mark.parametrize("duration", [-1, -50])
def test_activity_record_rejects_negative_duration(duration: int) -> None:
    with pytest.raises(ValueError, match="cannot be negative"):
        make_record(1, duration_minutes=duration)


@pytest.mark.parametrize("duration", [True, 1.5, "30", None])
def test_activity_record_rejects_non_integer_duration(duration: object) -> None:
    with pytest.raises(TypeError, match="duration_minutes must be an integer"):
        make_record(1, duration_minutes=duration)  # type: ignore[arg-type]


def test_activity_record_accepts_zero_duration() -> None:
    assert make_record(1, duration_minutes=0).duration_minutes == 0


@pytest.mark.parametrize(
    "occurred_on",
    ["2026-08-01", datetime(2026, 8, 1, 12, 0), None],
)
def test_activity_record_requires_plain_date(occurred_on: object) -> None:
    with pytest.raises(TypeError, match="occurred_on must be a date"):
        make_record(1, occurred_on=occurred_on)  # type: ignore[arg-type]


def test_report_window_normalizes_title() -> None:
    window = ReportWindow("  Monthly   Close  ", date(2026, 8, 1), date(2026, 8, 31))
    assert window.title == "Monthly Close"


@pytest.mark.parametrize("title", ["", "   "])
def test_report_window_rejects_blank_title(title: str) -> None:
    with pytest.raises(ValueError, match="title cannot be blank"):
        ReportWindow(title, date(2026, 8, 1), date(2026, 8, 31))


def test_report_window_rejects_title_over_limit() -> None:
    with pytest.raises(ValueError, match=f"at most {MAX_TITLE_LENGTH}"):
        ReportWindow("x" * (MAX_TITLE_LENGTH + 1), date(2026, 8, 1), date(2026, 8, 31))


def test_report_window_rejects_reversed_dates() -> None:
    with pytest.raises(ValueError, match="start_date cannot be after end_date"):
        ReportWindow("Report", date(2026, 8, 31), date(2026, 8, 1))


@pytest.mark.parametrize("field", ["start", "end"])
def test_report_window_requires_plain_dates(field: str) -> None:
    start = datetime(2026, 8, 1) if field == "start" else date(2026, 8, 1)
    end = datetime(2026, 8, 31) if field == "end" else date(2026, 8, 31)
    with pytest.raises(TypeError, match=f"{field}_date must be a date"):
        ReportWindow("Report", start, end)  # type: ignore[arg-type]


def test_summarize_empty_records() -> None:
    summary = summarize_activities(())
    assert summary == ReportSummary(
        total_records=0,
        completed_records=0,
        in_progress_records=0,
        blocked_records=0,
        total_duration_minutes=0,
        average_duration_minutes=Decimal("0.00"),
        longest_duration_minutes=0,
        completion_percentage=Decimal("0.00"),
        team_counts=(),
    )


def test_summarize_calculates_counts_duration_and_percentages() -> None:
    records = (
        make_record(1, status=WorkStatus.COMPLETED, duration_minutes=10),
        make_record(2, status=WorkStatus.COMPLETED, duration_minutes=20),
        make_record(3, status=WorkStatus.BLOCKED, duration_minutes=1),
    )
    summary = summarize_activities(records)
    assert summary.total_records == 3
    assert summary.completed_records == 2
    assert summary.in_progress_records == 0
    assert summary.blocked_records == 1
    assert summary.total_duration_minutes == 31
    assert summary.average_duration_minutes == Decimal("10.33")
    assert summary.longest_duration_minutes == 20
    assert summary.completion_percentage == Decimal("66.67")


def test_summarize_rounds_half_up_without_global_decimal_context() -> None:
    records = (
        make_record(1, duration_minutes=0),
        make_record(2, duration_minutes=0),
        make_record(3, duration_minutes=1),
        make_record(4, duration_minutes=1),
        make_record(5, duration_minutes=1),
        make_record(6, duration_minutes=0),
        make_record(7, duration_minutes=0),
        make_record(8, duration_minutes=0),
    )
    assert summarize_activities(records).average_duration_minutes == Decimal("0.38")


def test_summarize_groups_teams_case_insensitively_and_keeps_first_spelling() -> None:
    records = (
        make_record(1, team="Accounting"),
        make_record(2, team="accounting"),
        make_record(3, team="Tax"),
    )
    assert summarize_activities(records).team_counts == (("Accounting", 2), ("Tax", 1))


def test_summarize_sorts_team_counts_case_insensitively() -> None:
    records = (
        make_record(1, team="Treasury"),
        make_record(2, team="accounting"),
        make_record(3, team="Tax"),
    )
    assert summarize_activities(records).team_counts == (
        ("accounting", 1),
        ("Tax", 1),
        ("Treasury", 1),
    )


def test_summarize_rejects_duplicate_activity_ids() -> None:
    with pytest.raises(ValueError, match="activity_id 1 is duplicated"):
        summarize_activities((make_record(1), make_record(1, team="Tax")))


def test_summarize_rejects_non_record_values() -> None:
    with pytest.raises(TypeError, match="only ActivityRecord"):
        summarize_activities((make_record(1), object()))  # type: ignore[arg-type]


def test_summarize_accepts_generator_input() -> None:
    summary = summarize_activities(make_record(value) for value in (1, 2, 3))
    assert summary.total_records == 3


def test_build_report_filters_inclusive_window_and_sorts_records() -> None:
    report = make_report()
    assert [record.activity_id for record in report.records] == [101, 102, 103]
    assert report.source_record_count == 4
    assert report.included_record_count == 3
    assert report.excluded_record_count == 1


def test_build_report_includes_both_date_boundaries() -> None:
    records = (
        make_record(1, occurred_on=date(2026, 8, 1)),
        make_record(2, occurred_on=date(2026, 8, 31)),
        make_record(3, occurred_on=date(2026, 9, 1)),
    )
    report = build_report(
        records,
        title="August",
        start_date=date(2026, 8, 1),
        end_date=date(2026, 8, 31),
    )
    assert [record.activity_id for record in report.records] == [1, 2]


def test_build_report_can_produce_empty_period() -> None:
    report = build_report(
        (make_record(1, occurred_on=date(2026, 7, 1)),),
        title="August",
        start_date=date(2026, 8, 1),
        end_date=date(2026, 8, 31),
    )
    assert report.included_record_count == 0
    assert report.excluded_record_count == 1
    assert report.summary.total_records == 0


def test_build_report_rejects_duplicate_ids_even_when_one_is_outside_window() -> None:
    records = (
        make_record(1, occurred_on=date(2026, 8, 1)),
        make_record(1, occurred_on=date(2026, 7, 1)),
    )
    with pytest.raises(ValueError, match="activity_id 1 is duplicated"):
        build_report(
            records,
            title="August",
            start_date=date(2026, 8, 1),
            end_date=date(2026, 8, 31),
        )


def test_operational_report_rejects_summary_with_wrong_total() -> None:
    report = make_report()
    wrong_summary = summarize_activities(report.records[:2])
    with pytest.raises(ValueError, match="summary total"):
        OperationalReport(
            window=report.window,
            source_record_count=report.source_record_count,
            records=report.records,
            summary=wrong_summary,
        )

    same_size_wrong_summary = summarize_activities(
        (
            make_record(
                201,
                team="Different",
                status=WorkStatus.COMPLETED,
                duration_minutes=20,
                occurred_on=date(2026, 8, 1),
            ),
            make_record(
                202,
                team="Different",
                status=WorkStatus.COMPLETED,
                duration_minutes=20,
                occurred_on=date(2026, 8, 2),
            ),
            make_record(
                203,
                team="Different",
                status=WorkStatus.COMPLETED,
                duration_minutes=20,
                occurred_on=date(2026, 8, 3),
            ),
        )
    )
    with pytest.raises(ValueError, match="summary must match"):
        OperationalReport(
            window=report.window,
            source_record_count=report.source_record_count,
            records=report.records,
            summary=same_size_wrong_summary,
        )


def test_operational_report_rejects_unsorted_records() -> None:
    report = make_report()
    with pytest.raises(ValueError, match="records must be sorted"):
        OperationalReport(
            window=report.window,
            source_record_count=report.source_record_count,
            records=tuple(reversed(report.records)),
            summary=report.summary,
        )


def test_operational_report_rejects_included_record_outside_window() -> None:
    record = make_record(1, occurred_on=date(2026, 7, 31))
    window = ReportWindow("August", date(2026, 8, 1), date(2026, 8, 31))
    with pytest.raises(ValueError, match="inside the report window"):
        OperationalReport(
            window=window,
            source_record_count=1,
            records=(record,),
            summary=summarize_activities((record,)),
        )


def test_report_summary_rejects_status_arithmetic_mismatch() -> None:
    summary = summarize_activities((make_record(1),))
    with pytest.raises(ValueError, match="status counts"):
        replace(summary, blocked_records=1)


def test_report_summary_rejects_wrong_average() -> None:
    summary = summarize_activities((make_record(1),))
    with pytest.raises(ValueError, match="average_duration_minutes"):
        replace(summary, average_duration_minutes=Decimal("29.99"))


def test_report_summary_rejects_wrong_completion_percentage() -> None:
    summary = summarize_activities((make_record(1),))
    with pytest.raises(ValueError, match="completion_percentage"):
        replace(summary, completion_percentage=Decimal("99.99"))


def test_report_summary_rejects_non_decimal_metrics() -> None:
    summary = summarize_activities((make_record(1),))
    with pytest.raises(TypeError, match="average_duration_minutes"):
        replace(summary, average_duration_minutes=30.0)  # type: ignore[arg-type]
    with pytest.raises(TypeError, match="completion_percentage"):
        replace(summary, completion_percentage=100.0)  # type: ignore[arg-type]


def test_report_summary_rejects_unsorted_team_counts() -> None:
    summary = summarize_activities((make_record(1, team="Alpha"), make_record(2, team="Beta")))
    with pytest.raises(ValueError, match="sorted case-insensitively"):
        replace(summary, team_counts=(("Beta", 1), ("Alpha", 1)))


def test_report_summary_rejects_duplicate_casefolded_team_names() -> None:
    summary = summarize_activities((make_record(1), make_record(2)))
    with pytest.raises(ValueError, match="unique case-insensitive"):
        replace(summary, team_counts=(("Accounting", 1), ("accounting", 1)))


def test_report_summary_rejects_team_total_mismatch() -> None:
    summary = summarize_activities((make_record(1),))
    with pytest.raises(ValueError, match="team counts must equal"):
        replace(summary, team_counts=(("Accounting", 2),))


def test_render_text_report_is_deterministic() -> None:
    text = render_text_report(make_report())
    assert text == (
        "August Operations\n"
        "=================\n"
        "period: 2026-08-01 to 2026-08-31\n"
        "source records: 4\n"
        "included records: 3\n"
        "excluded records: 1\n"
        "\n"
        "SUMMARY\n"
        "completed: 1\n"
        "in progress: 1\n"
        "blocked: 1\n"
        "completion: 33.33%\n"
        "total duration: 60 min\n"
        "average duration: 20.00 min\n"
        "longest duration: 30 min\n"
        "\n"
        "TEAMS\n"
        "- Accounting: 2\n"
        "- Tax: 1\n"
        "\n"
        "RECORDS\n"
        "- 2026-08-01 | 101 | Accounting | completed | 30 min\n"
        "- 2026-08-02 | 102 | Accounting | in_progress | 10 min\n"
        "- 2026-08-03 | 103 | Tax | blocked | 20 min\n"
    )


def test_render_text_report_handles_empty_period() -> None:
    report = build_report(
        (),
        title="Empty",
        start_date=date(2026, 8, 1),
        end_date=date(2026, 8, 31),
    )
    text = render_text_report(report)
    assert "TEAMS\n- none" in text
    assert "RECORDS\n- none" in text


def test_render_text_report_rejects_wrong_type() -> None:
    with pytest.raises(TypeError, match="OperationalReport"):
        render_text_report(object())  # type: ignore[arg-type]


def test_render_markdown_report_contains_stable_tables() -> None:
    markdown = render_markdown_report(make_report())
    assert markdown.startswith("# August Operations\n")
    assert "| Completion | 33.33% |" in markdown
    assert "| 2026-08-01 | 101 | Accounting | completed | 30 min |" in markdown
    assert markdown.endswith("\n")

    escaped_title_report = build_report(
        (),
        title="# *Ops* [Report](x) <tag>",
        start_date=date(2026, 8, 1),
        end_date=date(2026, 8, 31),
    )
    escaped_title_markdown = render_markdown_report(escaped_title_report)
    assert escaped_title_markdown.startswith(
        "# \\# \\*Ops\\* \\[Report\\]\\(x\\) \\<tag\\>\n"
    )


def test_render_markdown_report_escapes_team_table_delimiters() -> None:
    report = build_report(
        (make_record(1, team=r"Ops | Core\\Team"),),
        title="Escaping",
        start_date=date(2026, 8, 1),
        end_date=date(2026, 8, 1),
    )
    markdown = render_markdown_report(report)
    assert r"Ops \| Core\\\\Team" in markdown


def test_render_markdown_report_handles_empty_period() -> None:
    report = build_report(
        (),
        title="Empty",
        start_date=date(2026, 8, 1),
        end_date=date(2026, 8, 31),
    )
    markdown = render_markdown_report(report)
    assert "_No teams in this reporting period._" in markdown
    assert "_No records in this reporting period._" in markdown


@pytest.mark.parametrize(
    ("output_format", "renderer"),
    [
        (ReportFormat.TEXT, render_text_report),
        (ReportFormat.MARKDOWN, render_markdown_report),
    ],
)
def test_render_report_dispatches_to_explicit_format(output_format, renderer) -> None:
    report = make_report()
    assert render_report(report, output_format) == renderer(report)


def test_render_report_requires_report_format_enum() -> None:
    with pytest.raises(TypeError, match="ReportFormat"):
        render_report(make_report(), "text")  # type: ignore[arg-type]


@pytest.mark.parametrize(
    ("output_format", "filename"),
    [
        (ReportFormat.TEXT, "report.txt"),
        (ReportFormat.MARKDOWN, "report.md"),
    ],
)
def test_write_report_writes_utf8_content(tmp_path, output_format, filename) -> None:
    destination = tmp_path / filename
    returned = write_report(make_report(), destination, output_format)
    assert returned == destination
    assert destination.read_text(encoding="utf-8") == render_report(
        make_report(), output_format
    )


@pytest.mark.parametrize(
    ("output_format", "filename"),
    [
        (ReportFormat.TEXT, "report.md"),
        (ReportFormat.MARKDOWN, "report.txt"),
        (ReportFormat.TEXT, "report"),
    ],
)
def test_write_report_rejects_wrong_suffix(output_format, filename, tmp_path) -> None:
    with pytest.raises(ValueError, match="reports must use"):
        write_report(make_report(), tmp_path / filename, output_format)


def test_write_report_accepts_case_insensitive_suffix(tmp_path) -> None:
    destination = tmp_path / "REPORT.TXT"
    write_report(make_report(), destination, ReportFormat.TEXT)
    assert destination.exists()


def test_write_report_does_not_create_missing_directories(tmp_path) -> None:
    destination = tmp_path / "missing" / "report.txt"
    with pytest.raises(FileNotFoundError):
        write_report(make_report(), destination, ReportFormat.TEXT)


def test_write_report_rejects_non_path_value(tmp_path) -> None:
    with pytest.raises(TypeError, match="path must be"):
        write_report(make_report(), 123, ReportFormat.TEXT)  # type: ignore[arg-type]


def test_write_report_requires_report_format_enum(tmp_path) -> None:
    with pytest.raises(TypeError, match="ReportFormat"):
        write_report(make_report(), tmp_path / "report.txt", "text")  # type: ignore[arg-type]