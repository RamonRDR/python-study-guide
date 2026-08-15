def parse_integer(text: str) -> int | None:
    try:
        return int(text)
    except ValueError:
        return None


for text in ["42", "seven", "-8"]:
    result = parse_integer(text)

    if result is None:
        print(f"{text!r}: invalid")
    else:
        print(f"{text!r}: {result}")
