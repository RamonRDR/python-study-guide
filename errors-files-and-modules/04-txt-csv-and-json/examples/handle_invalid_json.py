import json


text = '{"topic": "Files",}'

try:
    data = json.loads(text)
except json.JSONDecodeError:
    print("Invalid JSON")
else:
    print(data)
