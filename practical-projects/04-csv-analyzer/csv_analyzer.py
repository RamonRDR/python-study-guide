from __future__ import annotations

import csv
import io
from dataclasses import dataclass
from datetime import date
from decimal import Decimal
from enum import Enum
from pathlib import Path
from typing import Iterable, TextIO

EXPECTED_HEADERS = (
    "event_id",
    "service",
    "severity",
    "duration_minutes",
    "resolved",
    "occurred_on",
)
MAX_SERVICE_LENGTH = 60


class CsvSchemaError(ValueError):
    """Raised when a CSV file does not match the expected column schema."""


class CsvFormatError(ValueError):
    """Raised when Python's CSV parser rejects the document structure."""


class Severity(str, Enum):
    """Severity values supported by the fictional incident dataset."""

    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


def _require_text(value: object, field_name: str) -> str:
    if not isinstance(value, str):
        raise TypeError(f"{field_name} must be text")
    return value


def parse_positive_integer(value: object, field_name: str) -> int:
    """Parse one strictly positive base-10 integer."""
    text = _require_text(value, field_name).strip()
    if not text or not text.isascii() or not text.isdigit():
        raise ValueError(f"{field_name} must be a positive integer")
    parsed = int(text)
    if parsed <= 0:
        raise ValueError(f"{field_name} must be greater than zero")
    return parsed


def parse_non_negative_integer(value: object, field_name: str) -> int:
    """Parse one non-negative base-10 integer."""
    text = _require_text(value, field_name).strip()
    if not text or not text.isascii() or not text.isdigit():
        raise ValueError(f"{field_name} must be a non-negative integer")
    return int(text)


def normalize_service(value: object) -> str:
    """Normalize readable service text while preserving casing."""
    normalized = " ".join(_require_text(value, "service").split())
    if not normalized:
        raise ValueError("service cannot be blank")
    if len(normalized) > MAX_SERVICE_LENGTH:
        raise ValueError(f"service must be at most {MAX_SERVICE_LENGTH} characters")
    return normalized


def parse_severity(value: object) -> Severity:
    """Parse a case-insensitive severity value."""
    text = _require_text(value, "severity").strip().casefold()
    try:
        return Severity(text)
    except ValueError as exc:
        allowed = ", ".join(item.value for item in Severity)
        raise ValueError(f"severity must be one of: {allowed}") from exc


def parse_boolean(value: object, field_name: str) -> bool:
    """Parse this project's strict true/false CSV Boolean contract."""
    text = _require_text(value, field_name).strip().casefold()
    if text == "true":
        return True
    if text == "false":
        return False
    raise ValueError(f"{field_name} must be 'true' or 'false'")


def parse_iso_date(value: object, field_name: str) -> date:
    """Parse an exact YYYY-MM-DD calendar date."""
    text = _require_text(value, field_name).strip()
    if (
        len(text) != 10
        or text[4] != "-"
        or text[7] != "-"
        or not text.isascii()
        or not text[:4].isdigit()
        or not text[5:7].isdigit()
        or not text[8:].isdigit()
    ):
        raise ValueError(f"{field_name} must use YYYY-MM-DD")
    try:
        parsed = date.fromisoformat(text)
    except ValueError as exc:
        raise ValueError(f"{field_name} must be a valid calendar date") from exc
    if parsed.isoformat() != text:
        raise ValueError(f"{field_name} must use YYYY-MM-DD")
    return parsed


@dataclass(frozen=True, slots=True)
class IncidentRecord:
    """One validated incident row."""

    event_id: int
    service: str
    severity: Severity
    duration_minutes: int
    resolved: bool
    occurred_on: date

    def __post_init__(self) -> None:
        if isinstance(self.event_id, bool) or not isinstance(self.event_id, int):
            raise TypeError("event_id must be an integer")
        if self.event_id <= 0:
            raise ValueError("event_id must be greater than zero")
        object.__setattr__(self, "service", normalize_service(self.service))
        if not isinstance(self.severity, Severity):
            raise TypeError("severity must be a Severity")
        if isinstance(self.duration_minutes, bool) or not isinstance(
            self.duration_minutes, int
        ):
            raise TypeError("duration_minutes must be an integer")
        if self.duration_minutes < 0:
            raise ValueError("duration_minutes cannot be negative")
        if not isinstance(self.resolved, bool):
            raise TypeError("resolved must be a Boolean")
        if not isinstance(self.occurred_on, date):
            raise TypeError("occurred_on must be a date")


