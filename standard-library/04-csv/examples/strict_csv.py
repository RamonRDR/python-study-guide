import csv
from io import StringIO

text = 'name,score\n"Ana,88\n'

try:
    list(csv.reader(StringIO(text, newline=""), strict=True))
except csv.Error:
    print("Malformed CSV rejected")
