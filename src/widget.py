from masks import get_mask_card_number, get_mask_account


def mask_account_card(account_details: str) -> str:
    """Функция принимает тип и номер карты или счета,
    возвращает строку с замаскированным номером"""

    account_details_list = account_details.split()
    type = []
    number = []

    for element in account_details_list:
        if element.isalpha():
            type.append(element)
        if element.isdigit():
            number.append(element)

    if "счет" or "счёт" in type:
        return f"{type} {get_mask_account(str(number))}"

    return f"{' '.join(type)} {get_mask_card_number(str(number))}"