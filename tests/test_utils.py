import json
from unittest.mock import mock_open, patch

from src.utils import transactions_load


def test_transactions_load_valid_json() -> None:
    """Тест функции transactions_load, корректного JSON (список транзакций)"""
    mock_data = json.dumps([{"amount": 31957.58, "currency": "USD"}])
    with patch("src.utils.open", mock_open(read_data=mock_data)):
        result = transactions_load("operations.json")
    assert isinstance(result, list)
    assert result == [{"amount": 31957.58, "currency": "USD"}]


def test_transactions_load_empty_list() -> None:
    """Тест функции transactions_load, с пустым списком"""
    mock_data = json.dumps([])
    with patch("src.utils.open", mock_open(read_data=mock_data)):
        result = transactions_load("operations.json")
    assert result == []


def test_transactions_load_file_not_found() -> None:
    """Тест функции transactions_load на отсутствие файла"""
    with patch("src.utils.open", side_effect=FileNotFoundError):
        result = transactions_load("operations.json")
    assert result == []


def test_transactions_load_json_decode_error() -> None:
    """Тест функции transactions_load, с некорректным содержимым файла"""
    mock_file = mock_open(read_data="{broken")
    with patch("src.utils.open", mock_file):
        result = transactions_load("operations.json")
    assert result == []
