def filter_by_state(processing_list: list, state: str = "EXECUTED") -> list:
    """Функция возвращает новый список словарей, содержащий только те словари, у которых ключ state (по умолчанию
    'EXECUTED') соответствует указанному значению."""

    processing_list_filtred = []

    for processing in processing_list:
        if processing.get("state") == state:
            processing_list_filtred.append(operation)

    return processing_list_filtred
