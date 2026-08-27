import csv
import os
import tempfile


records = [
    {"topic": "Functions", "score": 91, "note": "Clear flow"},
    {"topic": "Files", "score": 88, "note": "Read, write, validate"},
]

with tempfile.TemporaryDirectory() as directory:
    path = os.path.join(directory, "scores.csv")
    fieldnames = ["topic", "score", "note"]

    with open(path, "w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(records)

    with open(path, "r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            score = int(row["score"])
            print(f'{row["topic"]}: {score} - {row["note"]}')
