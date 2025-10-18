import logging

logger = logging.getLogger("masks")
file_handler = logging.FileHandler("../logs/example.log", mode="w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)


def get_mask_card_number(card_number: str | int) -> str:
    """Функция принимает на вход номер карты в формате "73654108430135874305"
    и возвращает ее маску XXXX XX** **** XXXX где X цифра"""
    logger.info(f"Обработка номера карты: {card_number}")
    card_str = str(card_number).replace(" ", "")

    if len(card_str) != 16 or not card_str.isdigit():
        logger.error("Ошибка: некорректный номер карты")
        raise ValueError("Номер карты должен содержать 16 цифр")

    mask_card = f"{card_str[:4]} {card_str[4:6]}** **** {card_str[12:]}"
    logger.info(f"Результат маскирования: {mask_card}")
    return mask_card


def get_mask_account(account_number: str | int) -> str:
    """Функция принимает на вход номер в формате "73654108430135874305" счета
    и возвращает его маску в формате **XXXX, где X это цифра"""
    logger.info(f"Получен номер счёта для маскировки: {account_number}")
    account_str = str(account_number).replace(" ", "")

    if not account_str.isdigit():
        logger.error("Ошибка: номер счёта должен содержать только цифры")
        raise ValueError("Номер счёта должен содержать только цифры")

    if len(account_str) < 4:
        logger.error("Ошибка: слишком короткий номер счёта")
        raise ValueError("Номер счёта должен содержать минимум 4 цифры")

    result = f"**{account_str[-4:]}"
    logger.info(f"Маскированный номер счёта: {result}")
    return result


# if __name__ == "__main__":
#     print(get_mask_card_number(7000792289606361))
#     print(get_mask_account(736541084301358743059988))
