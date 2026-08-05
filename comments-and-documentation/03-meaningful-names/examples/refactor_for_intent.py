"""Show how small named operations can reveal a workflow's intention."""


def normalize_account_code(raw_account_code: str) -> str:
    """Return an uppercase account code without surrounding whitespace."""
    return raw_account_code.strip().upper()


def is_supported_account(account_code: str) -> bool:
    """Return whether the account belongs to the fictional supported set."""
    supported_account_codes = {"ASSET", "LIABILITY", "REVENUE"}
    return account_code in supported_account_codes


def build_validation_message(raw_account_code: str) -> str:
    """Return a readable validation result for a fictional account code."""
    account_code = normalize_account_code(raw_account_code)

    if is_supported_account(account_code):
        return f"{account_code}: supported"

    return f"{account_code}: unsupported"


def main() -> None:
    """Run the deterministic intention-revealing refactoring example."""
    raw_account_codes = [" asset ", "expense", "revenue"]

    validation_messages = [
        build_validation_message(raw_account_code)
        for raw_account_code in raw_account_codes
    ]

    print("\n".join(validation_messages))


if __name__ == "__main__":
    main()
