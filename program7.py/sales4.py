import numpy as np
import pandas as pd

data = {
    "Product": ["Laptop", "Phone", "Tablet", "Monitor", "Printer"],
    "Price": [60000, 30000, 25000, 18000, 12000],
    "Quantity": [2, 5, 4, 3, 6],
    "Discount": [10, 5, 8, 10, 5]
}

df = pd.DataFrame(data)

df["Gross_Sales"] = df["Price"] * df["Quantity"]
df["Discount_Amount"] = (
    df["Gross_Sales"] * df["Discount"] / 100
)
df["Net_Sales"] = (
    df["Gross_Sales"] - df["Discount_Amount"]
)

print("DISCOUNT AND NET SALES ANALYSIS")
print(df)

print("\nGross Sales:",
      np.sum(df["Gross_Sales"]))
print("Total Discount:",
      np.sum(df["Discount_Amount"]))
print("Net Sales:",
      np.sum(df["Net_Sales"]))