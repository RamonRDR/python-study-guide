topics = ["conditions", "loops", "helpers"]
minutes = [25, 40, 30]

for topic, duration in zip(topics, minutes, strict=True):
    print(f"{topic}: {duration} min")
