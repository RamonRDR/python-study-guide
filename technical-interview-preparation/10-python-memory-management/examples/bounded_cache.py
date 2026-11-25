"""Bound the number of entries held by a simple update-ordered cache."""


class BoundedCache:
    def __init__(self, capacity: int) -> None:
        if type(capacity) is not int or capacity < 1:
            raise ValueError("capacity must be a positive integer")
        self._capacity = capacity
        self._entries = {}

    def put(self, key: str, value: int) -> None:
        self._entries.pop(key, None)
        self._entries[key] = value
        if len(self._entries) > self._capacity:
            oldest = next(iter(self._entries))
            del self._entries[oldest]

    def snapshot(self) -> dict:
        return self._entries.copy()

    def clear(self) -> None:
        self._entries.clear()


if __name__ == "__main__":
    cache = BoundedCache(2)
    for key, value in (("a", 1), ("b", 2), ("c", 3)):
        cache.put(key, value)
    print(cache.snapshot())
