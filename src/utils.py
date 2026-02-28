import re
from typing import Any
from logs.logger_utils import setup_logging_utils
from src import external_api
logger = setup_logging_utils()
import json


def dict_transactions_to_json(file_json_dict: str = "") -> list[dict[Any, Any]]:
    """Для обработки выбран JSON-файл."""
    try:
        data_json = json.load(open(file_json_dict, "r", encoding="utf-8"))
        data = []
        for transaction in data_json:
            amount = transaction.get("operationAmount", {}).get("amount")
            currency_name = transaction.get("operationAmount", {}).get("currency", {}).get("name")
            currency_code = transaction.get("operationAmount", {}).get("currency", {}).get("code")
            data.append({'id': transaction.get("id"),
                         'state': transaction.get("state"),
                         'date': transaction.get("date"),
                         'amount': amount,
                         'currency_name': currency_name,
                         'currency_code': currency_code,
                         'from': transaction.get("from"),
                         'to': transaction.get("to"),
                         'description': transaction.get("description")})
        return data
    except Exception:
        return []



def convertation_currency(transaction: dict) -> float:
    """Принимает транзакцию в виде словаря и возвращает сумму транзакции,
    конвертированную в рубли по курсу на сегодняшний день, либо просто в рублях"""
    logger.info("Запуск функции convertation_currency")
    currency: str = transaction.get("operationAmount", {}).get("currency", {}).get("code", "")
    amount: float = float(transaction.get("operationAmount", {}).get("amount", 0))
    if currency == "RUB":
        logger.info("Совершена операция не требующая конвертации в рубли")
        return amount
    result_return: float = external_api.exchange_rates_data(currency, amount)
    logger.info(f"Совершена операция обмена {currency} в рубли на сумму {amount}")
    return result_return


def filter_by_word(transaction: list[dict], word: str) -> list[dict]:
    """Функция поиска транзакций по слову в словаре"""
    filter_data = [data for data in transaction if re.search(word.lower(), data.get("description", "").lower())]
    return filter_data
