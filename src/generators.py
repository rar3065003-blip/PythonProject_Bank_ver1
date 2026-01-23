from typing import Any, Generator, Iterator


def filter_by_currency(transactions, code) -> Iterator:
    return (transaction for transaction in transactions if transaction.get("operationAmount", {})
        .get("currency", {})
        .get("code") == code)


def transaction_descriptions(transactions: list) -> Iterator:
    while True:
        for transaction in transactions:
            transaction.get("description")
            yield transaction


def card_number_generator(start, stop) -> Generator:
    for i in range(start, stop + 1):
        result = f'{i:016d}'
        result_1 = " ".join(result[a: a + 4] for a in range(0, len(result), 4))
        yield result_1
