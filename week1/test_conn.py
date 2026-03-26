import psycopg2

try:
    conn = psycopg2.connect(
        host="127.0.0.1", port=5433, dbname="dedb", user="deuser", password="pass123"
    )
    print("CONNECTION SUCCESSFUL")
    conn.close()
except Exception as e:
    print(f"FAILED: {e}")
