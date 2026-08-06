"""Demonstrate readable layout, spacing, and line wrapping."""

STANDARD_DISCOUNT_RATE = 0.10


def calculate_subtotal(unit_price: float, quantity: int) -> float:
    """Return the subtotal before discounts."""
    return unit_price * quantity


def calculate_total(
    unit_price: float,
    quantity: int,
    *,
    discount_rate: float = STANDARD_DISCOUNT_RATE,
) -> float:
    """Return the total after applying a fractional discount rate."""
    subtotal = calculate_subtotal(unit_price, quantity)
    discount_amount = subtotal * discount_rate
    return subtotal - discount_amount


def main() -> None:
    total = calculate_total(
        unit_price=125.0,
        quantity=4,
        discount_rate=0.08,
    )
    print(f"Total: {total:.2f}")


if __name__ == "__main__":
    main()
