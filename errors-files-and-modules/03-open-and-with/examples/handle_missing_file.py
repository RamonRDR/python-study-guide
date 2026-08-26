import os
import tempfile


with tempfile.TemporaryDirectory() as directory:
    path = os.path.join(directory, "optional.txt")

    try:
        with open(path, "r", encoding="utf-8") as file:
            content = file.read()
    except FileNotFoundError:
        content = "default settings"

    print(content)
