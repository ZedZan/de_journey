import psycopg2
import logging
import time
from datetime import datetime

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

SAMPLE_DATA = [
    {"id": 1, "name": "Alice", "sales": 4200,  "date": "2024-01-15"},
    {"id": 2, "name": "Bob",   "sales": 3100,  "date": "2024-01-15"},
    {"id": 3, "name": "Carol", "sales": "bad_value", "date": "2024-01-16"},  # 💥 bad data
    {"id": 4, "name": "Dave",  "sales": 5100,  "date": "2024-01-16"},
]

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

def get_connection():
    return psycopg2.connect(
        host="127.0.0.1",
        port=5433,
        dbname="dedb",
        user="deuser",
        password="pass123"
    )

def extract(data: list[dict]) -> list[dict]:
    logger.info(f"Extracting {len(data)} records")
    return data

def transform(records: list[dict]) -> list[dict]:
   transformed = []
   for record in records :
      try :      
        transformed.append({
            "id" : record["id"],
            "name" : record["name"],
            "sales" : float(record["sales"]),
            "date" : record["date"],
            "loaded_at" : datetime.now()
        })
        return transformed
      except ValueError :
          logger.warning(f"skipping record {record['name']} - invalid sales value: {record['sales']}")
             

def load_with_retry(records: list[dict], retries: int = 3, delay: int = 2) -> None:
    for attempt in range(retries):
        try:
            conn = get_connection()  # YOUR CODE: get the connection
            with conn.cursor() as cur:
                for r in records:
                    cur.execute("""
                        INSERT INTO sales (id, name, sales, date, loaded_at)
                        VALUES (%s, %s, %s, %s, %s)
                    """, (r["id"], r["name"], r["sales"], r["date"], r["loaded_at"] ))  
            conn.commit()
            logger.info(f"Attempt {attempt +1} succeeded")
            return 
        except Exception as e:
            logger.warning(f"Attempt {attempt +1} failed : {e}")
            time.sleep(delay)  # YOUR CODE: wait before retrying
    raise Exception ("all retries failed")
def run_pipeline():
    logger.info("=== Pipeline started ===")
    raw     = extract(SAMPLE_DATA)
    cleaned = transform(raw)
    
    if not cleaned:
        logger.error("No valid records to load. Aborting.")
        return
    
    load_with_retry(cleaned)
    logger.info("=== Pipeline finished ===")

if __name__ == "__main__":
    run_pipeline()