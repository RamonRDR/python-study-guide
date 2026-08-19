import os
import tempfile


with tempfile.TemporaryDirectory() as directory:
    path = os.path.join(directory, "topics.txt")

    with open(path, "w", encoding="utf-8") as file:
        file.write("Functions\n")
        file.write("Exceptions\n")
        file.write("Files\n")

    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            print(line.rstrip("\n"))
