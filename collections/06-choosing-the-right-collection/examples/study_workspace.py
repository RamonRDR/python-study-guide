course = {
    "title": "Python Study Guide",
    "phase": 3,
}
planned_topics = ["lists", "tuples", "dictionaries", "sets"]
checkpoint = (3, 4)
completed_topics = {"lists", "tuples"}

planned_topics.append("collection choices")
course["status"] = "in progress"
completed_topics.add("dictionaries")

print(course["title"])
print(planned_topics[0])
print(checkpoint)
print("dictionaries" in completed_topics)
print(len(completed_topics))
