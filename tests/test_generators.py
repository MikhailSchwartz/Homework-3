import pytest

from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


def test_filter_by_currency_normal_usd(
    normal_transaction_list: list, normal_result_filter_by_currency_usd: list
) -> None:
    """Тест работы функции filter_by_currency при вводе полных данных и валюты USD"""

    result = list(filter_by_currency(normal_transaction_list, "USD"))
    assert result == normal_result_filter_by_currency_usd


def test_filter_by_currency_normal_rub(
    normal_transaction_list: list, normal_result_filter_by_currency_rub: list
) -> None:
    """Тест работы функции filter_by_currency при вводе полных данных и валюты RUB"""

    result = list(filter_by_currency(normal_transaction_list, "RUB"))
    assert result == normal_result_filter_by_currency_rub


def test_filter_by_currency_defective_usd(
    defective_transaction_list: list, defective_result_filter_by_currency_usd: list
) -> None:
    """Тест работы функции filter_by_currency при вводе неполных данных и валюты USD"""

    result = list(filter_by_currency(defective_transaction_list, "USD"))
    assert result == defective_result_filter_by_currency_usd


def test_filter_by_currency_empty(epty_transaction_list: list) -> None:
    """Тест работы функции filter_by_currency при вводе полных данных и валюты RUB"""

    result = next(filter_by_currency(epty_transaction_list, "RUB"))
    assert result == "Данные отсутствуют"


def test_transaction_descriptions_normal(normal_transaction_list: list) -> None:
    """Тест работы функции transaction_descriptions при вводе полных данных"""

    result = list(transaction_descriptions(normal_transaction_list))
    assert result == [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации",
    ]


def test_transaction_descriptions_defective(defective_transaction_list: list) -> None:
    """Тест работы функции transaction_descriptions при вводе неполных данных"""

    result = list(transaction_descriptions(defective_transaction_list))
    assert result == [
        "Информации об операции недостаточно",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации",
    ]


def test_transaction_descriptions_one(one_transaction_list: list) -> None:
    """Тест работы функции transaction_descriptions при вводе информации об одной операции"""

    result = next(transaction_descriptions(one_transaction_list))
    assert result == "Перевод организации"

