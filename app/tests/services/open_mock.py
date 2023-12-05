import json


def open_mock(model: str):
    """Reads mock data."""
    with open(f"app/tests/mock_{model}.json", encoding="utf-8") as file:
        return json.load(file)
