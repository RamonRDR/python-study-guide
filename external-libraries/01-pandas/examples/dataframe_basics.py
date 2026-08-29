import pandas as pd


data = {
    "product": ["Notebook", "Keyboard", "Mouse"],
    "units": [2, 5, 8],
    "unit_price": [3500.0, 180.0, 95.0],
}

sales = pd.DataFrame(data)
sales["total"] = sales["units"] * sales["unit_price"]

print(f"shape: {sales.shape}")
print(f"columns: {sales.columns.tolist()}")
print(f"grand total: {sales['total'].sum():.2f}")
