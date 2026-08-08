path_text = "docs/guides/python"

parts = path_text.split("/")

print("Parts:", parts)
print("Joined:", " > ".join(parts))
print("First separator:", path_text.find("/"))
print("Slash count:", path_text.count("/"))
print("Ends with python:", path_text.endswith("python"))
