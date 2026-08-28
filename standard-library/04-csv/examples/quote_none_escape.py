import csv
from io import StringIO


row = ["alpha,beta", 'quoted "text"', "line\nbreak"]

output = StringIO(newline="")
writer = csv.writer(
    output,
    delimiter=",",
    quoting=csv.QUOTE_NONE,
    escapechar="\\",
    lineterminator="\n",
)
writer.writerow(row)

text = output.getvalue()
print(repr(text))

source = StringIO(text, newline="")
reader = csv.reader(
    source,
    delimiter=",",
    quoting=csv.QUOTE_NONE,
    escapechar="\\",
)
print(next(reader))
