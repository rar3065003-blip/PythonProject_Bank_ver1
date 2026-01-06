from src.processing import sort_by_date, filter_by_state


def test_filter_by_state(transaction_1: list, transaction_executed: list, transaction_canceled: list) -> None:
    """Тестирование на условия фильтрации по статусу state и пустому списку транзакций"""
    assert filter_by_state(transaction_1, state="EXECUTED") == transaction_executed
    assert filter_by_state(transaction_1, state="CANCELED") == transaction_canceled
    assert filter_by_state(transaction_1, state="a") == []


def test_sort_by_date(transaction: list, result_reverse_true: list, result_reverse_false: list) -> None:
    """Тестирование на условие сортировки по дате reverse"""
    assert sort_by_date(transaction) == result_reverse_true
    assert sort_by_date(transaction, reverse=False) == result_reverse_false
