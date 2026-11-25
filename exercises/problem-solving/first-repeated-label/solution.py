"""Reference solution for first-repeated-label."""


def first_repeated_label(labels: list[str]) -> str | None:
    seen = set()
    for label in labels:
        if label in seen:
            return label
        seen.add(label)
    return None
