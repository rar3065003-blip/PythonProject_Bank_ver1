from src.generators import filter_by_currency


def test_filter_by_currency_with_usd_transaction(fix_currency, fix_currency_empty_currency):
    """Тесты на выполненние кода с заполнением и без"""
    result = list(filter_by_currency(fix_currency, "USD")) # успешный
    result_2 = list(filter_by_currency(fix_currency, "")) # не успешный
    assert result[0]['id'] == 939719570
    assert result_2 == []