import csv
from io import StringIO

stream = StringIO(newline="")
writer = csv.writer(
    stream,
    quoting=csv.QUOTE_NOTNULL,
    lineterminator="\n",
)
writer.writerow(["name", "note"])
writer.writerow(["Ana", None])
writer.writerow(["Bob", ""])

text = stream.getvalue()
print(text, end="")

reader = csv.reader(
    StringIO(text, newline=""),
    quoting=csv.QUOTE_NOTNULL,
)
print(list(reader))
