import logging
import psycopg2
from week1.config import Config

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

def get_connection(config):
    return psycopg2.connect(
        host=config.DB_HOST,
        port=config.DB_PORT,
        dbname=config.DB_NAME,
        user=config.DB_USER,
        password=config.DB_PASSWORD,
    )

def create_table(conn):
    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS dim_products (
                product_id  INTEGER PRIMARY KEY,
                name        varchar(100),
                category    varchar(100),
                price       FLOAT  
                    )
        """)
        cur.execute("""
            CREATE TABLE IF NOT EXISTS dim_customer (
                customer_id INTEGER PRIMARY KEY,
                name        varchar(100),
                city        varchar(100),
                country     varchar(100)
                    )
        """)
        cur.execute("""
            CREATE TABLE IF NOT EXISTS dim_date (
                date_id     INTEGER PRIMARY KEY,
                date        date,
                month       INTEGER,
                year        INTEGER,
                quarter     varchar(2)
                    )
        """)
        cur.execute("""
            CREATE TABLE IF NOT EXISTS fact_sales (
                id          INTEGER PRIMARY KEY,
                date_id     INTEGER,
                product_id  INTEGER,
                customer_id INTEGER,
                quantity    INTEGER,
                tota_amount FLOAT,
                FOREIGN KEY (date_id) REFERENCES dim_date(date_id),
                FOREIGN KEY (product_id) REFERENCES dim_products(product_id),
                FOREIGN KEY (customer_id) REFERENCES dim_customer(customer_id)
            )
        """)
    conn.commit()
    logger.info("Table ready")

if __name__ == "__main__":
    conn = get_connection(Config())
    create_table(conn)
    conn.close()