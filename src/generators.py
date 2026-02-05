from typing import Generator
from typing import Iterator


def filter_by_currency(transactions: list, code: str) -> Iterator:
    """Принимает список словарей транзакций возвращает список отфильтрованный по коду валюты"""
    return (
        transaction
        for transaction in transactions
        if transaction.get("operationAmount", {}).get("currency", {}).get("code") == code
    )


def transaction_descriptions(transactions: list) -> Iterator:
    """Принимает список словарей транзакций возвращает действие со счетом"""
    for transaction in transactions:
        yield transaction.get("description")


def card_number_generator(start: int, stop: int) -> Generator:
    """Генерирует номер банковской карты в заданном диапазоне"""
    if start > stop:
        start, stop = stop, start
    for i in range(start, stop + 1):
        result = f"{i:016d}"
        result_1 = " ".join(result[a : a + 4] for a in range(0, len(result), 4))
        yield result_1
