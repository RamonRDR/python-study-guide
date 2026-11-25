"""Count loop iterations instead of timing the hardware."""


def scan_count(size: int) -> int:
    count = 0
    for _ in range(size):
        count += 1
    return count


def pair_count(size: int) -> int:
    count = 0
    for _ in range(size):
        for _ in range(size):
            count += 1
    return count


def halving_count(size: int) -> int:
    count = 0
    while size > 1:
        size //= 2
        count += 1
    return count


if __name__ == "__main__":
    for size in (4, 8, 16):
        print(size, scan_count(size), pair_count(size), halving_count(size))
