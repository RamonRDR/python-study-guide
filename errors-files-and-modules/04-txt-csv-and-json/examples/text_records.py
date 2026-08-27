import os
import tempfile


with tempfile.TemporaryDirectory() as directory:
    path = os.path.join(directory, "topics.txt")

    with open(path, "w", encoding="utf-8") as file:
        file.write("Functions\n")
        file.write("Files\n")
        file.write("JSON\n")

    with open(path, "r", encoding="utf-8") as file:
        topics = [line.rstrip("\n") for line in file]

    print(topics)