@dataclass(frozen=True, slots=True)
class FieldIssue:
    """One validation problem attached to a rejected logical CSV row."""

    field: str
    message: str

    def __post_init__(self) -> None:
        field = _require_text(self.field, "field").strip()
        message = _require_text(self.message, "message").strip()
        if not field:
            raise ValueError("field cannot be blank")
        if not message:
            raise ValueError("message cannot be blank")
        object.__setattr__(self, "field", field)
        object.__setattr__(self, "message", message)


@dataclass(frozen=True, slots=True)
class RejectedRow:
    """One logical CSV row that failed one or more validation checks."""

    row_number: int
    issues: tuple[FieldIssue, ...]

    def __post_init__(self) -> None:
        if isinstance(self.row_number, bool) or not isinstance(self.row_number, int):
            raise TypeError("row_number must be an integer")
        if self.row_number < 2:
            raise ValueError("row_number must be at least 2")
        if not isinstance(self.issues, tuple) or not self.issues:
            raise ValueError("issues must be a non-empty tuple")
        if any(not isinstance(issue, FieldIssue) for issue in self.issues):
            raise TypeError("issues must contain FieldIssue values")


@dataclass(frozen=True, slots=True)
class CsvLoadResult:
    """Validated records plus logical rows rejected for data problems."""

    records: tuple[IncidentRecord, ...]
    rejected_rows: tuple[RejectedRow, ...]

    def __post_init__(self) -> None:
        if not isinstance(self.records, tuple) or any(
            not isinstance(value, IncidentRecord) for value in self.records
        ):
            raise TypeError("records must be a tuple of IncidentRecord values")
        if not isinstance(self.rejected_rows, tuple) or any(
            not isinstance(value, RejectedRow) for value in self.rejected_rows
        ):
            raise TypeError("rejected_rows must be a tuple of RejectedRow values")

    @property
    def valid_count(self) -> int:
        return len(self.records)

    @property
    def rejected_count(self) -> int:
        return len(self.rejected_rows)

    @property
    def data_row_count(self) -> int:
        return self.valid_count + self.rejected_count


@dataclass(frozen=True, slots=True)
class IncidentSummary:
    """Deterministic aggregate statistics for validated records."""

    total_records: int
    resolved_records: int
    unresolved_records: int
    total_duration_minutes: int
    average_duration_minutes: Decimal
    longest_duration_minutes: int
    severity_counts: tuple[tuple[Severity, int], ...]
    service_counts: tuple[tuple[str, int], ...]

    def __post_init__(self) -> None:
        integer_fields = (
            self.total_records,
            self.resolved_records,
            self.unresolved_records,
            self.total_duration_minutes,
            self.longest_duration_minutes,
        )
        if any(
            isinstance(value, bool) or not isinstance(value, int)
            for value in integer_fields
        ):
            raise TypeError("summary count and duration fields must be integers")
        if any(value < 0 for value in integer_fields):
            raise ValueError("summary count and duration fields cannot be negative")
        if self.resolved_records + self.unresolved_records != self.total_records:
            raise ValueError("resolved and unresolved counts must equal total_records")
        if not isinstance(self.average_duration_minutes, Decimal):
            raise TypeError("average_duration_minutes must be a Decimal")
        if self.average_duration_minutes < 0:
            raise ValueError("average_duration_minutes cannot be negative")
        if self.total_records == 0:
            expected_average = Decimal("0.00")
            if self.total_duration_minutes != 0 or self.longest_duration_minutes != 0:
                raise ValueError(
                    "empty summaries must have zero total and longest duration"
                )
        else:
            hundredths, remainder = divmod(
                self.total_duration_minutes * 100,
                self.total_records,
            )
            if remainder * 2 >= self.total_records:
                hundredths += 1
            expected_average = Decimal(
                f"{hundredths // 100}.{hundredths % 100:02d}"
            )
            minimum_longest = (
                self.total_duration_minutes + self.total_records - 1
            ) // self.total_records
            if self.longest_duration_minutes < minimum_longest:
                raise ValueError(
                    "longest_duration_minutes is too small for "
                    "total_duration_minutes and total_records"
                )
            if self.longest_duration_minutes > self.total_duration_minutes:
                raise ValueError(
                    "longest_duration_minutes cannot exceed total_duration_minutes"
                )

        if self.average_duration_minutes != expected_average:
            raise ValueError(
                "average_duration_minutes must match total_duration_minutes "
                "and total_records"
            )
        object.__setattr__(
            self,
            "average_duration_minutes",
            expected_average,
        )
        if not isinstance(self.severity_counts, tuple) or any(
            not isinstance(item, tuple)
            or len(item) != 2
            or not isinstance(item[0], Severity)
            or isinstance(item[1], bool)
            or not isinstance(item[1], int)
            or item[1] < 0
            for item in self.severity_counts
        ):
            raise TypeError(
                "severity_counts must contain (Severity, non-negative int) pairs"
            )
        expected_severities = tuple(Severity)
        if (
            tuple(severity for severity, _ in self.severity_counts)
            != expected_severities
        ):
            raise ValueError(
                "severity_counts must contain every Severity exactly once"
            )
        if sum(count for _, count in self.severity_counts) != self.total_records:
            raise ValueError("severity counts must equal total_records")
        if not isinstance(self.service_counts, tuple) or any(
            not isinstance(item, tuple)
            or len(item) != 2
            or not isinstance(item[0], str)
            or not item[0]
            or isinstance(item[1], bool)
            or not isinstance(item[1], int)
            or item[1] <= 0
            for item in self.service_counts
        ):
            raise TypeError(
                "service_counts must contain (non-blank str, positive int) pairs"
            )
        if any(
            normalize_service(service) != service
            for service, _ in self.service_counts
        ):
            raise ValueError(
                "service_counts service names must be normalized"
            )
        service_keys = tuple(
            service.casefold() for service, _ in self.service_counts
        )
        if len(service_keys) != len(set(service_keys)):
            raise ValueError(
                "service_counts must use unique case-insensitive services"
            )
        if tuple(sorted(service_keys)) != service_keys:
            raise ValueError("service_counts must be sorted case-insensitively")
        if sum(count for _, count in self.service_counts) != self.total_records:
            raise ValueError("service counts must equal total_records")


