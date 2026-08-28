import csv
from io import StringIO


text = 'name;note\nAda;"uses, commas in text"\nLin;ready\n'
dialect = csv.Sniffer().sniff(text, delimiters=",;\t")

print(repr(dialect.delimiter))

source = StringIO(text, newline="")
reader = csv.reader(source, dialect)
print(list(reader))
