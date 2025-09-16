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

    if not numbers or not types:
        raise ValueError("Неполные данные о карте или счёте.")

    numbers_str = "".join(numbers)
    types_str = " ".join(types)

    if "счет" in types_str.lower() or "счёт" in types_str.lower():
        return f"{types_str} {get_mask_account(numbers_str)}"

    return f"{types_str} {get_mask_card_number(numbers_str)}"


def get_date(data_and_time: str) -> str:
    """Функция которая принимает строку с датой и временем,
    водвращает строку в формате ДД.ММ.ГГГГ"""

    data_and_time = data_and_time.strip()

    if 'T' not in data_and_time:
        raise ValueError("Строка не содержит даты в формате ISO 8601.")

    position_t = data_and_time.index("T")

    data_info = data_and_time[:position_t]

    if len(data_info) != 10:
        raise ValueError("Некорректный формат даты.")

    year = data_info[0:4]
    month = data_info[5:7]
    day = data_info[8:10]

    if 1000 < int(year) < 3000 and 1 <= int(month) <= 12 and 1 <= int(day) <= 31:
        return f"{day}.{month}.{year}"
    raise ValueError("Некорректная дата")

if __name__ == "__main__":
    print(mask_account_card("Visa Platinum 7000 7922 8960 6000"))
    print(mask_account_card("счёт 44444"))
    print(get_date("2024-12-31T02:26:18.671407"))
