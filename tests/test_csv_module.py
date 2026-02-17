from unittest.mock import mock_open
from unittest.mock import patch
import pytest
from src.csv_excel_module import csv_module


def test_csv_transactions() -> None:
    csv_data = """id;state;date;amount;currency_name;
    currency_code;from;to;description
650703;EXECUTED;2023-09-05T11:30:32Z;16210;Sol;PEN;
Счет 58803664561298323391;Счет 39745660563456619397;
Перевод организации
3598919;EXECUTED;2020-12-06T23:00:58Z;29740;Peso;COP;
Discover 3172601889670065;Discover 0720428384694643;
Перевод с карты на карту
593027;CANCELED;2023-07-22T05:02:01Z;30368;Shilling;
TZS;Visa 1959232722494097;Visa 6804119550473710;
Перевод с карты на карту
"""
    with patch("builtins.open", mock_open(read_data=csv_data)):
        result = csv_module("wrong_path.csv")
    assert len(result) == 10
    assert result[0] == {"id;state;date;amount;currency_name;": "    currency_code;from;to;description"}
    assert result[1] == {
        "id;state;date;amount;currency_name;": "650703;EXECUTED;2023-09-05T11:30:32Z;" "16210;Sol;PEN;"
    }


def test_empty_csv_transactions_file() -> None:
    with patch("builtins.open", mock_open(read_data="")):
        result = csv_module("empty.csv")
    assert result == []


def test_csv_module_file_not_found() -> None:
    with patch("builtins.open", side_effect=FileNotFoundError):
        with pytest.raises(FileNotFoundError):
            csv_module("Error_file.csv")
