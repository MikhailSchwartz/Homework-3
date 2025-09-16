def filter_by_state(banking_oprtations: list, state: str = "EXECUTED") -> list:
    """Функция принимает список словарей с банковскими операциями и возвращает новый список словарей,
    содержащий только те словари, у которых ключ state (по умолчанию 'EXECUTED') соответствует указанному значению."""

    filtered_banking_operanions = []

    for operation in banking_oprtations:
        if operation.get("state") == state:
            filtered_banking_operanions.append(operation)

    if len(filtered_banking_operanions) == 0:
        return f"Операции со статусом {state} отсутствуют"

    return filtered_banking_operanions


def sort_by_date(banking_operations: list, order: bool = True) -> list:
    """Функция sort_by_date, которая принимает список словарей и необязательный параметр, задающий порядок сортировки
    (по умолчанию — убывание). Функция должна возвращать новый список, отсортированный по дате (date)."""

    sorted_banking_operations = sorted(banking_operations, key=lambda operation: operation["date"], reverse=order)

    return sorted_banking_operations


if __name__ == "__main__":
    bank = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
    print(sort_by_date(bank))
