import csv
import logging
import psycopg2
import time
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def get_connection(config):
    return psycopg2.connect(
        host= config.DB_HOST,
        port= config.DB_PORT,
        dbname= config.DB_NAME,
        user= config.DB_USER,
        password= config.DB_PASSWORD
    )


def extract(filepath :str) -> list[dict] :
    with open(filepath, "r") as extractee :
        extracted = list(csv.DictReader(extractee, delimiter=','))
        logger.info(f"Extracted  {len(extracted)}")
    return extracted

def load_with_retry(records, conn, query, values_fn, retries=3, delay=2):
    for attempt in range(retries):
        try:
            with conn.cursor() as cur:
                for r in records:
                    cur.execute(query, values_fn(r))
            conn.commit()
            logger.info(f"Attempt {attempt+1} succeeded")
            return
        except Exception as e:
            logger.warning(f"Attempt {attempt+1} failed: {e}")
            time.sleep(delay)
    raise Exception("all retries failed")

BASE_DIR = Path(__file__).parent  # always points to week2/ folder
def run(config):
    conn = get_connection(config)
    raw_products = extract("week2/data/dim_products.csv")
    raw_date = extract("week2/data/dim_date.csv")
    raw_customer = extract("week2/data/dim_customer.csv")
    raw_fact = extract("week2/data/fact_sales.csv")

    load_with_retry(
        raw_products,
        conn,
        "INSERT INTO dim_products VALUES (%s, %s, %s, %s)",
        lambda r: (r["product_id"], r["name"], r["category"], r["price"])
)
    load_with_retry(
        raw_customer,
        conn,
        "INSERT INTO dim_customer VALUES (%s, %s, %s, %s)",
        lambda r: (r["customer_id"], r["name"], r["city"], r["country"])
    )
    
    load_with_retry(
        raw_date,
        conn,
        "INSERT INTO dim_date VALUES (%s, %s, %s, %s, %s)",
        lambda r: (r["date_id"], r["date"], r["month"], r["year"], r["quarter"])
    )
    
    load_with_retry(
        raw_fact,
        conn,
        "INSERT INTO fact_sales VALUES (%s, %s, %s, %s, %s, %s)",
        lambda r: (r["id"], r["date_id"], r["product_id"], r["customer_id"], r["quantity"], r["total_amount"])
    )



if __name__ == "__main__":
    from week1.config import Config
    run(Config())

