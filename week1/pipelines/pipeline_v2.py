import logging
import os
import psycopg2  # replaces psycopg2
from datetime import datetime




logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

SAMPLE_DATA = [
    {"id": 1, "name": "Alice", "sales": 4200, "date": "2024-01-15"},
    {"id": 2, "name": "Bob",   "sales": 3100, "date": "2024-01-15"},
    {"id": 3, "name": "Carol", "sales": 5800, "date": "2024-01-16"},
]

def get_connection():
    return psycopg2.connect(
        host="127.0.0.1",
        port=5433,
        dbname="dedb",
        user="deuser",
        password="pass123"
    )
def create_table(conn):
    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS sales (
                id          INTEGER,
                name        VARCHAR(100),
                sales       FLOAT,
                date        DATE,
                loaded_at   TIMESTAMP
            )
        """)
    conn.commit()
    logger.info("Table ready")

def extract(data: list[dict]) -> list[dict]:
    logger.info(f"Extracting {len(data)} records")
    return data

def transform(records: list[dict]) -> list[dict]:
    transformed = []
    for r in records:
        transformed.append({
            **r,
            "sales": float(r["sales"]),
            "date": datetime.strptime(r["date"], "%Y-%m-%d").date(),
            "loaded_at": datetime.now()
        })
    logger.info(f"Transformed {len(transformed)} records")
    return transformed

def load(records: list[dict], conn) -> None:
    with conn.cursor() as cur:
        for r in records:
            cur.execute("""
                INSERT INTO sales (id, name, sales, date, loaded_at)
                VALUES (%s, %s, %s, %s, %s)
            """, (r["id"], r["name"], r["sales"], r["date"], r["loaded_at"]))
    conn.commit()
    logger.info(f"Loaded {len(records)} records into database")
def run_pipeline():
    logger.info("=== Pipeline started ===")
    conn = get_connection()

    try:
        create_table(conn)
        raw     = extract(SAMPLE_DATA)
        cleaned = transform(raw)
        load(cleaned, conn)
        logger.info("=== Pipeline finished ===")
    except Exception as e:
        logger.error(f"Pipeline failed: {e}")
        conn.rollback()
        raise
    finally:
        conn.close()

if __name__ == "__main__":
    run_pipeline()