class ConfigurationError(Exception):
    pass


def parse_attempt_limit(text: str) -> int:
    try:
        limit = int(text)
    except ValueError as error:
        raise ConfigurationError("attempt limit must be an integer") from error

    if limit <= 0:
        raise ConfigurationError("attempt limit must be greater than zero")

    return limit


try:
    parse_attempt_limit("three")
except ConfigurationError as error:
    cause_name = type(error.__cause__).__name__ if error.__cause__ else "None"
    print(f"{type(error).__name__}: {error}")
    print(f"Cause: {cause_name}")
