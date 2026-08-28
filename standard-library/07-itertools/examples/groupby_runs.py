"""Group consecutive status runs with itertools.groupby."""

from itertools import groupby

statuses = ["ok", "ok", "retry", "retry", "ok"]
runs = [(status, len(list(group))) for status, group in groupby(statuses)]

print(runs)
