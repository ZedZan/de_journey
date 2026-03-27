import psycopg2
import logging
import time

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


class BasePipeline:
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

    def close(self):
        if self.conn:
            self.conn.close()
            logger.info("Connection closed")

    def _execute_with_retry(self, func, retries=3, delay=2):
        for attempt in range(retries):
            try:
                func()
                return
            except Exception as e:
                logger.warning(f"Attempt {attempt +1} failed ! {e}")
                time.sleep(delay)

        raise Exception("All retries failed")
