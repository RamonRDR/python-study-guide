from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from decimal import Decimal
from enum import Enum
from pathlib import Path
from typing import Iterable

MAX_TITLE_LENGTH = 80
MAX_TEAM_LENGTH = 60


class WorkStatus(str, Enum):
    """Workflow states supported by the fictional operational dataset."""

    COMPLETED = "completed"
    IN_PROGRESS = "in_progress"
    BLOCKED = "blocked"


class ReportFormat(str, Enum):
    """Output formats supported by the report renderer."""

    TEXT = "text"
    MARKDOWN = "markdown"


_FORMAT_SUFFIX = {
    ReportFormat.TEXT: ".txt",
    ReportFormat.MARKDOWN: ".md",
}

_MARKDOWN_ESCAPABLE = frozenset("!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~")


def _normalize_readable_text(value: object, field_name: str, max_length: int) -> str:
    if not isinstance(value, str):
        raise TypeError(f"{field_name} must be text")
    normalized = " ".join(value.split())
    if not normalized:
        raise ValueError(f"{field_name} cannot be blank")
    if not normalized.isprintable():
        raise ValueError(f"{field_name} cannot contain control characters")
    if len(normalized) > max_length:
        raise ValueError(f"{field_name} must be at most {max_length} characters")
    return normalized


def _require_plain_date(value: object, field_name: str) -> date:
    if type(value) is not date:
        raise TypeError(f"{field_name} must be a date")
    return value


def _rounded_ratio(numerator: int, denominator: int, scale: int) -> Decimal:
    """Return a non-negative ratio rounded half-up to ``scale`` decimals."""
    if denominator <= 0:
        return Decimal(f"0.{''.join('0' for _ in range(scale))}")

    factor = 10**scale
    units, remainder = divmod(numerator * factor, denominator)
    if remainder * 2 >= denominator:
        units += 1

    whole, fractional = divmod(units, factor)
    return Decimal(f"{whole}.{fractional:0{scale}d}")


def _average_minutes(total_minutes: int, total_records: int) -> Decimal:
    return _rounded_ratio(total_minutes, total_records, 2)


def _completion_percentage(completed_records: int, total_records: int) -> Decimal:
    return _rounded_ratio(completed_records * 100, total_records, 2)


@dataclass(frozen=True, slots=True)
class ActivityRecord:
    """One validated fictional activity used as report source data."""

    activity_id: int
    team: str
    status: WorkStatus
    duration_minutes: int
    occurred_on: date

    def __post_init__(self) -> None:
        if isinstance(self.activity_id, bool) or not isinstance(self.activity_id, int):
            raise TypeError("activity_id must be an integer")
        if self.activity_id <= 0:
            raise ValueError("activity_id must be greater than zero")
        object.__setattr__(
            self,
            "team",
            _normalize_readable_text(self.team, "team", MAX_TEAM_LENGTH),
        )
        if not isinstance(self.status, WorkStatus):
            raise TypeError("status must be a WorkStatus")
        if isinstance(self.duration_minutes, bool) or not isinstance(
            self.duration_minutes, int
        ):
            raise TypeError("duration_minutes must be an integer")
        if self.duration_minutes < 0:
            raise ValueError("duration_minutes cannot be negative")
        _require_plain_date(self.occurred_on, "occurred_on")


@dataclass(frozen=True, slots=True)
class ReportWindow:
    """Inclusive reporting period plus a human-readable title."""

    title: str
    start_date: date
    end_date: date

    def __post_init__(self) -> None:
        object.__setattr__(
            self,
            "title",
            _normalize_readable_text(self.title, "title", MAX_TITLE_LENGTH),
        )
        start = _require_plain_date(self.start_date, "start_date")
        end = _require_plain_date(self.end_date, "end_date")
        if start > end:
            raise ValueError("start_date cannot be after end_date")


