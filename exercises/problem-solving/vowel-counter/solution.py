"""Count only literal ASCII vowel occurrences."""


def count_vowels(text: str) -> int:
    count = 0
    for character in text:
        if character in "aeiouAEIOU":
            count += 1
    return count
