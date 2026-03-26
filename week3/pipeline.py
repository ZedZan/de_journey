import psycopg2
import logging
import time
import csv
from datetime import datetime

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


class Pipeline:
    def __init__(self, config):
        self.config = config
        self.conn = None

    def connect(self):
        self.conn = psycopg2.connect(
            host=self.config.DB_HOST,
            port=self.config.DB_PORT,
            dbname=self.config.DB_NAME,
            user=self.config.DB_USER,
            password=self.config.DB_PASSWORD,
        )

    def create_table(self):
        with self.conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS sales(
                 id          INTEGER,
                name        VARCHAR(100),
                sales       FLOAT,
                date        DATE,
                loaded_at   TIMESTAMP
                )
                """)
            self.conn.commit()
            logger.info("Table ready!")

    def extract(self, filepath: str) -> list[dict]:
        with open(filepath, newline="") as extractee:
            extracted = list(csv.DictReader(extractee, delimiter=","))
            logger.info(f"Extracted {len(extracted)}")
            return extracted

    def transform(self, records: list[dict]) -> list[dict]:
        transformed = []
        for record in records:
            try:
                transformed.append(
                    {
                        "id": record["id"],
                        "name": record["name"],
                        "sales": float(record["sales"]),
                        "date": datetime.strptime(record["date"], "%Y-%m-%d").date(),
                        "loaded_at": datetime.now(),
                    }
                )
            except ValueError:
                logger.warning(
                    f"Skipping record {record['name']} - invalid sales value: {record['sales']}"
                )
        return transformed  # 👈 outside the loop

    def load_with_retry(
        self, records: list[dict], retries: int = 3, delay: int = 2
    ) -> None:
        for attempt in range(retries):
            try:
                with self.conn.cursor() as cur:
                    for r in records:
                        cur.execute(
                            """
                            INSERT INTO sales (id, name, sales, date, loaded_at)
                            VALUES (%s, %s, %s, %s, %s)
                        """,
                            (r["id"], r["name"], r["sales"], r["date"], r["loaded_at"]),
                        )
                self.conn.commit()
                logger.info(f"Attempt {attempt +1} succeeded")
                return
            except Exception as e:
                logger.warning(f"Attempt {attempt +1} failed : {e}")
                time.sleep(delay)  # YOUR CODE: wait before retrying
        raise Exception("all retries failed")

    def run(self):
        logger.info("=== Pipeline started ===")
        self.connect()
        self.create_table()
        raw = self.extract("week1/data/sales.csv")
        cleaned = self.transform(raw)

        if not cleaned:
            logger.error("No valid records to load. Aborting.")
            return

        self.load_with_retry(cleaned)
        logger.info("=== Pipeline finished ===")

    def close(self):
        if self.conn:
            self.conn.close()
            logger.info("Connection closed")


if __name__ == "__main__":
    from week1.config import Config

    pipeline = Pipeline(Config())
    pipeline.run()
    pipeline.close()
