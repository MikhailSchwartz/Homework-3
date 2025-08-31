from masks import account_number, ddcard_number


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
