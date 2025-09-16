import pytest
from src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("7000792289606361", "7000 79** **** 6361"),
        (7000792289606361, "7000 79** **** 6361"),
        ("7000 7922 8960 6361", "7000 79** **** 6361"),
    ],
)
def test_get_mask_card_number_valid(card_number, expected):
    """Тестирование при вводе корректных номеров карт"""
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize(
    "invalid_card",
    [
        "70007922896",
        "70007922896063615566",
        "number",
        "",
    ],
)
def test_get_mask_card_number_invalid(invalid_card):
    """Тестирование при вводе некорректных номеров"""
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number(invalid_card)

    assert str(exc_info.value) == "Номер карты должен содержать 16 цифр"


@pytest.mark.parametrize(
    "account_number, expected",
    [
        (73654108430135874305, "**4305"),
        ("73654108430135874305", "**4305"),
        ("7365410843013587", "**3587"),
        ("7365 4108 4301 3587 4305", "**4305"),
    ],
)
def test_get_mask_account_valid(account_number, expected):
    """Тестирование при вводе корректных номеров счетов"""
    assert get_mask_account(account_number) == expected


@pytest.mark.parametrize("invalid_account_number", ["7365-4108-4301-3587-4305", "account", "     ", ""])
def test_get_mask_account_invalid_chars(invalid_account_number):
    """Тестирование при вводе номеров счетов с недопустимыми символами"""
    with pytest.raises(ValueError) as exc_info:
        get_mask_account(invalid_account_number)

    assert str(exc_info.value) == "Номер счёта должен содержать только цифры"


@pytest.mark.parametrize("short_account_number", ["763", "76", "7"])
def test_get_mask_account_short_number(short_account_number):
    """Тестирование при вводе коротких номеров счетов"""
    with pytest.raises(ValueError) as exc_info:
        get_mask_account(short_account_number)

    assert str(exc_info.value) == "Номер счёта должен содержать минимум 4 цифры"
