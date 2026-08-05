"""Demonstrate module and function docstrings with runtime access."""


def calculate_average(values: list[float]) -> float:
    """Return the arithmetic mean of a non-empty sequence of numbers.

    Args:
        values: Numbers included in the calculation.

    Returns:
        The arithmetic mean of the provided values.

    Raises:
        ValueError: If values is empty.
    """
    if not values:
        raise ValueError("values must not be empty")
    return sum(values) / len(values)


def main() -> None:
    """Run the deterministic function-docstring example."""
    scores = [8.0, 9.5, 7.5]
    print(f"Average: {calculate_average(scores):.2f}")
    print(f"Summary: {calculate_average.__doc__.splitlines()[0]}")


if __name__ == "__main__":
    main()
