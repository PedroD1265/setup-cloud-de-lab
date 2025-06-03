# hello_postgres.py

import psycopg2

DB_NAME = "labdatos"
DB_USER = "postgres"
DB_PASSWORD = "1265"
DB_HOST = "192.168.1.8"
DB_PORT = 5432

try:
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )
    print("✅ Conexión exitosa a PostgreSQL")
    conn.close()
except Exception as e:
    print("❌ Error al conectar:", e)
