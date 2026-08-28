import csv
from io import StringIO

stream = StringIO(newline="")
writer = csv.writer(
    stream,
    delimiter=";",
    quoting=csv.QUOTE_MINIMAL,
    lineterminator="\n",
)
writer.writerow(["name", "note"])
writer.writerow(["Ana", "uses;semicolon"])
writer.writerow(["Bob", 'says "hello"'])

text = stream.getvalue()
print(text, end="")

reader = csv.reader(
    StringIO(text, newline=""),
    delimiter=";",
)
print(list(reader))
