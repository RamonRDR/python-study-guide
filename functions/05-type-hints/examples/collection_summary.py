def summarize_topics(topics: list[str]) -> str:
    return f"{len(topics)} topics: {', '.join(topics)}"


print(summarize_topics(["scope", "type hints", "defaults"]))
