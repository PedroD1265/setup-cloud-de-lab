import pandas as pd
from pathlib import Path

DATA_DIR = Path("data")

def cargar_csv(nombre_archivo: str) -> pd.DataFrame:
    """Carga un CSV desde data/ y devuelve un DataFrame."""
    ruta = DATA_DIR / nombre_archivo
    return pd.read_csv(ruta)

def mostrar_info(df: pd.DataFrame) -> None:
    """Imprime el DataFrame, el número de filas y la columna name."""
    print(df)
    print(f"Filas totales: {df.shape[0]}")
    print("Columna name:")
    print(df["name"])

def main() -> None:
    df = cargar_csv("sample.csv")
    mostrar_info(df)

if __name__ == "__main__":
    main()
