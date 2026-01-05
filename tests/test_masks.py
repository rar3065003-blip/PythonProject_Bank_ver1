from src.masks import get_mask_card_number, get_mask_account
import pytest


def test_get_mask_card_number_correct_mask(numbers_1: int) -> str:
      pass

def test_get_mask_card_number_correct_length(numbers_1: int) -> str:
      pass

def test_get_mask_card_number_correct_digits(numbers_1: int) -> str:
     pass

def test_get_mask_card_number_no_number(numbers_1: int) -> str:
     pass



def test_get_mask_account_correct_mask(account_1: int) -> str:
      pass

def test_get_mask_account_correct_length(account_1: int) -> str:
      pass

def test_get_mask_account_correct_digits(account_1: int) -> str:
      pass

def test_get_mask_account_no_numbers(account_1: int) -> str:
      pass


# Тестирование правильности маскирования номера карты.
#
# Проверка работы функции на различных входных форматах номеров карт,
# включая граничные случаи и нестандартные длины номеров.
#
# Проверка, что функция корректно обрабатывает входные строки,
# где отсутствует номер карты.