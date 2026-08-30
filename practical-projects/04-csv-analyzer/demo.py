from csv_analyzer import (
    Severity,
    filter_incidents,
    format_analysis,
    parse_incident_csv_text,
    summarize_incidents,
)

CSV_TEXT = """event_id,service,severity,duration_minutes,resolved,occurred_on
101,Payments,high,45,true,2026-08-01
102,Portal,medium,20,true,2026-08-02
103,Payments,critical,90,false,2026-08-03
104,Data Sync,low,10,true,2026-08-04
105,Portal,urgent,15,true,2026-08-05
106,Portal,high,30,false,2026-02-30
"""

result = parse_incident_csv_text(CSV_TEXT)
summary = summarize_incidents(result.records)

print(format_analysis(result, summary))
print(
    f"critical: {len(filter_incidents(result.records, severity=Severity.CRITICAL))}"
)
