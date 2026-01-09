import pytest

from src.widget import get_date
from src.widget import mask_account_card


def test_mask_account_card(
    account_card_16: str,
    account_card_20: str,
    length_account_card: str,
    correct_mask_amount: str,
    correct_mask_card: str,
) -> None:
    """Тестирование функции номера счета и номера карты на количество символов,
    корректность маски счета"""
    assert mask_account_card(account_card_16) == "1234 56XX XXXX 4567"
    assert mask_account_card(account_card_20) == "Счет XX8912"
    with pytest.raises(ValueError):
        mask_account_card(length_account_card)
        mask_account_card(correct_mask_card)
        mask_account_card(correct_mask_amount)


def test_get_date() -> None:
    """Тестирование формата времени с отработкой ошибок корректности даты"""
    assert get_date("") == "Некорректная дата"
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"
