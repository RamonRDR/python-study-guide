planned_topics = ["strings", "lists", "tuples"]
fixed_version = (3, 13)
student = {"name": "Mina", "active": False}
skills = {"python", "git"}

planned_topics.append("dictionaries")
student["active"] = True
skills.add("sql")

print(len(planned_topics))
print(fixed_version[0])
print(student["active"])
print("sql" in skills)
