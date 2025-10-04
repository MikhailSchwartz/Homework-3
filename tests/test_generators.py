import pytest

from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


def test_filter_by_currency_normal_usd(
    normal_transaction_list: list, normal_result_filter_transaction_usd: list
) -> None:
    """Тест работы функции filter_by_currency при вводе полных данных и валюты USD"""

    result = list(filter_by_currency(normal_transaction_list, "USD"))
    assert result == normal_result_filter_transaction_usd


def test_filter_by_currency_normal_rub(
    normal_transaction_list: list, normal_result_filter_transaction_rub: list
) -> None:
    """Тест работы функции filter_by_currency при вводе полных данных и валюты RUB"""

    result = list(filter_by_currency(normal_transaction_list, "RUB"))
    assert result == normal_result_filter_transaction_rub


def test_filter_by_currency_defective_usd(
    defective_transaction_list: list, defective_result_filter_transaction_usd: list
) -> None:
    """Тест работы функции filter_by_currency при вводе неполных данных и валюты USD"""

    result = list(filter_by_currency(defective_transaction_list, "USD"))
    assert result == defective_result_filter_transaction_usd


def test_filter_by_currency_empty(epty_transaction_list: list) -> None:
    """Тест работы функции filter_by_currency при вводе полных данных и валюты RUB"""

    result = next(filter_by_currency(epty_transaction_list, "RUB"))
    assert result == "Данные отсутствуют"


def test_filter_by_currency_wrong(wrong_translation_list: list) -> None:
    """Тест работы функции filter_by_currency при вводе некорректных данных"""

    result = next(filter_by_currency(wrong_translation_list, "RUB"))
    assert (
        result
        == "Произошла ошибка: 'str' object has no attribute 'get'. Функция должна принимать на вход два аргумента: список со словарями и информацию о валюте"
    )


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


def test_transaction_descriptions_empty(epty_transaction_list: list) -> None:
    """Тест работы функции transaction_descriptions при вводе пустого списка"""

    result = next(transaction_descriptions(epty_transaction_list))
    assert result == "Данные отсутствуют"

def test_transaction_descriptions_wrong_list(wrong_translation_list: list) -> None:
    """Тест работы функции transaction_descriptions при вводе списка с некорректными данными"""

    result = next(transaction_descriptions(wrong_translation_list))
    assert result == "Некорректный тип данных элемента списка транзакций"


def test_transaction_descriptions_wrong(wrong_translation_tuple: tuple ) -> None:
    """Тест работы функции transaction_descriptions при вводе некорректных данных"""

    result = next(transaction_descriptions(wrong_translation_tuple))
    assert result == "Некорректный тип данных: ожидается список"


@pytest.mark.parametrize("start, stop, expected_first, expected_last", [
    (1, 3, "0000 0000 0000 0001", "0000 0000 0000 0003"),
    (9999999999999997, 9999999999999999, "9999 9999 9999 9997", "9999 9999 9999 9999"),
    (1000, 1000, "0000 0000 0000 1000", "0000 0000 0000 1000"),
])
def test_card_number_generator_ranges(start: int, stop: int, expected_first: str, expected_last: str) -> None:
    gen = card_number_generator(start, stop)
    result = list(gen)
    assert result[0] == expected_first
    assert result[-1] == expected_last


def test_value_error_start_less_than_1() -> None:
    with pytest.raises(ValueError) as exc_info:
        list(card_number_generator(0, 10))
    assert str(exc_info.value) == "Начальное значение не может быть меньше 1"


def test_value_error_stop_greater_than_max() -> None:
    with pytest.raises(ValueError) as exc_info:
        list(card_number_generator(1, 10000000000000000))
    assert str(exc_info.value) == "Конечное значение не может быть больше 9999999999999999"


def test_value_error_start_greater_than_stop() -> None:
     with pytest.raises(ValueError) as exc_info:
         list(card_number_generator(10, 5))
     assert str(exc_info.value) == "Значение stop значение не может быть меньше значения start"

@pytest.mark.parametrize("start, stop, expected_len", [
    (1, 1, 1),
    (9999999999999998, 9999999999999999, 2),
])
def test_card_number_generator_single_and_two_numbers(start, stop, expected_len):
    numbers = list(card_number_generator(start, stop))
    assert len(numbers) == expected_len
