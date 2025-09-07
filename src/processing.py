def filter_by_state(bank_processing_list: list, state: str = "EXECUTED") -> list:
    """Функция принимает список словарей с банковскими операциями и возвращает новый список словарей,
    содержащий только те словари, у которых ключ state (по умолчанию 'EXECUTED') соответствует указанному значению."""

    bank_processing_list_filtred = []

    for processing in bank_processing_list:
        if processing.get("state") == state:
            bank_processing_list_filtred.append(processing)

    return bank_processing_list_filtred


def sort_by_date(bank_processing_list: list, order: bool = True) -> list:
    """Функция sort_by_date, которая принимает список словарей и необязательный параметр, задающий порядок сортировки
    (по умолчанию — убывание). Функция должна возвращать новый список, отсортированный по дате (date)."""

    bank_processing_list_sorted = sorted(bank_processing_list, key=lambda operation: operation["date"], reverse=order)

    return bank_processing_list_sorted


if __name__ == "__main__":
    bank = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
    print(sort_by_date(bank))
