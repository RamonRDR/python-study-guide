from pathlib import Path
from tempfile import TemporaryDirectory

import pandas as pd


with TemporaryDirectory() as temp_dir:
    workspace = Path(temp_dir)
    source = workspace / "orders.csv"
    destination = workspace / "paid_orders.csv"

    source.write_text(
        "order_id,date,status,amount\n"
        "1,2026-08-01,paid,120.50\n"
        "2,2026-08-02,pending,80.00\n"
        "3,2026-08-03,paid,250.00\n",
        encoding="utf-8",
    )

    orders = pd.read_csv(source, parse_dates=["date"])
    paid_orders = orders.loc[orders["status"] == "paid"].sort_values("order_id")
    paid_orders.to_csv(destination, index=False)

    print(f"rows: {len(paid_orders)}")
    print(f"total: {paid_orders['amount'].sum():.2f}")
    print(f"saved: {destination.name}")
