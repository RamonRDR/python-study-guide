topics = ["strings", "lists", "sets", "lists", "sets"]
unique_topics = set(topics)

print("Unique topics:", len(unique_topics))
print("Has lists:", "lists" in unique_topics)
print("Has dictionaries:", "dictionaries" in unique_topics)
print("Expected members:", unique_topics == {"strings", "lists", "sets"})
