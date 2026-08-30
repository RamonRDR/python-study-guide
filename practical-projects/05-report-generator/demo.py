from datetime import date

from report_generator import (
    ActivityRecord,
    ReportFormat,
    WorkStatus,
    build_report,
    render_report,
)


def main() -> None:
    records = (
        ActivityRecord(
            activity_id=101,
            team="Accounting",
            status=WorkStatus.COMPLETED,
            duration_minutes=30,
            occurred_on=date(2026, 8, 1),
        ),
        ActivityRecord(
            activity_id=102,
            team="Accounting",
            status=WorkStatus.IN_PROGRESS,
            duration_minutes=10,
            occurred_on=date(2026, 8, 2),
        ),
        ActivityRecord(
            activity_id=103,
            team="Tax",
            status=WorkStatus.BLOCKED,
            duration_minutes=20,
            occurred_on=date(2026, 8, 3),
        ),
        ActivityRecord(
            activity_id=104,
            team="Treasury",
            status=WorkStatus.COMPLETED,
            duration_minutes=40,
            occurred_on=date(2026, 7, 31),
        ),
    )

    report = build_report(
        records,
        title="August Operations",
        start_date=date(2026, 8, 1),
        end_date=date(2026, 8, 31),
    )
    print(render_report(report, ReportFormat.TEXT), end="")


if __name__ == "__main__":
    main()
