"""Contrast source-code explanation with runtime observation."""

import logging
import sys


logger = logging.getLogger(__name__)


def calculate_shipping_total(
    subtotal_cents: int,
    customer_region: str,
) -> int:
    """Return the subtotal plus the applicable shipping fee."""
    # Local regulation requires free shipping for domestic orders over 10,000 cents.
    qualifies_for_free_shipping = (
        customer_region == "domestic" and subtotal_cents >= 10_000
    )

    shipping_cents = 0 if qualifies_for_free_shipping else 1_500
    logger.info(
        "Calculated shipping region=%s subtotal_cents=%s shipping_cents=%s",
        customer_region,
        subtotal_cents,
        shipping_cents,
    )
    return subtotal_cents + shipping_cents


def main() -> None:
    """Run the comments-versus-logging example."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)s:%(name)s:%(message)s",
        stream=sys.stdout,
    )

    total_cents = calculate_shipping_total(12_000, "domestic")
    print(f"Customer total: {total_cents} cents")


if __name__ == "__main__":
    main()
