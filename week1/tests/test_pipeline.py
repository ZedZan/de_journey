from week1.pipelines.pipeline_v4 import transform

def test_transform_valid_records():
    # Step 1: create fake input (a list of dicts — just like SAMPLE_DATA)
    input_data = [{"id": 1, "name": "Alice", "sales": "4200", "date": "2024-01-15"}]

    # Step 2: call transform with that input
    result = transform(input_data)

    # Step 3: assert what you expect
    assert len(result) == 1  # how many records should come back?
    assert result[0]["name"] == "Alice"  # what should the name be?
    assert result[0]["sales"] == 4200  # what type should sales be after transform?


def test_transform_skips_bad_data():
    input_data = [
        {"id": 3, "name": "Carol", "sales": "bad_value", "date": "2024-01-16"}
    ]

    result = transform(input_data)

    assert len(result) == 0

def test_transform_all_bad_data():
    input_data = [
        {"id": 3, "name": "Carol", "sales": "bad_value", "date": "2024-01-16"},
        {"id": 1, "name": "Bob", "sales": "bad_value", "date": "2024-01-16"},
    ]

    result = transform(input_data)

    assert len(result) == 0