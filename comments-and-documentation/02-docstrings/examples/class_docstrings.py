"""Demonstrate class and method docstrings."""


class ReadingProgress:
    """Track completed pages in a fictional reading session."""

    def __init__(self, total_pages: int) -> None:
        """Initialize progress for a book with a positive page count."""
        if total_pages <= 0:
            raise ValueError("total_pages must be positive")
        self.total_pages = total_pages
        self.completed_pages = 0

    def record_pages(self, pages: int) -> None:
        """Add completed pages without exceeding the total page count."""
        if pages < 0:
            raise ValueError("pages must not be negative")
        self.completed_pages = min(
            self.completed_pages + pages,
            self.total_pages,
        )

    def percentage(self) -> float:
        """Return the completed portion as a percentage."""
        return self.completed_pages / self.total_pages * 100


def main() -> None:
    """Run the deterministic class-docstring example."""
    progress = ReadingProgress(total_pages=200)
    progress.record_pages(50)
    print(f"Progress: {progress.percentage():.1f}%")
    print(f"Class summary: {ReadingProgress.__doc__}")


if __name__ == "__main__":
    main()
