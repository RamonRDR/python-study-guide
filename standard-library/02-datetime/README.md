# Working with Dates and Time Calculations Using `datetime`

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

Python's `datetime` module provides explicit objects for dates, clock times, combined date-and-time values, durations, fixed UTC offsets, parsing, formatting, comparison, and arithmetic.

Strings such as `"2026-08-27"` are useful for storage and communication, but they do not automatically know how many days separate two dates, whether a year is a leap year, or how to add a duration safely. The `datetime` module gives those concepts dedicated types and rules.

For most beginner and intermediate work, the central imports are:

```python
from datetime import date, datetime, time, timedelta, timezone
```

## Learning goals

By the end of this chapter, you should be able to:

- distinguish `date`, `time`, `datetime`, and `timedelta`;
- construct date and time objects explicitly;
- inspect year, month, day, hour, minute, and second components;
- use `date.today()` and `datetime.now()` deliberately;
- perform date and datetime arithmetic with `timedelta`;
- understand the difference between `timedelta.seconds` and `timedelta.total_seconds()`;
- parse text with `strptime()` and format objects with `strftime()`;
- use ISO-oriented helpers such as `fromisoformat()` and `isoformat()`;
- distinguish naive and timezone-aware `datetime` objects;
- represent UTC and fixed offsets with `timezone`;
- convert aware datetimes with `astimezone()`;
- understand why assigning `tzinfo` is not the same as converting a time;
- avoid treating fixed durations as calendar-month rules;
- recognize when real-world time zones require the companion `zoneinfo` module.

## 1. Why use dedicated date and time types?

Consider two strings:

```python
start = "2026-08-27"
end = "2026-09-03"
```

A human can see that they look like dates, but Python still sees ordinary strings.

With `date`, the meaning is explicit:

```python
from datetime import date

start = date(2026, 8, 27)
end = date(2026, 9, 3)

print(end - start)
```

The subtraction produces a `timedelta`, because Python now knows that the values represent calendar dates.

The main design idea is:

```text
text for representation
        !=
objects for date/time behavior
```

## 2. The central classes

The most commonly used classes are:

| Class | Represents |
|---|---|
| `date` | a calendar date: year, month, day |
| `time` | a clock time without a calendar date |
| `datetime` | a date and clock time together |
| `timedelta` | a duration between points in time |
| `timezone` | a fixed offset from UTC |

These classes solve related problems, but they are not interchangeable.

## 3. Creating a `date`

Construct a date with year, month, and day:

```python
from datetime import date

release_date = date(2026, 8, 27)

print(release_date.year)
print(release_date.month)
print(release_date.day)
```

Invalid calendar values fail immediately:

```python
from datetime import date

try:
    impossible = date(2026, 2, 30)
except ValueError:
    print("Invalid calendar date")
```

That validation is one advantage of using a date type instead of carrying unchecked text through the program.

## 4. Creating a `time`

A `time` represents a clock time:

```python
from datetime import time

meeting_time = time(14, 30, 15)

print(meeting_time.hour)
print(meeting_time.minute)
print(meeting_time.second)
```

A `time` object does not include a year, month, or day. It is useful when the clock-time concept matters independently from a date.

Do not expect to add a `timedelta` directly to a plain `time` object. Time arithmetic normally needs a `datetime` or application-specific logic about what date should be used.

## 5. Creating a `datetime`

A `datetime` combines both concepts:

```python
from datetime import datetime

moment = datetime(2026, 8, 27, 14, 30, 15)

print(moment.date())
print(moment.time())
print(moment.year)
print(moment.hour)
```

This is useful for events, timestamps, deadlines, logs, appointments, and other values where both date and clock time matter.

## 6. Current date and current time

`date.today()` returns the current local date:

```python
from datetime import date

today = date.today()
print(today)
```

`datetime.now()` returns the current local date and time as a naive `datetime` by default:

```python
from datetime import datetime

now = datetime.now()
print(now)
```

For an aware UTC datetime, prefer:

```python
from datetime import datetime, timezone

now_utc = datetime.now(timezone.utc)
print(now_utc)
```

Do not use current-time calls when a deterministic test or example can use a fixed value instead. Real clocks make outputs change from run to run.

### Avoid `datetime.utcnow()` in new code

`datetime.utcnow()` returns a naive object even though the value is intended to represent UTC, and it is deprecated in modern Python. Prefer `datetime.now(timezone.utc)` so the UTC relationship is explicit in the object.

## 7. What is a `timedelta`?

A `timedelta` represents a duration.

```python
from datetime import timedelta

review_window = timedelta(days=7, hours=3)
print(review_window)
```

It can be added to or subtracted from dates and datetimes:

```python
from datetime import date, timedelta

start = date(2026, 8, 27)
end = start + timedelta(days=10)

print(end)
```

