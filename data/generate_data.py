import pandas as pd
import numpy as np

np.random.seed(42)

dates = pd.date_range(start="2023-01-01", periods=180)

data = []

products = ["P1", "P2", "P3"]
stores = ["S1", "S2"]

for store in stores:
    for product in products:
        base = np.random.randint(30, 80)

        for date in dates:
            sales = base + np.random.randint(-10, 15)

            data.append({
                "date": date,
                "store": store,
                "product": product,
                "sales": max(sales, 0),
                "stock": np.random.randint(50, 150)
            })

df = pd.DataFrame(data)
df.to_csv("data/retail_data.csv", index=False)

print("✅ Multi-product dataset created!")