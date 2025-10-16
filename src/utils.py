import json


def transactions_load(path: str) -> list:
    """Загружает данные о финансовых транзакциях из JSON-файла.
    Если файл не найден, пустой или не содержит список — возвращает пустой список."""

    try:
        with open(path, encoding='utf-8') as f:
            data = json.load(f)
        if isinstance(data, list) and len(data) > 0:
            return data
        else:
            return []
    except json.JSONDecodeError:
        return []
    except FileNotFoundError:
        return []


# if __name__ == "__main__":
#     print(transactions_load("../data/operations.json"))