Subtracting compatible dates or datetimes produces a `timedelta`:

```python
from datetime import date

start = date(2026, 8, 27)
end = date(2026, 9, 3)

difference = end - start
print(difference.days)
```

## 8. `timedelta.seconds` is not total seconds

This is a classic trap.

```python
from datetime import timedelta

duration = timedelta(days=1, seconds=90)

print(duration.days)
print(duration.seconds)
print(duration.total_seconds())
```

`duration.seconds` is only the normalized seconds portion inside the day. It does not include whole days.

Use `total_seconds()` when you need the complete duration expressed in seconds.

For the example above:

```text
seconds component = 90
total duration = 86490 seconds
```

## 9. Durations are not calendar months

A `timedelta` models fixed durations in days, seconds, and microseconds. It does not have a built-in concept of "one calendar month".

This:

```python
from datetime import date, timedelta

start = date(2026, 1, 31)
approximate = start + timedelta(days=30)

print(approximate)
```

means exactly "add 30 days". It does not mean "move to the same day in the next month".

Calendar-month rules vary because months have different lengths. Business calendars, month-end logic, holidays, and settlement rules are application concepts that need explicit policies.

## 10. Comparing dates and datetimes

Objects of the same compatible kind can be compared:

```python
from datetime import date

deadline = date(2026, 9, 10)
today = date(2026, 9, 3)

if today <= deadline:
    print("Still on time")
```

Do not compare formatted strings merely because they look date-like. Some string formats sort chronologically, some do not, and string comparison does not provide date semantics.

## 11. Parsing text with `strptime()`

External data often arrives as text.

Use `datetime.strptime()` when the input follows a known format:

```python
from datetime import datetime

text = "27/08/2026 18:45"
moment = datetime.strptime(text, "%d/%m/%Y %H:%M")

print(moment)
```

The format string is a contract between your code and the input.

Common directives include:

| Directive | Meaning |
|---|---|
| `%Y` | four-digit year |
| `%m` | month number |
| `%d` | day of month |
| `%H` | hour from 00 to 23 |
| `%M` | minute |
| `%S` | second |
| `%f` | microseconds |
| `%z` | UTC offset |

If the text does not match the expected format, parsing raises `ValueError`.

```python
from datetime import datetime

try:
    moment = datetime.strptime("2026/08/27", "%Y-%m-%d")
except ValueError:
    print("Unexpected date format")
```

## 12. Formatting with `strftime()`

`strftime()` goes in the other direction: object to text.

```python
from datetime import datetime

moment = datetime(2026, 8, 27, 18, 45)

print(moment.strftime("%Y-%m-%d"))
print(moment.strftime("%d/%m/%Y %H:%M"))
```

Formatting is useful for presentation and external contracts.

Keep the distinction clear:

```text
strptime: text -> datetime
strftime: datetime/date/time -> text
```

## 13. ISO-oriented helpers

For ISO-style representations, dedicated methods are often clearer than custom format strings.

```python
from datetime import date, datetime

calendar_date = date.fromisoformat("2026-08-27")
moment = datetime.fromisoformat("2026-08-27T18:45:00+00:00")

print(calendar_date.isoformat())
print(moment.isoformat())
```

`fromisoformat()` and `isoformat()` are convenient when your contract matches forms supported by Python's ISO-oriented parser and formatter.

Do not assume that every string loosely described as "ISO 8601" is accepted by every parser. Treat the exact accepted form as part of the interface contract.

## 14. Controlling ISO output precision

`datetime.isoformat()` can control the displayed time precision:

```python
from datetime import datetime

moment = datetime(2026, 8, 27, 18, 45, 12, 345678)

print(moment.isoformat(timespec="minutes"))
print(moment.isoformat(timespec="seconds"))
print(moment.isoformat(timespec="microseconds"))
```

This is useful when an external format requires a particular precision.

## 15. Naive and aware datetimes

A `datetime` can be **naive** or **aware**.

A naive datetime does not contain enough timezone information to unambiguously position itself relative to other moments in the world.

```python
from datetime import datetime

naive = datetime(2026, 8, 27, 18, 30)
print(naive.tzinfo)
```

An aware datetime has timezone information that can provide an offset from UTC:

```python
from datetime import datetime, timezone

aware = datetime(2026, 8, 27, 18, 30, tzinfo=timezone.utc)
print(aware.tzinfo)
print(aware.utcoffset())
```

This distinction matters in APIs, logs, distributed systems, scheduled jobs, and any system that crosses timezone boundaries.

## 16. Representing UTC

Use `timezone.utc` for UTC:

```python
from datetime import datetime, timezone

moment = datetime(2026, 8, 27, 21, 30, tzinfo=timezone.utc)

print(moment.isoformat())
```

