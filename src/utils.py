import json
import logging
import os
from json import JSONDecodeError

from config import ROOT_DIR
from logs.logger_utils import setup_logging_utils
from src import external_api

logger = setup_logging_utils()


def dict_transactions(file_json_dict: str) -> list[dict]:
    """Принимает json файл и возвращает список транзакций в формате *.py"""
    logging.info("Запуск функции dict_transactions")
    list_result: list = []
    path_filename: str = f"{ROOT_DIR}{file_json_dict}"
    file_exist: bool = os.path.exists(path_filename)
    if not file_exist:
        logger.error("Файл отсутствует")
        return list_result
    with open(path_filename, encoding="utf8") as f:
        try:
            x = json.load(f)
        except JSONDecodeError:
            logger.error("Не корректный формат файла")
            return list_result
    if not isinstance(x, list):
        logger.error("Файл пуст")
        return list_result
    return x


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
