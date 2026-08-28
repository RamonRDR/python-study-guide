import json


def reject_duplicate_keys(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON object name: {key}")
        result[key] = value
    return result


samples = [
    '{"topic": "JSON", "score": 88}',
    '{"topic": "JSON", "topic": "CSV"}',
]

for text in samples:
    try:
        data = json.loads(text, object_pairs_hook=reject_duplicate_keys)
    except ValueError as error:
        print(error)
    else:
        print(data)
