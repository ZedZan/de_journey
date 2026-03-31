from unittest.mock import MagicMock
from week3.sales_pipeline import SalesPipeline
from week3.config import Config
import tempfile
import os

# Instead of a real connection, use a fake one
mock_conn = MagicMock()


def test_transform_valid_records():
    pipeline = SalesPipeline(Config())
    result = pipeline.transform(
        [{"id": 1, "name": "Alice", "sales": "4200", "date": "2024-01-15"}]
    )
    assert len(result) == 1
    assert result[0]["name"] == "Alice"
    assert result[0]["sales"] == 4200


def test_transform_skips_bad_data():
    pipeline = SalesPipeline(Config())
    result = pipeline.transform(
        [{"id": 5, "name": 44, "sales": "bad_value", "date": "3055-14-15"}]
    )
    assert len(result) == 0


def test_transform_returns_empty_for_all_bad():
    pipeline = SalesPipeline(Config())
    result = pipeline.transform(
        [
            {"id": 3, "name": "Carol", "sales": "bad_value", "date": "2024-01-16"},
            {"id": 1, "name": "Bob", "sales": "bad_value", "date": "2024-01-16"},
        ]
    )
    assert len(result) == 0


def test_extract_reads_csv():
    pipeline = SalesPipeline(Config())

    # create a temporary CSV file
    with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False) as f:
        f.write("id,name,sales,date\n")
        f.write("1,Alice,4200,2024-01-15\n")
        temp_path = f.name

    result = pipeline.extract(temp_path)
    assert len(result) == 1
    assert result[0]["name"] == "Alice"

    os.unlink(temp_path)  # delete temp file