@dataclass(frozen=True, slots=True)
class ReportSummary:
    """Validated deterministic aggregates for one reporting window."""

    total_records: int
    completed_records: int
    in_progress_records: int
    blocked_records: int
    total_duration_minutes: int
    average_duration_minutes: Decimal
    longest_duration_minutes: int
    completion_percentage: Decimal
    team_counts: tuple[tuple[str, int], ...]

    def __post_init__(self) -> None:
        count_fields = (
            self.total_records,
            self.completed_records,
            self.in_progress_records,
            self.blocked_records,
            self.total_duration_minutes,
            self.longest_duration_minutes,
        )
        if any(
            isinstance(value, bool) or not isinstance(value, int)
            for value in count_fields
        ):
            raise TypeError("summary count and duration fields must be integers")
        if any(value < 0 for value in count_fields):
            raise ValueError("summary count and duration fields cannot be negative")
        if (
            self.completed_records
            + self.in_progress_records
            + self.blocked_records
            != self.total_records
        ):
            raise ValueError("status counts must equal total_records")

        if not isinstance(self.average_duration_minutes, Decimal):
            raise TypeError("average_duration_minutes must be a Decimal")
        if not isinstance(self.completion_percentage, Decimal):
            raise TypeError("completion_percentage must be a Decimal")

        expected_average = _average_minutes(
            self.total_duration_minutes,
            self.total_records,
        )
        expected_completion = _completion_percentage(
            self.completed_records,
            self.total_records,
        )
        if self.average_duration_minutes != expected_average:
            raise ValueError(
                "average_duration_minutes must match total_duration_minutes and total_records"
            )
        if self.completion_percentage != expected_completion:
            raise ValueError(
                "completion_percentage must match completed_records and total_records"
            )

        object.__setattr__(self, "average_duration_minutes", expected_average)
        object.__setattr__(self, "completion_percentage", expected_completion)

        if self.total_records == 0:
            if self.total_duration_minutes != 0 or self.longest_duration_minutes != 0:
                raise ValueError("empty summaries must have zero duration values")
        else:
            minimum_longest = (
                self.total_duration_minutes + self.total_records - 1
            ) // self.total_records
            if self.longest_duration_minutes < minimum_longest:
                raise ValueError(
                    "longest_duration_minutes is too small for the recorded total duration"
                )
            if self.longest_duration_minutes > self.total_duration_minutes:
                raise ValueError(
                    "longest_duration_minutes cannot exceed total_duration_minutes"
                )

        if not isinstance(self.team_counts, tuple):
            raise TypeError("team_counts must be a tuple")
        for item in self.team_counts:
            if (
                not isinstance(item, tuple)
                or len(item) != 2
                or not isinstance(item[0], str)
                or isinstance(item[1], bool)
                or not isinstance(item[1], int)
                or item[1] <= 0
            ):
                raise TypeError("team_counts must contain (str, positive int) pairs")
            if _normalize_readable_text(item[0], "team", MAX_TEAM_LENGTH) != item[0]:
                raise ValueError("team_counts names must already be normalized")

        team_keys = tuple(team.casefold() for team, _ in self.team_counts)
        if len(team_keys) != len(set(team_keys)):
            raise ValueError("team_counts must use unique case-insensitive team names")
        if team_keys != tuple(sorted(team_keys)):
            raise ValueError("team_counts must be sorted case-insensitively")
        if sum(count for _, count in self.team_counts) != self.total_records:
            raise ValueError("team counts must equal total_records")


@dataclass(frozen=True, slots=True)
class OperationalReport:
    """One immutable report containing source counts, records, and summary."""

    window: ReportWindow
    source_record_count: int
    records: tuple[ActivityRecord, ...]
    summary: ReportSummary

    def __post_init__(self) -> None:
        if not isinstance(self.window, ReportWindow):
            raise TypeError("window must be a ReportWindow")
        if isinstance(self.source_record_count, bool) or not isinstance(
            self.source_record_count, int
        ):
            raise TypeError("source_record_count must be an integer")
        if self.source_record_count < 0:
            raise ValueError("source_record_count cannot be negative")
        if not isinstance(self.records, tuple) or any(
            not isinstance(record, ActivityRecord) for record in self.records
        ):
            raise TypeError("records must be a tuple of ActivityRecord values")
        if not isinstance(self.summary, ReportSummary):
            raise TypeError("summary must be a ReportSummary")
        if self.source_record_count < len(self.records):
            raise ValueError("source_record_count cannot be smaller than included records")
        if self.summary.total_records != len(self.records):
            raise ValueError("summary total must equal the number of included records")

        expected_order = tuple(
            sorted(self.records, key=lambda record: (record.occurred_on, record.activity_id))
        )
        if self.records != expected_order:
            raise ValueError("records must be sorted by occurred_on and activity_id")

        seen_ids: set[int] = set()
        for record in self.records:
            if record.activity_id in seen_ids:
                raise ValueError("included activity_id values must be unique")
            seen_ids.add(record.activity_id)
            if not self.window.start_date <= record.occurred_on <= self.window.end_date:
                raise ValueError("included records must fall inside the report window")

        if self.summary != summarize_activities(self.records):
            raise ValueError("summary must match the included records")

    @property
    def included_record_count(self) -> int:
        return len(self.records)

    @property
    def excluded_record_count(self) -> int:
        return self.source_record_count - self.included_record_count


