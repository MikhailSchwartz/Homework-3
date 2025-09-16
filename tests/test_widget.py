import pytest
from src.widget import mask_account_card, get_date


@pytest.mark.parametrize("valid_input, expected",
                         [("Счет 73654108430135874305", "Счет **4305"),
                          ("счет 73654108430135874305", "счет **4305"),
                          ("Счёт 73654108430135874305", "Счёт **4305"),
                          ("Visa Platinum 7000792289606360", "Visa Platinum 7000 79** **** 6360"),
                          ("Maestro 7000792289606362", "Maestro 7000 79** **** 6362"),
                          ("  Счет  73654108430135874305  ", "Счет **4305"),
                          ])

def test_mask_account_card_valid(valid_input, expected):
    """Тестирование при вводе корректных данных"""
    assert mask_account_card(valid_input) == expected


@pytest.mark.parametrize("invalid_input",
                         [ "",
                           "Visa Platinum",
                           "1234567812345678",
                           "Invalid Input",
                           "   ",
                           "Visa1234567812345678",
                           "Счёт"])

def test_mask_account_card_invalid_inputs(invalid_input):
    """Тест обработки при вводе некорректных данных"""
    with pytest.raises(ValueError) as exc_info:
        mask_account_card(invalid_input)

    assert str(exc_info.value) == "Неполные данные о карте или счёте."





