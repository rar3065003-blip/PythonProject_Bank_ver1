import pytest

from src.generators import transaction_descriptions


def test_transaction_descriptions(fix_currency):
    transaction = [fix_currency]
    result = list(transaction_descriptions(transaction))
    assert len(result) == 1
    assert result[0]['description'] == "Перевод организации"

def test_empty_transaction_description(fix_currency):
    result = list(transaction_descriptions([]))
    assert len(result) == 0
