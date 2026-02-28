from unittest.mock import mock_open
from unittest.mock import patch

import pytest

from src.csv_excel_module import csv_module


def test_csv_transactions() -> None:
    csv_data = """id;state;date 
    650703;EXECUTED;2023-09-05T11:30:32Z"""
    with patch("builtins.open", mock_open(read_data=csv_data)):
        result = csv_module("wrong_path.csv")
    assert len(result) == 1
    assert result[0] == {"date ": "2023-09-05T11:30:32Z", "id": "    650703", "state": "EXECUTED"}
    # assert result[1] == {
    #     "id;state;date;amount;currency_name;": "650703;EXECUTED;2023-09-05T11:30:32Z;" "16210;Sol;PEN;"
    # }


def test_empty_csv_transactions_file() -> None:
    with patch("builtins.open", mock_open(read_data="")):
        result = csv_module("empty.csv")
    assert result == []


def test_csv_module_file_not_found() -> None:
    with patch("builtins.open", side_effect=FileNotFoundError):
        with pytest.raises(FileNotFoundError):
            csv_module("Error_file.csv")
