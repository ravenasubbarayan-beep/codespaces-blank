import numpy as np
import pandas as pd

data = {
    "Customer": ["Asha", "Bala", "Chitra", "Deepa", "Eshan"],
    "Orders": [5, 8, 4, 10, 6],
    "Amount": [25000, 42000, 18000, 55000, 30000]
}

df = pd.DataFrame(data)

df["Average_Order_Value"] = df["Amount"] / df["Orders"]

print("CUSTOMER SALES ANALYSIS")
print(df)

print("\nTotal Revenue:", np.sum(df["Amount"]))
print("Average Revenue:", np.mean(df["Amount"]))

top = df.loc[df["Amount"].idxmax()]
print("\nHighest Value Customer:")
print(top)