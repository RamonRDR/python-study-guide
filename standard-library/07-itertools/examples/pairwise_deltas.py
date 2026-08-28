"""Compute adjacent changes with itertools.pairwise."""

from itertools import pairwise

readings = [120, 126, 123, 131]
changes = [current - previous for previous, current in pairwise(readings)]

print(changes)
