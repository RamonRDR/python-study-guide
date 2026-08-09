skills = {"python", "sql"}

skills.add("git")
skills.update(["testing", "python"])
skills.remove("git")
skills.discard("missing")

print("Has Python:", "python" in skills)
print("Has Git:", "git" in skills)
print("Expected members:", skills == {"python", "sql", "testing"})
print("Count:", len(skills))
