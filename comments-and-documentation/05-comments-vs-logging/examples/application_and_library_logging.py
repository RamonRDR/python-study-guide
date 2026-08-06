"""Show that applications configure logging while libraries emit records."""

import logging
import sys


library_logger = logging.getLogger("study_guide.inventory")
library_logger.addHandler(logging.NullHandler())


def count_available_items(stock_by_code: dict[str, int]) -> int:
    """Return how many item codes currently have available stock."""
    library_logger.debug(
        "Counting available items item_codes=%s",
        len(stock_by_code),
    )
    return sum(quantity > 0 for quantity in stock_by_code.values())


def configure_application_logging() -> None:
    """Configure the root logger at the application entry point."""
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(levelname)s:%(name)s:%(message)s",
        stream=sys.stdout,
    )


def main() -> None:
    """Configure the application and call the library-style function."""
    configure_application_logging()
    available_items = count_available_items(
        {"BOOK": 4, "PEN": 0, "NOTEBOOK": 7}
    )
    print(f"Available item codes: {available_items}")


if __name__ == "__main__":
    main()
