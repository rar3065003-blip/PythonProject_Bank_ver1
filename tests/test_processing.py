from src.processing import sort_by_date, filter_by_state

def test_filter_by_state(transaction_1, transaction_executed, transaction_canceled) -> None:
    assert filter_by_state(transaction_1, state = "EXECUTED") == transaction_executed
    assert filter_by_state(transaction_1, state = "CANCELED") == transaction_canceled
    assert filter_by_state(transaction_1, state = "a") == []


def test_sort_by_date(transaction, result_reverse_true, result_reverse_false) -> None:
    assert sort_by_date(transaction) == result_reverse_true
    assert sort_by_date(transaction, reverse = False) == result_reverse_false