def _validate_source_records(records: Iterable[ActivityRecord]) -> tuple[ActivityRecord, ...]:
    try:
        source = tuple(records)
    except TypeError as exc:
        raise TypeError("records must be an iterable of ActivityRecord values") from exc

    if any(not isinstance(record, ActivityRecord) for record in source):
        raise TypeError("records must contain only ActivityRecord values")

    seen_ids: set[int] = set()
    for record in source:
        if record.activity_id in seen_ids:
            raise ValueError(f"activity_id {record.activity_id} is duplicated")
        seen_ids.add(record.activity_id)
    return source


def summarize_activities(records: Iterable[ActivityRecord]) -> ReportSummary:
    """Summarize already validated activity records deterministically."""
    values = _validate_source_records(records)
    status_counts = {status: 0 for status in WorkStatus}
    total_duration = 0
    longest_duration = 0
    teams: dict[str, tuple[str, int]] = {}

    for record in values:
        status_counts[record.status] += 1
        total_duration += record.duration_minutes
        longest_duration = max(longest_duration, record.duration_minutes)
        key = record.team.casefold()
        display_name, count = teams.get(key, (record.team, 0))
        teams[key] = (display_name, count + 1)

    team_counts = tuple(
        (display_name, count)
        for _, (display_name, count) in sorted(teams.items(), key=lambda item: item[0])
    )
    total = len(values)
    completed = status_counts[WorkStatus.COMPLETED]
    return ReportSummary(
        total_records=total,
        completed_records=completed,
        in_progress_records=status_counts[WorkStatus.IN_PROGRESS],
        blocked_records=status_counts[WorkStatus.BLOCKED],
        total_duration_minutes=total_duration,
        average_duration_minutes=_average_minutes(total_duration, total),
        longest_duration_minutes=longest_duration,
        completion_percentage=_completion_percentage(completed, total),
        team_counts=team_counts,
    )


def build_report(
    records: Iterable[ActivityRecord],
    *,
    title: str,
    start_date: date,
    end_date: date,
) -> OperationalReport:
    """Filter source records by an inclusive period and build one report."""
    source = _validate_source_records(records)
    window = ReportWindow(title=title, start_date=start_date, end_date=end_date)
    included = tuple(
        sorted(
            (
                record
                for record in source
                if window.start_date <= record.occurred_on <= window.end_date
            ),
            key=lambda record: (record.occurred_on, record.activity_id),
        )
    )
    return OperationalReport(
        window=window,
        source_record_count=len(source),
        records=included,
        summary=summarize_activities(included),
    )


def _render_team_lines(summary: ReportSummary) -> list[str]:
    if not summary.team_counts:
        return ["- none"]
    return [f"- {team}: {count}" for team, count in summary.team_counts]


