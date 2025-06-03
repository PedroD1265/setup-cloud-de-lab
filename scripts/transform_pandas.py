import pandas as pd

# 1. Leer el CSV generado previamente
df = pd.read_csv("usuarios_export.csv")

# 2. Mostrar las primeras filas (opcional)
print("Primeras filas:")
print(df.head(), "\n")

# 3. Calcular edad promedio
promedio_edad = df["edad"].mean()
print(f"Edad promedio: {promedio_edad}\n")

# 4. Filtrar usuarios con edad > 25
df_mayores_25 = df[df["edad"] > 25]

# 5. Guardar los filtrados en un nuevo CSV
df_mayores_25.to_csv("usuarios_mayores_25.csv", index=False)

print("Archivo 'usuarios_mayores_25.csv' creado correctamente.")
