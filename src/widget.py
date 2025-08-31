from masks import get_mask_account, get_mask_card_number


def mask_account_card(account_details: str) -> str:
    """Функция принимает тип и номер карты или счета,
    возвращает строку с замаскированным номером"""

    account_details_list = account_details.split()
    types = []
    numbers = []

    for element in account_details_list:
        if element.isalpha():
            types.append(element)
        elif element.isdigit():
            numbers.append(element)

    numbers_str = "".join(numbers)
    types_str = " ".join(types)

    if "счет" in types_str.lower() or "счёт" in types_str.lower():
        return f"{types_str} {get_mask_account(numbers_str)}"

    return f"{types_str} {get_mask_card_number(numbers_str)}"


if __name__ == "__main__":
    print(mask_account_card("Visa Platinum 7000792289606361"))
    print(mask_account_card("Счет 73654108430135874305"))
