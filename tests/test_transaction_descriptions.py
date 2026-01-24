from src.generators import transaction_descriptions

def test_transaction_description(fix_currency, fix_currency_empty_transaction):
    test_1 = list(transaction_descriptions(fix_currency))
    test_2 = list(transaction_descriptions(fix_currency_empty_transaction))
    assert test_1[0] == "Перевод организации"
    assert test_2[0] == ""