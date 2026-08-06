"""Demonstrate import grouping and common naming conventions."""

from collections.abc import Iterable
from decimal import Decimal

DEFAULT_TAX_RATE = Decimal("0.18")


def calculate_tax(
    amounts: Iterable[Decimal],
    tax_rate: Decimal = DEFAULT_TAX_RATE,
) -> Decimal:
    """Return the tax calculated from all supplied amounts."""
    taxable_total = sum(amounts, start=Decimal("0"))
    return taxable_total * tax_rate


def main() -> None:
    invoice_amounts = [
        Decimal("120.00"),
        Decimal("80.00"),
    ]
    tax_amount = calculate_tax(invoice_amounts)
    print(f"Tax: {tax_amount:.2f}")


if __name__ == "__main__":
    main()
