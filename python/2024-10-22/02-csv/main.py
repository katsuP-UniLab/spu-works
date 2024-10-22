import pandas as pd

df = pd.read_csv("../expense.csv")

print(df.to_string(index=False))
