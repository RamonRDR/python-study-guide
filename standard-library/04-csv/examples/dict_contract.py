import csv
from io import StringIO

EXPECTED_FIELDS = ["name", "score"]

text = "name,score\nAna,88\nBob,91\n"
reader = csv.DictReader(StringIO(text, newline=""))

if reader.fieldnames != EXPECTED_FIELDS:
    raise ValueError("unexpected header")

for row in reader:
    if None in row:
        raise ValueError("row has extra fields")
    if any(value is None for value in row.values()):
        raise ValueError("row has missing fields")
    print(row)
