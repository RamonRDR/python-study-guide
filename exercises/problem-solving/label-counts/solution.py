"""Reference solution for label-counts."""


def label_counts(labels: list[str]) -> dict[str, int]:
    counts = {}
    for label in labels:
        counts[label] = counts.get(label, 0) + 1
    return counts
