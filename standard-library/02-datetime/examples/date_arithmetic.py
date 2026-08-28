from datetime import date, timedelta

start = date(2026, 8, 27)
deadline = start + timedelta(days=10)

print(start.isoformat())
print(deadline.isoformat())
print((deadline - start).days)
