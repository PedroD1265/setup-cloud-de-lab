import pandas as pd
import os

def test_csv_processing():
    # Verifica que el archivo de salida exista
    assert os.path.exists('../data/salida.csv'), "El archivo salida.csv no existe."

    # Carga el archivo de salida
    df = pd.read_csv('../data/salida.csv')

    # Verifica que la columna 'Clasificacion' exista
    assert 'Clasificacion' in df.columns, "La columna 'Clasificacion' no fue creada."

    # Verifica que todos estén clasificados como 'mayor'
    assert all(df['Clasificacion'] == 'mayor'), "No todos los valores en 'Clasificacion' son 'mayor'."

