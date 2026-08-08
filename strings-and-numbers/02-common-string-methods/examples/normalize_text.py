raw_title = "  Python Study Guide  "

clean_title = raw_title.strip()
normalized_title = clean_title.lower().replace(" ", "-")

print("Raw:", "[" + raw_title + "]")
print("Clean:", clean_title)
print("Normalized:", normalized_title)
print("Starts with python:", clean_title.lower().startswith("python"))
print("Word count:", len(clean_title.split()))
