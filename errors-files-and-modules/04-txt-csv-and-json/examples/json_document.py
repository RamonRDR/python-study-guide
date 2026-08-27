import json
import os
import tempfile


profile = {
    "topic": "Files",
    "score": 88,
    "tags": ["io", "formats"],
    "complete": True,
}

with tempfile.TemporaryDirectory() as directory:
    path = os.path.join(directory, "profile.json")

    with open(path, "w", encoding="utf-8") as file:
        json.dump(profile, file, ensure_ascii=False, indent=2)

    with open(path, "r", encoding="utf-8") as file:
        restored = json.load(file)

    print(restored["topic"])
    print(restored["tags"])
    print(restored["complete"])
