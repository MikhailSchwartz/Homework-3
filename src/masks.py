def get_mask_card_number(card_number: str | int) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску XXXX XX** **** XXXX где X цифра"""

    card_str = str(card_number).replace(" ", "")

    if len(card_str) != 16:
        return "Номер карты должен содержать 16 цифр"

    return f"{card_str[:4]} {card_str[4:6]}** **** {card_str[12:]}"


def get_mask_account(account_number: str | int) -> str:
    """принимает на вход номер счета и возвращает его маску в формате **XXXX, где X это цифра"""

    account_str = str(account_number).replace(" ", "")

    return f"**{account_str[-4:]}"
