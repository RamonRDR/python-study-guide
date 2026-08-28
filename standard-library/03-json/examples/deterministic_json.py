import json


data = {"status": "ready", "score": 88, "topic": "JSON"}
text = json.dumps(
    data,
    ensure_ascii=False,
    sort_keys=True,
    separators=(",", ":"),
)

print(text)
