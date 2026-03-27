import csv
import logging
from week3.base_pipeline import BasePipeline
from datetime import datetime
from week3.config import Config

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


class SalesPipeline(BasePipeline):
    def __init__(self, config):
        super().__init__(config)

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

    def extract(self, filepath: str):
        with open(filepath, newline="") as extractee:
            extracted = list(csv.DictReader(extractee, delimiter=","))
            logger.info(f"Extracted{len(extracted)}")
            return extracted

    def transform(self, records):
        transformed = []
        for r in records:
            try:
                transformed.append(
                    {
                        "id": r["id"],
                        "name": r["name"],
                        "sales": float(r["sales"]),
                        "date": datetime.strptime(r["date"], "%Y-%m-%d").date(),
                        "loaded_at": datetime.now(),
                    }
                )
            except ValueError:
                logger.warning(
                    f"Skipping record {r['name']} - invalid sales value: {r['sales']}"
                )
        return transformed

    def load(self, records):
        def _insert():
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

        self._execute_with_retry(_insert)

    def run(self):
        logger.info("=== Pipeline started ===")
        self.connect()
        self.create_table()
        raw = self.extract("week1/data/sales.csv")
        cleaned = self.transform(raw)

        if not cleaned:
            logger.error("No valid records to load. Aborting.")
            return

        self.load(cleaned)
        logger.info("=== Pipeline finished ===")


if __name__ == "__main__":
    pipeline = SalesPipeline(Config())
    pipeline.run()
    pipeline.close()
