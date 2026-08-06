"""Demonstrate actionable markers in a fictional API compatibility policy."""


DEFAULT_TIMEOUT_SECONDS = 30


def build_request_options(api_version: str) -> dict[str, int | str]:
    """Return deterministic request options for a fictional API."""
    options: dict[str, int | str] = {
        "api_version": api_version,
        "timeout_seconds": DEFAULT_TIMEOUT_SECONDS,
    }

    # NOTE: API v1 requires an explicit compatibility mode.
    if api_version == "v1":
        # TODO(#128): Remove this branch after every client uses API v2.
        options["compatibility_mode"] = "legacy"

    return options


def main() -> None:
    """Run the actionable-marker example."""
    for version in ("v1", "v2"):
        print(f"{version}: {build_request_options(version)}")


if __name__ == "__main__":
    main()
