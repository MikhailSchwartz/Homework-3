import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "valid_input, expected",
    [
        ("Счет 73654108430135874305", "Счет **4305"),
        ("счет 73654108430135874305", "счет **4305"),
        ("Счёт 73654108430135874305", "Счёт **4305"),
        ("Visa Platinum 7000792289606360", "Visa Platinum 7000 79** **** 6360"),
        ("Maestro 7000792289606362", "Maestro 7000 79** **** 6362"),
        ("  Счет  73654108430135874305  ", "Счет **4305"),
    ],
)
def test_mask_account_card_valid(valid_input: str, expected: str) -> None:
    """Тестирование при вводе корректных данных"""
    assert mask_account_card(valid_input) == expected


@pytest.mark.parametrize(
    "invalid_input", ["", "Visa Platinum", "1234567812345678", "Invalid Input", "   ", "Visa1234567812345678", "Счёт"]
)
def test_mask_account_card_invalid_inputs(invalid_input: str) -> None:
    """Тест обработки при вводе некорректных данных"""
    with pytest.raises(ValueError) as exc_info:
        mask_account_card(invalid_input)

    assert str(exc_info.value) == "Неполные данные о карте или счёте."


@pytest.mark.parametrize(
    "input_date, expected",
    [
        # Основные случаи
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2024-12-31T23:59:59.999999", "31.12.2024"),
        ("2024-01-01T00:00:00.", "01.01.2024"),
        ("2024-03-11T", "11.03.2024"),
        ("  2024-03-11T02:26:18.671407  ", "11.03.2024"),
    ],
)
def test_get_date_valid_format(input_date: str, expected: str) -> None:
    """Тест преобразования при вводе корректных дат в формате ISO 8601"""
    assert get_date(input_date) == expected


def test_get_date_invalid_format(invalid_data_iso: str) -> None:
    with pytest.raises(ValueError) as exc_info:
        get_date(invalid_data_iso)

    assert str(exc_info.value) == "Строка не содержит даты в формате ISO 8601."


@pytest.mark.parametrize("invalid_format_date", ["2024-03-1T02:26:18", "2024-3-11T02:26:18", "24-03-11T02:26:18"])
def test_get_date_invalid_formats(invalid_format_date: str) -> None:
    """Тест обработки при вводе некорректных форматов дат"""
    with pytest.raises(ValueError) as exc_info:
        get_date(invalid_format_date)

    assert str(exc_info.value) == "Некорректный формат даты."


@pytest.mark.parametrize("incorrect_date", ["0999-03-11T02:26:18", "2010-32-11T02:26:18", "0000-03-11T02:26:18"])
def test_get_date_incorrect_dates(incorrect_date: str) -> None:
    """Тест обработки при вводе некорректных дат"""
    with pytest.raises(ValueError) as exc_info:
        get_date(incorrect_date)

    assert str(exc_info.value) == "Некорректная дата"
