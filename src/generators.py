from typing import Generator, Iterator


def filter_by_currency(transactions, code) -> Iterator:
    """ Принимает список словарей транзакций возвращает список отфильтрованный по коду валюты"""
    return (transaction for transaction in transactions if transaction.get("operationAmount", {})
        .get("currency", {})
        .get("code") == code)


def transaction_descriptions(transactions: list):
    """ Принимает список словарей транзакций возвращает действие со счетом"""
    if not transactions:
        return
    for transaction in transactions:
         yield transaction.get('description')


def card_number_generator(start, stop) -> Generator:
    """Генерирует номер банковской карты в заданном диапазоне"""
    for i in range(start, stop + 1):
        result = f'{i:016d}'
        result_1 = " ".join(result[a: a + 4] for a in range(0, len(result), 4))
        yield result_1
