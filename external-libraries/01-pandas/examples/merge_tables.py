import pandas as pd


orders = pd.DataFrame(
    {
        "order_id": [1, 2, 3],
        "customer_id": [10, 20, 10],
        "amount": [50.0, 80.0, 30.0],
    }
)
customers = pd.DataFrame(
    {
        "customer_id": [10, 20],
        "customer": ["Aster", "Boreal"],
    }
)

report = orders.merge(customers, on="customer_id", how="left", validate="many_to_one")
report = report[["order_id", "customer", "amount"]].sort_values("order_id")

print(report.to_dict(orient="records"))
