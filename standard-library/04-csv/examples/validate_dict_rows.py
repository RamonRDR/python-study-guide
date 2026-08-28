import csv
from io import StringIO


text = "name,score,status\nAda,91,complete\nLin,88,review\n"
source = StringIO(text, newline="")
missing = object()
reader = csv.DictReader(
    source,
    restkey="_extra_fields",
    restval=missing,
)

expected_fields = ["name", "score", "status"]
if reader.fieldnames != expected_fields:
    raise ValueError("unexpected CSV header")

records = []
for row in reader:
    if row.get("_extra_fields") is not None:
        raise ValueError("row contains extra fields")
    if any(value is missing for value in row.values()):
        raise ValueError("row contains missing fields")

    score = int(row["score"])
    if not 0 <= score <= 100:
        raise ValueError("score must be between 0 and 100")

    records.append(
        {
            "name": row["name"],
            "score": score,
            "status": row["status"],
        }
    )

print(records)
