"""Demonstrate the five standard logging levels with deterministic output."""

import logging
import sys


logger = logging.getLogger(__name__)


def report_import_status() -> None:
    """Emit example events at the standard logging levels."""
    logger.debug("Validated 3 input columns")
    logger.info("Imported 12 records")
    logger.warning("Skipped 1 optional field")
    logger.error("Rejected 1 malformed record")
    logger.critical("Stopped because the destination is unavailable")


def main() -> None:
    """Configure logging and run the level demonstration."""
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(levelname)s:%(message)s",
        stream=sys.stdout,
    )
    report_import_status()


if __name__ == "__main__":
    main()
