def filter_by_currency(transactions: list, currency: str) -> None:
    """Функция, которая принимает на вход список словарей, представляющих транзакции, должна возвращать итератор,
    который поочередно выдает транзакции, где валюта операции соответствует заданной (например, USD)."""

    try:
        if transactions != []:
            for transaction in transactions:
                operation_amount = transaction.get("operationAmount")
                if operation_amount is None:
                    continue

                currency_info = operation_amount.get("currency")
                if currency_info is None:
                    continue

                currency_code = currency_info.get("code")
                if currency_code == currency:
                    yield transaction
        else:
            yield "Список пуст"
    except TypeError:
        yield "Введенный тип данных не соответствует словарю, либо переданы не все аргумнты"

def transaction_descriptions(transactions: list) -> None:
    """Функция которая принимает список словарей с транзакциями и возвращает описание каждой операции по очереди."""

    try:
        if transactions != []:
            for transaction in transactions:
                if "description" in transaction:
                    yield transaction["description"]
                else:
                    yield "Информации об операциях нет"
        else:
            yield "Список транзакций пуст"
    except TypeError:
        yield "Введенный тип данных не соответствует словарю"


def card_number_generator(start: int, stop: int) -> str:
    """Функция генератор, которыя выдает номера банковских карт в формате XXXX XXXX XXXX XXXX,
    где X цифра номера карты. Генератор может сгенерировать номера карт в заданном диапазоне от
     0000 0000 0000 0001 до 9999 9999 9999 9999."""

    if start < 1:
        raise ValueError("Начальное значение не может быть меньше 1")
    if stop > 9999999999999999:
        raise ValueError("Конечное значение не может быть больше 9999999999999999")
    if start > stop:
        raise ValueError("Значение stop значение не может быть меньше значения start")

    for num in range(start, stop + 1):
        rest_of_number = 16 - len(str(num))
        zeros = "0" * rest_of_number
        number = zeros + str(num)
        received_card_number = f"{number[0:4]} {number[4:8]} {number[8:12]} {number[12:16]}"
        yield received_card_number


if __name__ == "__main__":
    finish_number1 = card_number_generator(4, 5)
    try:
        for _ in range(6):
            print(next(finish_number1))
    except StopIteration:
        print("Без вариантов")


if __name__ == "__main__":
    transactions1 = (
        [
            {
                "id": 939719570,
                "state": "EXECUTED",
                "date": "2018-06-30T02:08:58.425572",
                "operationAmount": {

                },
                "description": "Перевод организации",
                "from": "Счет 75106830613657916952",
                "to": "Счет 11776614605963066702"
            },
            {
                "id": 142264268,
                "state": "EXECUTED",
                "date": "2019-04-04T23:20:05.206878",
                "operationAmount": {
                    "amount": "79114.93",
                    "currency": {
                        "name": "USD",
                        "code": "USD"
                    }
                },
                "description": "Перевод со счета на счет",
                "from": "Счет 19708645243227258542",
                "to": "Счет 75651667383060284188"
            },
            {
                "id": 873106923,
                "state": "EXECUTED",
                "date": "2019-03-23T01:09:46.296404",
                "operationAmount": {
                    "amount": "43318.34",
                    "currency": {
                        "name": "руб.",
                        "code": "RUB"
                    }
                },
                "description": "Перевод со счета на счет",
                "from": "Счет 44812258784861134719",
                "to": "Счет 74489636417521191160"
            },
            {
                "id": 895315941,
                "state": "EXECUTED",
                "date": "2018-08-19T04:27:37.904916",
                "operationAmount": {
                    "amount": "56883.54",
                    "currency": {
                        "name": "USD",
                        "code": "USD"
                    }
                },
                "description": "Перевод с карты на карту",
                "from": "Visa Classic 6831982476737658",
                "to": "Visa Platinum 8990922113665229"
            },
            {
                "id": 594226727,
                "state": "CANCELED",
                "date": "2018-09-12T21:27:25.241689",
                "operationAmount": {
                    "amount": "67314.70",
                    "currency": {
                        "name": "руб.",
                        "code": "RUB"
                    }
                },
                "description": "Перевод организации",
                "from": "Visa Platinum 1246377376343588",
                "to": "Счет 14211924144426031657"
            }
        ]
    )

    transactions2 = (1, 2, 3, 4, 5)

    usd_transactions = filter_by_currency(transactions1, "USD")
    try:
        for _ in range(6):
            print(next(usd_transactions))
    except StopIteration:
        print("Словари закончились")
