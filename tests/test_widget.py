import pytest

from src.widget import mask_account_card, get_date


def test_mask_account_card(account_card_16, account_card_20, length_account_card,
                           correct_mask_amount, correct_mask_card,) -> None:
    assert mask_account_card(account_card_16) == '1234 56XX XXXX 4567'
    assert mask_account_card(account_card_20) == 'Счет XX8912'
    with pytest.raises(ValueError):
        mask_account_card(length_account_card)
        mask_account_card(correct_mask_card)
        mask_account_card(correct_mask_amount)

def test_get_date() -> None:
    assert get_date('') == "Некорректная дата"
    assert get_date('2024-03-11T02:26:18.671407') == '11.03.2024'
