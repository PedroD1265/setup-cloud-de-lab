import psycopg2
import csv

# Parámetros de conexión (ajusta si cambias IP o credenciales)
DB_NAME = "labdatos"
DB_USER = "postgres"
DB_PASSWORD = "1265"
DB_HOST = "192.168.1.8"
DB_PORT = 5432

# Nombre del archivo CSV de salida
CSV_FILE = "usuarios_export.csv"

try:
    # 1. Conectar a PostgreSQL
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )
    cursor = conn.cursor()

    # 2. Ejecutar consulta para obtener todos los registros
    cursor.execute("SELECT id, nombre, edad FROM usuarios;")
    filas = cursor.fetchall()  # lista de tuplas

    # 3. Abrir (o crear) el archivo CSV y escribir encabezados + filas
    with open(CSV_FILE, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        # Escribimos la fila de encabezados
        writer.writerow(["id", "nombre", "edad"])
        # Escribimos cada fila de datos
        for fila in filas:
            writer.writerow(fila)

    # 4. Cerrar cursor y conexión
    cursor.close()
    conn.close()

    print(f"✅ Datos exportados correctamente a '{CSV_FILE}'")

except Exception as e:
    print("❌ Error durante la exportación:", e)
