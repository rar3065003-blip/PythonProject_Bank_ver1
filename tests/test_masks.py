from src.masks import get_mask_card_number, get_mask_account
import pytest


def test_get_mask_card_number_correct_mask(numbers_1: int) -> None:
      pass

def test_get_mask_card_number_correct_length(numbers_1: int) -> None:
      pass

def test_get_mask_card_number_correct_digits(numbers_1: int) -> None:
     pass

def test_get_mask_card_number_no_number(numbers_1: int) -> str:
     pass


@pytest.mark.parametrize("account, expected", [
    (32165498712365478965 , "XX8965"),
    (321654982365478965 , "Введите  номер счета 20 цифр")
])
def test_get_mask_account_mask(account, expected) -> None:
    assert get_mask_account(account) == expected





# Тестирование правильности маскирования номера карты.
#
# Проверка работы функции на различных входных форматах номеров карт,
# включая граничные случаи и нестандартные длины номеров.
#
# Проверка, что функция корректно обрабатывает входные строки,
# где отсутствует номер карты.