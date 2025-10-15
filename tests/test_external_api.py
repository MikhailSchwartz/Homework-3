import requests
from unittest.mock import patch, Mock
from src.external_api import convert_rub


@patch("src.external_api.requests.get")
def test_convert_rub_success(mock_get):
    """Тестирует успешную конвертацию USD -> RUB валюты через API"""
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"success": True, "result": 8000.0}
    mock_get.return_value = mock_response

    result = convert_rub(100, "USD")
    assert result == 8000.0



