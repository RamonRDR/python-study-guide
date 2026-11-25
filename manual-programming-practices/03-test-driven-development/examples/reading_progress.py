"""Calculate remaining pages according to the reading-progress contract."""


def remaining_pages(total_pages: int, pages_read: int) -> int:
    """Return unread pages; reject non-integers and invalid ranges."""
    if any(isinstance(value, bool) or not isinstance(value, int)
           for value in (total_pages, pages_read)):
        raise TypeError("Page counts must be integers, excluding bool")
    if total_pages < 0 or not 0 <= pages_read <= total_pages:
        raise ValueError("Page counts must satisfy 0 <= pages_read <= total_pages")
    return total_pages - pages_read


if __name__ == "__main__":
    print(remaining_pages(20, 7))
