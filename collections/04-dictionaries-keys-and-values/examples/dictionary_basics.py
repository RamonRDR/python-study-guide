profile = {
    "name": "Ana",
    "track": "Python",
    "level": "beginner",
}

print("Name:", profile["name"])
print("Level:", profile.get("level"))
print("Entries:", len(profile))
print("Has track:", "track" in profile)
