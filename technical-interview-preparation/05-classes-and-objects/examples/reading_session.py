"""Model independent reading sessions."""


class ReadingSession:
    def __init__(self, topic: str) -> None:
        self.topic = topic
        self.pages = 0

    def read(self, pages: int) -> None:
        if type(pages) is not int:
            raise TypeError("pages must be an integer")
        if pages < 0:
            raise ValueError("pages cannot be negative")
        self.pages += pages


if __name__ == "__main__":
    first = ReadingSession("Python")
    second = ReadingSession("SQL")
    first.read(4)
    print(first.pages, second.pages)
