"""Protect a shared read-modify-write operation with a lock."""
from concurrent.futures import ThreadPoolExecutor
from threading import Lock


def count_updates(workers: int, updates: int) -> int:
    if type(workers) is not int or workers < 1:
        raise ValueError("workers must be a positive integer")
    if type(updates) is not int or updates < 0:
        raise ValueError("updates must be a nonnegative integer")

    count = 0
    lock = Lock()

    def increment_many() -> None:
        nonlocal count
        for _ in range(updates):
            with lock:
                count += 1

    with ThreadPoolExecutor(max_workers=workers) as executor:
        futures = [executor.submit(increment_many) for _ in range(workers)]
        for future in futures:
            future.result()
    return count


if __name__ == "__main__":
    print(count_updates(4, 250))
