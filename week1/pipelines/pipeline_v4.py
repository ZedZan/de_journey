import psycopg2
import logging
import time
import csv
from datetime import datetime

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


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

def get_connection(config):
    return psycopg2.connect(
        host= config.DB_HOST,
        port= config.DB_PORT,
        dbname= config.DB_NAME,
        user= config.DB_USER,
        password= config.DB_PASSWORD
    )

def extract(filepath: str) -> list[dict]:
    with open(filepath, newline ='') as extractee:
        extracted = list(csv.DictReader(extractee, delimiter=','))
        logger.info(f"Extracted {len(extracted)}")
        return extracted

def transform(records: list[dict]) -> list[dict]:
    transformed = []
    for record in records:
        try:
            transformed.append({
                "id": record["id"],
                "name": record["name"],
                "sales": float(record["sales"]),
                "date": datetime.strptime(record["date"], "%Y-%m-%d").date(),
                "loaded_at": datetime.now()
            })
        except ValueError:
            logger.warning(f"Skipping record {record['name']} - invalid sales value: {record['sales']}")
    return transformed  # 👈 outside the loop
    

def load_with_retry(records: list[dict], config, retries: int = 3, delay: int = 2) -> None:
    for attempt in range(retries):
        try:
            conn = get_connection(config)  # YOUR CODE: get the connection
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
def run_pipeline(config):
    logger.info("=== Pipeline started ===")
    conn = get_connection(config)
    create_table(conn)
    raw     = extract("week1/data/sales.csv")
    cleaned = transform(raw)
    
    if not cleaned:
        logger.error("No valid records to load. Aborting.")
        return
    
    load_with_retry(cleaned, config)
    logger.info("=== Pipeline finished ===")

