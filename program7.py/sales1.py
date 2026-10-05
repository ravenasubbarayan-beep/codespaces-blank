import numpy as np
import pandas as pd

data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May"],
    "Sales": [20000, 24000, 22000, 30000, 36000]
}

df = pd.DataFrame(data)

df["Growth"] = df["Sales"].pct_change() * 100

print("SALES GROWTH ANALYSIS")
print(df)
