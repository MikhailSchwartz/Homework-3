import pytest

from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


def test_filter_by_currency_normal(normal_transaction_list: list, normal_result_filter_by_currency_usd: list) -> None:
    """Тест работы функции при вводе полных данных и валюты USD"""

    result = list(filter_by_currency(normal_transaction_list, "USD"))
    assert result == normal_result_filter_by_currency_usd


def test_filter_by_currency_normal(normal_transaction_list: list, normal_result_filter_by_currency_rub: list) -> None:
    """Тест работы функции при вводе полных данных и валюты RUB"""

    result = list(filter_by_currency(normal_transaction_list, "RUB"))
    assert result == normal_result_filter_by_currency_rub
