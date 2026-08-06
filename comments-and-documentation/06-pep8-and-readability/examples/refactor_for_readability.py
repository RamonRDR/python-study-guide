"""Refactor a dense calculation into intention-revealing steps."""

from collections.abc import Iterable


def has_minimum_activity(monthly_sales: Iterable[float]) -> bool:
    """Return whether at least one month contains a positive sale."""
    return any(sale > 0 for sale in monthly_sales)


def calculate_average_sales(monthly_sales: Iterable[float]) -> float:
    """Return the arithmetic mean of the supplied monthly sales."""
    sales = list(monthly_sales)
    if not sales:
        raise ValueError("monthly_sales must not be empty")
    return sum(sales) / len(sales)


def classify_sales_performance(monthly_sales: Iterable[float]) -> str:
    """Classify performance using explicit business thresholds."""
    sales = list(monthly_sales)

    if not has_minimum_activity(sales):
        return "inactive"

    average_sales = calculate_average_sales(sales)

    if average_sales >= 10_000:
        return "strong"
    if average_sales >= 5_000:
        return "stable"
    return "developing"


def main() -> None:
    monthly_sales = [7_500.0, 8_100.0, 9_000.0]
    classification = classify_sales_performance(monthly_sales)
    print(f"Classification: {classification}")


if __name__ == "__main__":
    main()
