def normalize_name(name: str) -> str:
    return name.strip().title()


def build_greeting(name: str) -> str:
    clean_name = normalize_name(name)
    return f"Welcome, {clean_name}!"


print(build_greeting("  ava stone  "))
