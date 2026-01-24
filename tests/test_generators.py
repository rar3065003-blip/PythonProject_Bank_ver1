import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.mark.parametrize("start, stop, expected", [(597, 597, '0000 0000 0000 0597'),( 0, 695, '0000 0000 0000 0000'), (659, 0, "0000 0000 0000 0000")],)
def test_card_number_generator(start, stop, expected) -> None:
    """тестирование согласно тестовым данным parametrize:
    заданные значения, пустой старт, пустой 'stop'"""
    assert next(card_number_generator(start, stop)) == expected


def test_filter_by_currency_with_usd_transaction(fix_currency):
    """Тесты на выполненние кода с заполнением и без"""
    result = list(filter_by_currency(fix_currency, "USD")) # успешный
    result_2 = list(filter_by_currency(fix_currency, "")) # не успешный
    assert result[0]['id'] == 939719570
    assert result_2 == []


def test_transaction_description(fix_currency):
    test_1 = list(transaction_descriptions(fix_currency))
    assert test_1[0] == "Перевод организации"
    assert list(transaction_descriptions([])) == []