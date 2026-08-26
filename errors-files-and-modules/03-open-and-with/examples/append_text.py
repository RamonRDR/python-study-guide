import os
import tempfile


with tempfile.TemporaryDirectory() as directory:
    path = os.path.join(directory, "history.txt")

    with open(path, "w", encoding="utf-8") as file:
        file.write("Chapter 01\n")

    with open(path, "a", encoding="utf-8") as file:
        file.write("Chapter 02\n")
        file.write("Chapter 03\n")

    with open(path, "r", encoding="utf-8") as file:
        print(file.read(), end="")
