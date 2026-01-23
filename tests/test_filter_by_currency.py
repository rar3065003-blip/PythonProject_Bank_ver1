import pytest

from src.generators import filter_by_currency


def test_filter_by_currency_with_usd_transaction(fix_currency):
    transactions = [fix_currency]
    result = list(filter_by_currency(transactions, "USD"))
    assert len(result) == 1
    assert result[0]["operationAmount"]["currency"]["code"] == "USD"

def test_filter_by_currency_empty_result_for_wrong_code(fix_currency):
    transactions = [fix_currency]
    result = list(filter_by_currency(transactions, "RUB"))
    assert len(result) == 0

def test_filter_by_transaction_w_o_currency(fix_currency):
    transactions = [fix_currency]
    result = list(filter_by_currency(transactions, ""))
    assert len(result) == 0

def test_filter_by_currency_handles_empty_list():
    result = list(filter_by_currency([], "USD"))
    assert len(result) == 0