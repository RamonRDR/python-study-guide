"""Show how inspect.getdoc() retrieves and cleans a docstring."""

from inspect import getdoc


def format_identifier(raw_value: str) -> str:
    """Normalize a fictional identifier for display.

    Leading and trailing whitespace is removed, and remaining letters are
    converted to uppercase.
    """
    return raw_value.strip().upper()


def main() -> None:
    """Run the deterministic docstring-inspection example."""
    print(format_identifier("  py-42  "))
    print("---")
    print(getdoc(format_identifier))


if __name__ == "__main__":
    main()
