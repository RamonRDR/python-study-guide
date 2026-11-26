"""Filter a stream without building an intermediate list."""
from collections.abc import Iterable, Iterator


def eligible_rows(rows: Iterable[int], minimum: int) -> Iterator[int]:
    for row in rows:
        if row >= minimum:
            yield row


if __name__ == "__main__":
    stream = eligible_rows([0, 3, 1, 4], 3)
    print(next(stream))
    print(list(stream))
    print(list(stream))
