import json
import logging

logger = logging.getLogger("utils")
file_handler = logging.FileHandler("../logs/logs.log", mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)


def transactions_load(path: str) -> list:
    """Загружает данные о финансовых транзакциях из JSON-файла.
    Если файл не найден, пустой или не содержит список — возвращает пустой список."""
    logger.info(f"Загрузка файла транзакций {path}")
    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)

        if isinstance(data, list) and len(data) > 0:
            logger.info(f"Загружено {len(data)} транзакций из {path}")
            return data
        else:
            logger.warning(f"Файл {path} пуст или не содержит список данных")
            return []
    except json.JSONDecodeError:
        logger.error(f"Ошибка декодирования JSON в файле {path}")
        return []
    except FileNotFoundError:
        logger.error(f"Файл не найден: {path}")
        return []


# if __name__ == "__main__":
#     print(transactions_load("../data/jsonempty.json"))
