import json


def reject_nonstandard_constant(value: str):
    raise ValueError(f"non-standard JSON constant: {value}")


try:
    json.dumps({"value": float("nan")}, allow_nan=False)
except ValueError:
    print("Encoding rejected non-finite float")

try:
    json.loads('{"value": NaN}', parse_constant=reject_nonstandard_constant)
except ValueError:
    print("Decoding rejected non-standard constant")
