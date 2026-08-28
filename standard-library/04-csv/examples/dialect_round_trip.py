import csv
from io import StringIO


rows = [
    ["name", "note"],
    ["Ada", "comma, semicolon; and newline\ninside"],
    ["Lin", 'She said "hello"'],
]

output = StringIO(newline="")
writer = csv.writer(
    output,
    delimiter=";",
    quotechar='"',
    quoting=csv.QUOTE_MINIMAL,
    lineterminator="\n",
)
writer.writerows(rows)

text = output.getvalue()
print(text)

source = StringIO(text, newline="")
reader = csv.reader(
    source,
    delimiter=";",
    quotechar='"',
    quoting=csv.QUOTE_MINIMAL,
)
print(list(reader))
