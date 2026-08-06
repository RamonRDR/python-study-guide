"""Demonstrate a bounded workaround for a fictional legacy export."""


def normalize_legacy_account_code(raw_account_code: str) -> str:
    """Return an account code without legacy fixed-width padding."""
    # HACK(#305): Legacy exports pad account codes to eight characters.
    # Remove this normalization after all supported exports use the new schema.
    normalized_code = raw_account_code.lstrip("0")
    return normalized_code or "0"


def main() -> None:
    """Run the temporary-workaround example."""
    for raw_code in ("00001234", "00000007", "00000000"):
        print(f"{raw_code} -> {normalize_legacy_account_code(raw_code)}")


if __name__ == "__main__":
    main()