def _validate_headers(fieldnames: list[str] | None) -> None:
    if fieldnames is None:
        raise CsvSchemaError("CSV document must contain a header row")
    normalized = list(fieldnames)
    if normalized and normalized[0].startswith("\ufeff"):
        normalized[0] = normalized[0].removeprefix("\ufeff")
    if len(normalized) != len(set(normalized)):
        raise CsvSchemaError("CSV header names must be unique")
    if tuple(normalized) != EXPECTED_HEADERS:
        expected = ", ".join(EXPECTED_HEADERS)
        actual = ", ".join(normalized)
        raise CsvSchemaError(
            f"CSV headers must be exactly: {expected}; "
            f"received: {actual or '<empty>'}"
        )
    fieldnames[:] = normalized


def _parse_field(row, field, parser, issues):
    try:
        return parser(row.get(field))
    except (TypeError, ValueError) as exc:
        issues.append(FieldIssue(field, str(exc)))
        return None


def _build_record(
    row: dict[str | None, object],
    row_number: int,
    seen_ids: set[int],
):
    issues: list[FieldIssue] = []
    if row.get(None):
        issues.append(
            FieldIssue(
                "_row",
                "row contains more values than the schema allows",
            )
        )
    event_id = _parse_field(
        row,
        "event_id",
        lambda value: parse_positive_integer(value, "event_id"),
        issues,
    )
    service = _parse_field(row, "service", normalize_service, issues)
    severity = _parse_field(row, "severity", parse_severity, issues)
    duration = _parse_field(
        row,
        "duration_minutes",
        lambda value: parse_non_negative_integer(value, "duration_minutes"),
        issues,
    )
    resolved = _parse_field(
        row,
        "resolved",
        lambda value: parse_boolean(value, "resolved"),
        issues,
    )
    occurred_on = _parse_field(
        row,
        "occurred_on",
        lambda value: parse_iso_date(value, "occurred_on"),
        issues,
    )
    if event_id is not None and event_id in seen_ids:
        issues.append(
            FieldIssue("event_id", f"event_id {event_id} is duplicated")
        )
    if issues:
        return None, RejectedRow(row_number, tuple(issues))
    record = IncidentRecord(
        event_id,
        service,
        severity,
        duration,
        resolved,
        occurred_on,
    )
    seen_ids.add(record.event_id)
    return record, None


