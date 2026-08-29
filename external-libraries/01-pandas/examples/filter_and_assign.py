import pandas as pd


orders = pd.DataFrame(
    {
        "order_id": [101, 102, 103, 104],
        "status": ["paid", "pending", "paid", "paid"],
        "amount": [120.0, 80.0, 250.0, 90.0],
    }
)

orders["priority"] = "normal"
orders.loc[(orders["status"] == "paid") & (orders["amount"] >= 200), "priority"] = "high"

selected = orders.loc[orders["status"] == "paid", ["order_id", "priority"]]
print(selected.to_dict(orient="records"))
