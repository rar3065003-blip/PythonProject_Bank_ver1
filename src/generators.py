from typing import Any, Generator
import random


def filter_by_currency(transactions, code) :
    for transaction in transactions:
        currency_code = (
        transaction.get("operationAmount", {})
        .get("currency", {})
        .get("code"))
        if currency_code == code:
            yield transaction


usd_transactions = filter_by_currency(transactions, "USD")
for _ in range(2):
    print(next(usd_transactions))


def transaction_descriptions(transactions: list) -> Generator[None, Any, Any]:
    while True:
        for transaction in transactions:
            transaction.get("description")
            yield transaction


def card_number_generator(start, stop):
    while True:
        temp = str(f'{random.randint(0000000000000000, 9999999999999999 ):016d}')
        result = " ".join(temp[i: i + 4] for i in range(0, len(temp), 4))
        for i in range(start, stop):
            result += i
        yield result
# задать диапазон номеров видимо по последней цифре