def parse_incident_csv(stream: TextIO) -> CsvLoadResult:
    """Parse a text stream, keeping valid rows and collecting data errors."""
    if not hasattr(stream, "read"):
        raise TypeError("stream must be a readable text stream")
    try:
        reader = csv.DictReader(stream, strict=True)
        _validate_headers(reader.fieldnames)
        records: list[IncidentRecord] = []
        rejected: list[RejectedRow] = []
        seen_ids: set[int] = set()
        for row_number, row in enumerate(reader, start=2):
            record, rejected_row = _build_record(row, row_number, seen_ids)
            if record is not None:
                records.append(record)
            elif rejected_row is not None:
                rejected.append(rejected_row)
    except csv.Error as exc:
        raise CsvFormatError(f"CSV structure is malformed: {exc}") from exc
    return CsvLoadResult(tuple(records), tuple(rejected))


def parse_incident_csv_text(text: str) -> CsvLoadResult:
    """Parse CSV content already available as text."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    return parse_incident_csv(io.StringIO(text, newline=""))


def load_incident_csv(path: str | Path) -> CsvLoadResult:
    """Load a UTF-8 CSV file, accepting an optional UTF-8 BOM."""
    with Path(path).open("r", encoding="utf-8-sig", newline="") as stream:
        return parse_incident_csv(stream)


def _average_to_decimal(total: int, count: int) -> Decimal:
    if count == 0:
        return Decimal("0.00")
    hundredths, remainder = divmod(total * 100, count)
    if remainder * 2 >= count:
        hundredths += 1
    return Decimal(f"{hundredths // 100}.{hundredths % 100:02d}")


def summarize_incidents(
    records: Iterable[IncidentRecord],
) -> IncidentSummary:
    """Aggregate validated incident rows into deterministic statistics."""
    values = tuple(records)
    if any(not isinstance(record, IncidentRecord) for record in values):
        raise TypeError("records must contain IncidentRecord values")
    total = len(values)
    resolved = sum(record.resolved for record in values)
    total_duration = sum(record.duration_minutes for record in values)
    longest = max(
        (record.duration_minutes for record in values),
        default=0,
    )
    severity_map = {severity: 0 for severity in Severity}
    service_map: dict[str, int] = {}
    display_names: dict[str, str] = {}
    for record in values:
        severity_map[record.severity] += 1
        key = record.service.casefold()
        display_names.setdefault(key, record.service)
        service_map[key] = service_map.get(key, 0) + 1
    return IncidentSummary(
        total_records=total,
        resolved_records=resolved,
        unresolved_records=total - resolved,
        total_duration_minutes=total_duration,
        average_duration_minutes=_average_to_decimal(total_duration, total),
        longest_duration_minutes=longest,
        severity_counts=tuple(
            (severity, severity_map[severity]) for severity in Severity
        ),
        service_counts=tuple(
            (display_names[key], service_map[key])
            for key in sorted(service_map)
        ),
    )


def filter_incidents(
    records: Iterable[IncidentRecord],
    *,
    severity: Severity | None = None,
    resolved: bool | None = None,
    service: str | None = None,
) -> tuple[IncidentRecord, ...]:
    """Filter validated rows without mutating the input collection."""
    values = tuple(records)
    if any(not isinstance(record, IncidentRecord) for record in values):
        raise TypeError("records must contain IncidentRecord values")
    if severity is not None and not isinstance(severity, Severity):
        raise TypeError("severity must be a Severity or None")
    if resolved is not None and not isinstance(resolved, bool):
        raise TypeError("resolved must be a Boolean or None")
    service_key = (
        None if service is None else normalize_service(service).casefold()
    )
    return tuple(
        record
        for record in values
        if (severity is None or record.severity is severity)
        and (resolved is None or record.resolved is resolved)
        and (
            service_key is None
            or record.service.casefold() == service_key
        )
    )


def format_analysis(
    result: CsvLoadResult,
    summary: IncidentSummary,
) -> str:
    """Return a stable plain-text report for demo and CLI-style reuse."""
    if not isinstance(result, CsvLoadResult):
        raise TypeError("result must be a CsvLoadResult")
    if not isinstance(summary, IncidentSummary):
        raise TypeError("summary must be an IncidentSummary")
    if summary.total_records != result.valid_count:
        raise ValueError(
            "summary total_records must match result.valid_count"
        )
    return "\n".join(
        (
            f"data rows: {result.data_row_count}",
            f"valid: {result.valid_count}",
            f"rejected: {result.rejected_count}",
            f"resolved: {summary.resolved_records}",
            f"unresolved: {summary.unresolved_records}",
            f"total duration: {summary.total_duration_minutes}",
            f"average duration: {summary.average_duration_minutes}",
            f"longest duration: {summary.longest_duration_minutes}",
        )
    )