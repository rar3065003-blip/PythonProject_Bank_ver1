import json
import os
from json import JSONDecodeError

from config import ROOT_DIR
from src import external_api


def dict_transactions(file_json_dict: str) -> list[dict]:
    """Принимает json файл и возвращает список транзакций в формате *.py"""
    list_result: list = []
    path_filename: str = f"{ROOT_DIR}{file_json_dict}"
    file_exist: bool = os.path.exists(path_filename)
    if not file_exist:
        return list_result
    with open(path_filename, encoding="utf8") as f:
        try:
            x = json.load(f)
        except JSONDecodeError:
            return list_result
    if not isinstance(x, list):
        return list_result
    return x


def convertation_currency(transaction: dict) -> float:
    """Принимает транзакцию в виде словаря и возвращает сумму транзакции,
    конвертированную в рубли по курсу на сегодняшний день, либо просто в рублях"""
    currency: str = transaction.get("operationAmount", {}).get("currency", {}).get("code", "")
    amount: float = float(transaction.get("operationAmount", {}).get("amount", 0))
    if currency == "RUB":
        return amount
    result_return: float = external_api.exchange_rates_data(currency, amount)
    return result_return
