"""Use closures for independent state and a decorator for call records."""
from functools import wraps


def make_counter():
    count = 0

    def increment() -> int:
        nonlocal count
        count += 1
        return count

    return increment


def record_calls(records: list[str]):
    def decorate(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            records.append(function.__name__)
            return function(*args, **kwargs)

        return wrapper

    return decorate


if __name__ == "__main__":
    calls = []

    @record_calls(calls)
    def double(value: int) -> int:
        return value * 2

    print(double(3), calls)
    counter = make_counter()
    print(counter(), counter())
