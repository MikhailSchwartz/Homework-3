def get_mask_card_number(card_number: str | int) -> str:
    """Функция принимает на вход номер карты в формате "73654108430135874305"
    и возвращает ее маску XXXX XX** **** XXXX где X цифра"""

    card_str = str(card_number).replace(" ", "")

    if len(card_str) != 16 or not card_str.isdigit():
        raise ValueError("Номер карты должен содержать 16 цифр")

    return f"{card_str[:4]} {card_str[4:6]}** **** {card_str[12:]}"


def get_mask_account(account_number: str | int) -> str:
    """Функция принимает на вход номер в формате "73654108430135874305" счета
    и возвращает его маску в формате **XXXX, где X это цифра"""

    account_str = str(account_number).replace(" ", "")

    if not account_str.isdigit():
        raise ValueError("Номер счёта должен содержать только цифры")

    if len(account_str) < 4:
        raise ValueError("Номер счёта должен содержать минимум 4 цифры")

    return f"**{account_str[-4:]}"


if __name__ == "__main__":
    print(get_mask_card_number(7000792289606361))
    print(get_mask_account(736541084301358743059988))
