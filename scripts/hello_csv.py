import pandas as pd

df = pd.read_csv("../data/sample.csv")
df["clasificacion"] = df["age"].apply(lambda x: "mayor" if x >= 18 else "menor")
df.to_csv("../data/salida.csv", index=False)

print("✅ CSV procesado y guardado como 'salida.csv'")
