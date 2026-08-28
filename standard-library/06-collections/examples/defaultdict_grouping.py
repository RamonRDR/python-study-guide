from collections import defaultdict


records = [
    ("billing", "INV-101"),
    ("support", "REQ-203"),
    ("billing", "INV-102"),
    ("operations", "OPS-305"),
    ("support", "REQ-204"),
]

by_team: defaultdict[str, list[str]] = defaultdict(list)

for team, reference in records:
    by_team[team].append(reference)

for team in sorted(by_team):
    print(f"{team}: {', '.join(by_team[team])}")
