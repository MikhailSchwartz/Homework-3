import pytest
from src.widget import mask_account_card, get_date


@pytest.mark.parametrize("input_string, expected",
                         [("Счет 73654108430135874305", "Счет **4305"),
                          ("счет 12345678901234567890", "счет **7890"),
                          ("Счёт 98765432109876543210", "Счёт **3210"),
                          ("Visa Platinum 1234567812345678", "Visa Platinum 1234 56** **** 5678")])

def test_mask_account_card_valid(input_string, expected):
    """Тестирование корректных входных данных"""
    assert mask_account_card(input_string) == expected