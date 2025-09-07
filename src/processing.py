def filter_by_state(bank_processing_list: list, state: str = "EXECUTED") -> list:
    """Функция принимает список словарей с банковскими операциями и возвращает новый список словарей,
    содержащий только те словари, у которых ключ state (по умолчанию 'EXECUTED') соответствует указанному значению."""

    bank_processing_list_filtred = []

    for processing in bank_processing_list:
        if processing.get("state") == state:
            bank_processing_list_filtred.append(processing)

    return bank_processing_list_filtred