The result includes the UTC offset:

```text
2026-08-27T21:30:00+00:00
```

## 17. Fixed UTC offsets

`timezone` can represent fixed offsets:

```python
from datetime import datetime, timedelta, timezone

brt = timezone(timedelta(hours=-3))
moment = datetime(2026, 8, 27, 18, 30, tzinfo=brt)

print(moment.isoformat())
```

A fixed offset such as `-03:00` is not the same thing as a real geographic timezone. Geographic zones can change offset because of historical rules, daylight-saving transitions, and political changes.

## 18. Converting with `astimezone()`

For an aware datetime, use `astimezone()` to represent the same instant in another timezone:

```python
from datetime import datetime, timedelta, timezone

brt = timezone(timedelta(hours=-3))
local = datetime(2026, 8, 27, 18, 30, tzinfo=brt)
utc = local.astimezone(timezone.utc)

print(local.isoformat())
print(utc.isoformat())
```

The wall-clock value changes, but both objects represent the same instant.

## 19. Assigning `tzinfo` is not timezone conversion

This code changes metadata without converting the clock reading:

```python
from datetime import datetime, timezone

naive = datetime(2026, 8, 27, 18, 30)
labeled = naive.replace(tzinfo=timezone.utc)

print(labeled.isoformat())
```

`replace(tzinfo=...)` does not ask, "what time is 18:30 in another zone?" It constructs a new object with fields replaced.

Use it only when you already know what timezone the naive wall-clock value is supposed to represent and attaching that timezone is the intended operation.

For converting an already-aware datetime from one timezone to another, use `astimezone()`.

## 20. Do not mix naive and aware arithmetic casually

Subtracting an aware datetime from a naive datetime is not a meaningful operation without an explicit timezone relationship.

```python
from datetime import datetime, timezone

naive = datetime(2026, 8, 27, 18, 30)
aware = datetime(2026, 8, 27, 18, 30, tzinfo=timezone.utc)

try:
    difference = aware - naive
except TypeError:
    print("Cannot mix naive and aware datetimes")
```

Choose and document a timezone policy at system boundaries instead of silently mixing models.

## 21. Real geographic time zones and `zoneinfo`

The standard library includes the companion `zoneinfo` module for IANA time-zone rules such as `America/Sao_Paulo` or `Europe/London`.

Conceptually:

```python
from datetime import datetime
from zoneinfo import ZoneInfo

moment = datetime(2026, 8, 27, 18, 30, tzinfo=ZoneInfo("America/Sao_Paulo"))
print(moment.isoformat())
```

Unlike `timezone(timedelta(...))`, `ZoneInfo` can model historical and future offset rules supplied by the available timezone database.

Timezone database availability is environment-dependent. Some systems provide it directly; others may need the `tzdata` package. For that reason, the executable examples in this chapter use fixed offsets rather than assuming a specific IANA database is installed.

## 22. Unix timestamps

A Unix timestamp represents elapsed seconds from the platform's Unix epoch convention.

Create an aware UTC datetime from a timestamp by supplying a timezone:

```python
from datetime import datetime, timezone

moment = datetime.fromtimestamp(0, tz=timezone.utc)
print(moment.isoformat())
```

Convert an aware datetime back to a timestamp with `.timestamp()`:

```python
from datetime import datetime, timezone

moment = datetime(1970, 1, 1, tzinfo=timezone.utc)
print(moment.timestamp())
```

Timestamps are useful interchange values, but readability, supported ranges, precision, and platform behavior still matter. Do not use them as a replacement for understanding timezone policy.

## 23. Replacing fields

`replace()` returns a new object with selected fields changed:

```python
from datetime import datetime

original = datetime(2026, 8, 27, 18, 30)
updated = original.replace(hour=9, minute=0)

print(original)
print(updated)
```

It does not mutate the original object.

This is field replacement, not business-calendar arithmetic. Changing `month=2` on a date whose day is invalid in February can raise `ValueError`.

## 24. Combining a date and a time

`datetime.combine()` is useful when separate values need to become one datetime:

```python
from datetime import date, datetime, time

calendar_date = date(2026, 8, 27)
clock_time = time(18, 30)
moment = datetime.combine(calendar_date, clock_time)

print(moment)
```

The resulting object is naive unless timezone information is supplied through the time or an explicit timezone-aware design.

## 25. Common mistakes

### Mistake 1: storing everything as strings

Strings are appropriate at boundaries, but calculations should usually use date/time objects.

### Mistake 2: treating `timedelta.seconds` as the whole duration

Use `total_seconds()` when you need all days converted into seconds too.

### Mistake 3: using `timedelta(days=30)` as "one month"

That is 30 days, not calendar-month arithmetic.

