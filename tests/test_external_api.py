from unittest.mock import Mock, patch

import requests

from src.external_api import convert_rub


@patch("src.external_api.requests.get")
def test_convert_rub_success(mock_get) -> None:
    """Тестирует функцию convert_rub, успешную конвертацию USD -> RUB валюты через API"""
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"success": True, "result": 8000.0}
    mock_get.return_value = mock_response

    result = convert_rub(100, "USD")
    assert result == 8000.0


@patch("src.external_api.requests.get")
def test_convert_rub_rub(mock_get) -> None:
    """Тестирует функцию convert_rub, успешную конвертацию RUB -> RUB валюты через API"""
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"success": True, "result": 100.0}
    mock_get.return_value = mock_response

    result = convert_rub(100.0, "RUB")
    assert result == 100.0


@patch("src.external_api.requests.get")
def test_convert_rub_api_error(mock_get) -> None:
    """Тестирует функцию convert_rub с ошибкой 404"""
    mock_response = Mock()
    mock_response.status_code = 404
    mock_get.return_value = mock_response

    result = convert_rub(100, "USD")
    assert result == "Ошибка API 404"


@patch("src.external_api.requests.get")
def test_convert_rub_conversion_error(mock_get) -> None:
    """Тестирует функцию convert_rub со статусом success = False"""
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"success": False}
    mock_get.return_value = mock_response

    result = convert_rub(100, "USD")
    assert result == "Ошибка обработки запроса конвертации"


@patch("src.external_api.requests.get")
def test_convert_rub_http_exception(mock_get) -> None:
    """Тестирует функцию convert_rub с ошибкой HTTP"""
    mock_get.side_effect = requests.exceptions.RequestException("Network failure")

    result = convert_rub(100, "USD")
    assert result.startswith("Ошибка HTTP:")