def render_text_report(report: OperationalReport) -> str:
    """Render one deterministic plain-text report."""
    if not isinstance(report, OperationalReport):
        raise TypeError("report must be an OperationalReport")

    summary = report.summary
    lines = [
        report.window.title,
        "=" * len(report.window.title),
        f"period: {report.window.start_date.isoformat()} to {report.window.end_date.isoformat()}",
        f"source records: {report.source_record_count}",
        f"included records: {report.included_record_count}",
        f"excluded records: {report.excluded_record_count}",
        "",
        "SUMMARY",
        f"completed: {summary.completed_records}",
        f"in progress: {summary.in_progress_records}",
        f"blocked: {summary.blocked_records}",
        f"completion: {summary.completion_percentage:.2f}%",
        f"total duration: {summary.total_duration_minutes} min",
        f"average duration: {summary.average_duration_minutes:.2f} min",
        f"longest duration: {summary.longest_duration_minutes} min",
        "",
        "TEAMS",
        *_render_team_lines(summary),
        "",
        "RECORDS",
    ]

    if not report.records:
        lines.append("- none")
    else:
        lines.extend(
            f"- {record.occurred_on.isoformat()} | {record.activity_id} | "
            f"{record.team} | {record.status.value} | {record.duration_minutes} min"
            for record in report.records
        )
    return "\n".join(lines) + "\n"


def _escape_markdown_text(value: str) -> str:
    """Escape CommonMark punctuation so validated text renders literally."""
    return "".join(
        f"\\{character}" if character in _MARKDOWN_ESCAPABLE else character
        for character in value
    )


def render_markdown_report(report: OperationalReport) -> str:
    """Render one deterministic Markdown report."""
    if not isinstance(report, OperationalReport):
        raise TypeError("report must be an OperationalReport")

    summary = report.summary
    lines = [
        f"# {_escape_markdown_text(report.window.title)}",
        "",
        f"**Period:** {report.window.start_date.isoformat()} to {report.window.end_date.isoformat()}",
        "",
        "## Summary",
        "",
        "| Metric | Value |",
        "|---|---:|",
        f"| Source records | {report.source_record_count} |",
        f"| Included records | {report.included_record_count} |",
        f"| Excluded records | {report.excluded_record_count} |",
        f"| Completed | {summary.completed_records} |",
        f"| In progress | {summary.in_progress_records} |",
        f"| Blocked | {summary.blocked_records} |",
        f"| Completion | {summary.completion_percentage:.2f}% |",
        f"| Total duration | {summary.total_duration_minutes} min |",
        f"| Average duration | {summary.average_duration_minutes:.2f} min |",
        f"| Longest duration | {summary.longest_duration_minutes} min |",
        "",
        "## Teams",
        "",
    ]

    if not summary.team_counts:
        lines.append("_No teams in this reporting period._")
    else:
        lines.extend(
            f"- {_escape_markdown_text(team)}: {count}"
            for team, count in summary.team_counts
        )

    lines.extend(["", "## Records", ""])
    if not report.records:
        lines.append("_No records in this reporting period._")
    else:
        lines.extend(
            [
                "| Date | ID | Team | Status | Duration |",
                "|---|---:|---|---|---:|",
            ]
        )
        lines.extend(
            f"| {record.occurred_on.isoformat()} | {record.activity_id} | "
            f"{_escape_markdown_text(record.team)} | {record.status.value} | "
            f"{record.duration_minutes} min |"
            for record in report.records
        )
    return "\n".join(lines) + "\n"


def render_report(report: OperationalReport, output_format: ReportFormat) -> str:
    """Render a report through an explicit output-format boundary."""
    if not isinstance(output_format, ReportFormat):
        raise TypeError("output_format must be a ReportFormat")
    if output_format is ReportFormat.TEXT:
        return render_text_report(report)
    return render_markdown_report(report)


def write_report(
    report: OperationalReport,
    path: str | Path,
    output_format: ReportFormat,
) -> Path:
    """Write one report as UTF-8 without creating missing directories."""
    if not isinstance(output_format, ReportFormat):
        raise TypeError("output_format must be a ReportFormat")
    if not isinstance(path, (str, Path)):
        raise TypeError("path must be a string or Path")

    destination = Path(path)
    expected_suffix = _FORMAT_SUFFIX[output_format]
    if destination.suffix.casefold() != expected_suffix:
        raise ValueError(
            f"{output_format.value} reports must use the {expected_suffix} suffix"
        )

    destination.write_text(
        render_report(report, output_format),
        encoding="utf-8",
        newline="\n",
    )
    return destination