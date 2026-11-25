"""Reference solution for longest-distinct-substring."""


def longest_distinct_length(text: str) -> int:
    last = {}
    left = 0
    best = 0
    for right, character in enumerate(text):
        if character in last:
            left = max(left, last[character] + 1)
        last[character] = right
        best = max(best, right - left + 1)
    return best
