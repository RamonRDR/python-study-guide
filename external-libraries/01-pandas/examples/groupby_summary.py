import pandas as pd


transactions = pd.DataFrame(
    {
        "category": ["books", "games", "books", "games", "office"],
        "amount": [40.0, 120.0, 35.0, 80.0, 25.0],
    }
)

summary = (
    transactions.groupby("category", as_index=False)
    .agg(total_amount=("amount", "sum"), transaction_count=("amount", "size"))
    .sort_values("category")
)

print(summary.to_dict(orient="records"))
