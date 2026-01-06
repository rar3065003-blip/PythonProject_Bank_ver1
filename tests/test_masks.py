from src.masks import get_mask_card_number, get_mask_account
import pytest

@pytest.mark.parametrize("account, expected", [
    (3216547898756423, "3216 54XX XXXX 6423"),
    (32147898756423 , "Введите 16 цифр"),
    (3216545647898756423, "Введите 16 цифр")
    ],)
def test_get_mask_card_number(account, expected) -> None:
      assert get_mask_card_number(account) == expected


@pytest.mark.parametrize("account, expected", [
    (32165498712365478965 , "XX8965"),
    (321654982365478965 , "Введите  номер счета 20 цифр"),
    (3216549823654789654688 , "Введите  номер счета 20 цифр"),
    ])
def test_get_mask_account_mask(account, expected) -> None:
    assert get_mask_account(account) == expected
