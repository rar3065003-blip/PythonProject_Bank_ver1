import pytest

from processing import sort_by_date


def test_filter_by_state(user_calculate: list, state: str = "EXECUTED") -> list:
    pass

def test_sort_by_date(transaction, result_reverse_true, result_reverse_false) -> None:
    assert sort_by_date(transaction) == result_reverse_true
    assert sort_by_date(transaction, reverse = False) == result_reverse_false