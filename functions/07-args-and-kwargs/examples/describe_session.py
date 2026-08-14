def describe_session(title: str, *topics: str, **details: str) -> None:
    print(f"Title: {title}")
    print(f"Topics: {', '.join(topics)}")

    for name, value in details.items():
        print(f"{name}: {value}")


describe_session(
    "Python Study",
    "functions",
    "arguments",
    level="beginner",
    format="guided",
)
