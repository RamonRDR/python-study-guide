def add_five(number: int) -> int:
    number += 5
    return number


def add_topic(topics: list[str], topic: str) -> None:
    topics.append(topic)


score = 70
updated_score = add_five(score)

topics = ["Functions"]
add_topic(topics, "Data flow")

print(f"Original score: {score}")
print(f"Updated score: {updated_score}")
print(f"Topics: {topics}")
