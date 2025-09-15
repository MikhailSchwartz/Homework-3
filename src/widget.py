from src.masks import get_mask_account, get_mask_card_number


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


def get_date(data_and_time: str) -> str:
    """Функция которая принимает строку с датой и временем,
    водвращает строку в формате ДД.ММ.ГГГГ"""

    data_and_time = data_and_time.strip()

    year = data_and_time[0:4]
    month = data_and_time[5:7]
    day = data_and_time[8:10]

    return f"{day}.{month}.{year}"


if __name__ == "__main__":
    print(mask_account_card("Visa Platinum 7000792289606361"))
    print(mask_account_card("счёт 7000792289606361"))
    print(get_date("2024-03-11T02:26:18.671407"))
