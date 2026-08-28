from datetime import datetime, timedelta, timezone

brt = timezone(timedelta(hours=-3))
local = datetime(2026, 8, 27, 18, 30, tzinfo=brt)
utc = local.astimezone(timezone.utc)

print(local.isoformat())
print(utc.isoformat())
