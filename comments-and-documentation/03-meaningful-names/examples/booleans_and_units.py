"""Demonstrate boolean, unit, collection, and constant naming."""


MAX_RETRY_ATTEMPTS = 3
RETRYABLE_STATUS_CODES = {502, 503, 504}


def should_retry_request(
    attempt_number: int,
    response_status_code: int,
) -> bool:
    """Return whether a failed request should be attempted again."""
    is_status_configured_for_retry = (
        response_status_code in RETRYABLE_STATUS_CODES
    )
    has_retry_attempts_remaining = attempt_number < MAX_RETRY_ATTEMPTS
    return (
        is_status_configured_for_retry
        and has_retry_attempts_remaining
    )


def main() -> None:
    """Run the deterministic naming example."""
    retry_delay_seconds = 30
    invoice_total_cents = 12_750
    customer_names = ["Ana", "Diego", "Mina"]

    print(f"Retry delay: {retry_delay_seconds} seconds")
    print(f"Invoice total: {invoice_total_cents} cents")
    print(f"Customers: {', '.join(customer_names)}")
    print(f"Should retry: {should_retry_request(1, 503)}")


if __name__ == "__main__":
    main()
