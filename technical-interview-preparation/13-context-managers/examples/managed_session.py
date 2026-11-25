"""Record acquisition and release around a managed operation."""
from contextlib import contextmanager


@contextmanager
def managed_session(events: list[str]):
    events.append("open")
    try:
        yield events
    finally:
        events.append("close")


if __name__ == "__main__":
    events = []
    with managed_session(events) as session:
        session.append("work")
    print(events)
