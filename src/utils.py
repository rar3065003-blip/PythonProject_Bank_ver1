import json
import logging
import os
from json import JSONDecodeError
from logs.logger_utils import setup_logging_utils
from src import external_api

logger = setup_logging_utils()


def dict_transactions(file_json_dict: str) -> list[dict]:
    """Принимает json файл и возвращает список транзакций в формате *.py"""
    logging.info("Запуск функции dict_transactions")
    list_result: list = []

    base_dir = os.path.dirname(os.path.abspath(__file__))
    path_filename: str = os.path.join(base_dir, file_json_dict)
    logging.debug(f"Проверяем существование файла: {path_filename}")

    file_exist: bool = os.path.exists(path_filename)
    if not file_exist:
        logger.error("Файл отсутствует: {path_filename}")
        return list_result

    with open(path_filename, encoding="utf-8") as f:
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
