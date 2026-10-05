import numpy as np
import pandas as pd

data = {
    "Employee": ["Arun", "Banu", "Cathy", "David", "Ezhil"],
    "Sales": [45000, 62000, 38000, 75000, 58000],
    "Target": [50000, 60000, 50000, 70000, 60000]
}

df = pd.DataFrame(data)

df["Difference"] = df["Sales"] - df["Target"]
df["Status"] = np.where(
    df["Sales"] >= df["Target"],
    "Target Achieved",
    "Target Not Achieved"
)

print("SALES TARGET ANALYSIS")
print(df)

print("\nTotal Sales:", np.sum(df["Sales"]))
print("Total Target:", np.sum(df["Target"]))
print("Targets Achieved:",
      (df["Status"] == "Target Achieved").sum())