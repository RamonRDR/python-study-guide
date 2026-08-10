age = 28
minimum_age = 18
maximum_age = 65
topics = ["strings", "numbers", "collections"]
profile = {"name": "Ava", "level": "beginner"}

print("At least 18:", age >= minimum_age)
print("Under 65:", age < maximum_age)
print("Inside interval:", minimum_age <= age < maximum_age)
print("Collections available:", "collections" in topics)
print("Name key exists:", "name" in profile)
print("Email key missing:", "email" not in profile)
