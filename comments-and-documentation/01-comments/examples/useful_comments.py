# Comments are most useful when they preserve reasoning that the code alone
# cannot communicate clearly.

from datetime import date, timedelta


start_date = date(2030, 5, 3)
next_reminder_date = start_date + timedelta(days=1)

# The fictional support team does not answer messages on weekends, so move
# reminders to the next weekday instead of sending a message with no coverage.
while next_reminder_date.weekday() >= 5:
    next_reminder_date += timedelta(days=1)

print(f"Next reminder: {next_reminder_date.isoformat()}")
