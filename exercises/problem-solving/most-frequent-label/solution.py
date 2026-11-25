"""Reference solution for most-frequent-label."""


def most_frequent_label(labels: list[str]) -> str | None:
    counts = {}
    for label in labels:
        counts[label] = counts.get(label, 0) + 1
    winner = None
    best = 0
    for label in labels:
        if counts[label] > best:
            winner = label
            best = counts[label]
    return winner