### Mistake 4: parsing without an explicit contract

If incoming text has a defined format, encode that format deliberately and handle `ValueError` when input can be invalid.

### Mistake 5: mixing naive and aware datetimes

Define whether your system works in local time, UTC, or explicit zones at each boundary.

### Mistake 6: using `replace(tzinfo=...)` as a conversion

Field replacement and timezone conversion are different operations.

### Mistake 7: using a fixed offset as if it were a geographic timezone

Real time zones may have rule changes. Use `zoneinfo` when geographic rules matter.

### Mistake 8: using the real clock in deterministic tests

Inject or construct fixed datetimes when reproducibility matters.

## 26. Practical example

Imagine a report that receives a UTC timestamp as text, parses it, applies a fixed local offset for presentation, and calculates a review deadline.

```python
from datetime import datetime, timedelta, timezone

source = "2026-08-27T21:30:00+00:00"
created_utc = datetime.fromisoformat(source)

local_zone = timezone(timedelta(hours=-3))
created_local = created_utc.astimezone(local_zone)
deadline = created_local + timedelta(days=5)

print(created_local.isoformat())
print(deadline.isoformat())
```

The flow is explicit:

```text
text contract
    ↓
aware datetime
    ↓
timezone conversion
    ↓
duration arithmetic
    ↓
formatted output
```

## 27. Exercise

Create a program that:

1. parses `"2026-10-15 09:30"` using `strptime()`;
2. treats that value as a wall-clock time with a fixed offset of `-03:00`;
3. adds 2 days and 4 hours with `timedelta`;
4. converts the result to UTC with `astimezone()`;
5. prints both the local and UTC values with `isoformat()`;
6. prints the complete duration in seconds;
7. formats the UTC result as `YYYY-MM-DD HH:MM`.

Then answer:

- Which objects are naive and which are aware?
- Why is `replace(tzinfo=...)` acceptable for attaching the known source offset here but not for converting between zones?
- Why should `total_seconds()` be used instead of `.seconds` for the complete duration?
- Why is a fixed `-03:00` offset not automatically equivalent to every historical or future rule for `America/Sao_Paulo`?

## 28. Review checklist

Before moving on, make sure you can explain:

- `date`, `time`, `datetime`, `timedelta`, and `timezone`;
- construction and validation of calendar values;
- `date.today()` and `datetime.now()`;
- why aware UTC should use `datetime.now(timezone.utc)`;
- date and datetime arithmetic;
- `.days`, `.seconds`, and `.total_seconds()`;
- why fixed durations are not calendar months;
- `strptime()` versus `strftime()`;
- `fromisoformat()` and `isoformat()`;
- naive versus aware datetimes;
- UTC and fixed offsets;
- `astimezone()` versus `replace(tzinfo=...)`;
- why real geographic timezone rules belong to `zoneinfo`;
- timestamps and their role as interchange values;
- how to keep tests deterministic.

## Quick reference

```python
from datetime import date, datetime, time, timedelta, timezone

calendar_date = date(2026, 8, 27)
clock_time = time(18, 30)
moment = datetime(2026, 8, 27, 18, 30)
duration = timedelta(days=2, hours=4)

calendar_date + timedelta(days=1)
moment + duration

datetime.strptime("2026-08-27 18:30", "%Y-%m-%d %H:%M")
moment.strftime("%d/%m/%Y %H:%M")

date.fromisoformat("2026-08-27")
datetime.fromisoformat("2026-08-27T18:30:00+00:00")
moment.isoformat()

aware_utc = datetime(2026, 8, 27, 21, 30, tzinfo=timezone.utc)
fixed_offset = timezone(timedelta(hours=-3))
aware_utc.astimezone(fixed_offset)

duration.total_seconds()
```

## Executable examples

- [`examples/date_arithmetic.py`](examples/date_arithmetic.py)
- [`examples/parse_and_format.py`](examples/parse_and_format.py)
- [`examples/utc_conversion.py`](examples/utc_conversion.py)
- [`examples/duration_seconds.py`](examples/duration_seconds.py)

The examples are deterministic and do not depend on the current clock or an external timezone database.

## Next chapter

Continue with **Chapter 03: `json` Beyond Basic Persistence**, where the standard library revisits JSON serialization with deeper control over encoders, decoders, formatting, numeric hooks, and strict interoperability contracts.

## Official references

- [Python 3.14 `datetime` - Basic date and time types](https://docs.python.org/3.14/library/datetime.html)
- [Python 3.14 `strftime()` and `strptime()` format codes](https://docs.python.org/3.14/library/datetime.html#strftime-and-strptime-format-codes)
- [Python 3.14 `zoneinfo` - IANA time zone support](https://docs.python.org/3.14/library/zoneinfo.html)
