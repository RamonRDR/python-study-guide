import json
from decimal import Decimal


data = json.loads(
    '{"price": 19.90, "quantity": 3}',
    parse_float=Decimal,
)

print(data["price"])
print(type(data["price"]).__name__)
print(type(data["quantity"]).__name__)
