"""Compare vague identifiers with names that communicate intention."""


def calculate_total_vague(p: list[float], d: float) -> float:
    """Return a total using deliberately vague parameter names."""
    t = sum(p)
    return t - (t * d)


def calculate_discounted_total(
    prices: list[float],
    discount_rate: float,
) -> float:
    """Return the total after applying a fractional discount rate."""
    subtotal = sum(prices)
    discount_amount = subtotal * discount_rate
    return subtotal - discount_amount


def main() -> None:
    """Run the deterministic naming comparison."""
    product_prices = [18.50, 7.25, 4.25]
    promotional_discount_rate = 0.10

    vague_total = calculate_total_vague(
        product_prices,
        promotional_discount_rate,
    )
    clear_total = calculate_discounted_total(
        product_prices,
        promotional_discount_rate,
    )

    print(f"Vague version total: {vague_total:.2f}")
    print(f"Clear version total: {clear_total:.2f}")
    print(f"Same result: {vague_total == clear_total}")


if __name__ == "__main__":
    main()
