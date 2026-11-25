"""Contrast recursive calls with an iterative accumulator."""


def _validate(n: int) -> None:
    if type(n) is not int:
        raise TypeError("Expected an exact integer")
    if not 0 <= n <= 100:
        raise ValueError("Expected an integer from 0 to 100")


def _recursive_sum(n: int) -> int:
    if n == 0:
        return 0
    return n + _recursive_sum(n - 1)


def recursive_sum(n: int) -> int:
    _validate(n)
    return _recursive_sum(n)


def iterative_sum(n: int) -> int:
    _validate(n)
    total = 0
    for value in range(1, n + 1):
        total += value
    return total


if __name__ == "__main__":
    assert recursive_sum(0) == 0
    assert recursive_sum(3) == iterative_sum(3) == 6
    print(recursive_sum(4))
