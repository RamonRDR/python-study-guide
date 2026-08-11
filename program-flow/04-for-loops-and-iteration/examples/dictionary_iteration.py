lesson_minutes = {
    "conditions": 25,
    "patterns": 35,
    "loops": 40,
}

for topic in lesson_minutes:
    print(f"Topic: {topic}")

for topic, minutes in lesson_minutes.items():
    print(f"{topic}: {minutes} min")
