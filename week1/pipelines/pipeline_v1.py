import logging
from datetime import datetime

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Pretend this came from a CSV file or an API
SAMPLE_DATA = [
    {"id": 1, "name": "Alice", "sales": 4200, "date": "2024-01-15"},
    {"id": 2, "name": "Bob", "sales": 3100, "date": "2024-01-15"},
    {"id": 3, "name": "Carol", "sales": 5800, "date": "2024-01-16"},
]


def extract(data: list[dict]) -> list[dict]:
    """Get raw data from the source."""
    logger.info(f"Extracting {len(data)} records")
    return data


def transform(records: list[dict]) -> list[dict]:
    """Clean and enrich the data."""
    transformed = []
    for r in records:
        transformed.append(
            {
                **r,
                "sales": float(r["sales"]),
                "date": datetime.strptime(r["date"], "%Y-%m-%d").date(),
                "loaded_at": datetime.now(),
            }
        )
    logger.info(f"Transformed {len(transformed)} records")
    return transformed


def load(records: list[dict]) -> None:
    """In a real pipeline this writes to a database."""
    for r in records:
        logger.info(f"Record ready: {r}")


def run_pipeline():
    logger.info("=== Pipeline started ===")
    raw = extract(SAMPLE_DATA)
    cleaned = transform(raw)
    load(cleaned)
    logger.info("=== Pipeline finished ===")


if __name__ == "__main__":
    run_pipeline()
