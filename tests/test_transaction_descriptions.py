import pytest
from src.generators import transaction_descriptions

def test_transaction_description(fix_currency, fix_currency_empty_transaction):
    test_1 = list(transaction_descriptions(fix_currency))
    assert test_1[0] == "Перевод организации"
    with pytest.raises(ValueError) as excinfo:
        list(transaction_descriptions(fix_currency_empty_transaction))
    assert "Не корректный список транзакций" in str(excinfo.value)
