"""Accumulate qualifying study minutes without mutating the input."""


def qualifying_minutes(minutes: list[int], goal: int = 20) -> int:
    total = 0
    for value in minutes:
        if value >= goal:
            total += value
    return total


if __name__ == "__main__":
    assert qualifying_minutes([]) == 0
    assert qualifying_minutes([19]) == 0
    assert qualifying_minutes([20, 20]) == 40
    print(qualifying_minutes([12, 20, 25]))
