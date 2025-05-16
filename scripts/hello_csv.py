import pandas as pd

df = pd.read_csv("scripts/data/sample.csv")
print(df)
print(df.shape[0])
print(df["name"])
