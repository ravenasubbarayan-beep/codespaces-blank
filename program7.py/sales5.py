import numpy as np
import pandas as pd

data = {
    "Category": [
        "Electronics", "Clothing", "Electronics",
        "Food", "Clothing", "Food"
    ],
    "Sales": [80000, 45000, 65000, 30000, 55000, 40000]
}

df = pd.DataFrame(data)

category_sales = df.groupby("Category")["Sales"].sum()

print("CATEGORY SALES ANALYSIS")
print(df)

print("\nCategory-wise Sales:")
print(category_sales)

print("\nTotal Sales:",
      np.sum(df["Sales"]))

print("Average Sale:",
      np.mean(df["Sales"]))

print("Best Category:",
      category_sales.idxmax())