"""Reference solution for ascii-digit-counter."""


def count_digits(text: str) -> int:
    count = 0
    for character in text:
        if character in "0123456789":
            count += 1
    return count
