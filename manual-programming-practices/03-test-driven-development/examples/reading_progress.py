"""Calculate remaining pages according to the reading-progress contract."""


def remaining_pages(total_pages: int, pages_read: int) -> int:
    """Return unread pages; reject non-integers and invalid ranges."""
    if type(total_pages) is not int or type(pages_read) is not int:
        raise TypeError("Page counts must be built-in integers")
    if total_pages < 0 or not 0 <= pages_read <= total_pages:
        raise ValueError("Page counts must satisfy 0 <= pages_read <= total_pages")
    return total_pages - pages_read


if __name__ == "__main__":
    print(remaining_pages(20, 7))
