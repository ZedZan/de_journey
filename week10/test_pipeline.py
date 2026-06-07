from week2.practice import extract_fields, filter_by_date_range, process_matches
import pytest

def test_extract_fields():
    data = [{"name": "Alice", "amount": 100, "country": "FR"}]
    result = extract_fields(data, ["name", "amount"])
    assert result == [{"name": "Alice", "amount": 100}]

def test_filter_by_date_range():
    records = [
        {"date": "2024-01-01", "name": "Alice"},
        {"date": "2024-02-15", "name": "Bob"},
        {"date": "2024-03-01", "name": "Charlie"},
    ]
    result = filter_by_date_range(records, "2024-01-01", "2024-02-15")
    assert result == [
        {"date": "2024-01-01", "name": "Alice"},
        {"date": "2024-02-15", "name": "Bob"},
    ]
def test_process_matches():
    result = process_matches("doesnotexist.json")
    assert result == []

def test_filter_by_date_range_no_result():
    records = [
        {"date": "2024-01-01", "name": "Alice"},
        {"date": "2024-02-15", "name": "Bob"},
        {"date": "2024-03-01", "name": "Charlie"},
    ]
    result = filter_by_date_range(records, "2025-01-01", "2026-02-15")
    assert result == []