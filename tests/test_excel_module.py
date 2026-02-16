from unittest.mock import patch
import pandas as pd
from src.csv_excel_module import excel_module


def test_excel_module() -> None:
    data = pd.DataFrame(
        [
            {"id": 1, "state": "EXECUTED", "date": "2024-01-15T10:30:00", "amount": 1000},
            {"id": 2, "state": "CANCELED", "date": "2024-01-15T10:30:00", "amount": 2000},
            {"id": 3, "state": "EXECUTED", "date": "2024-01-15T10:30:00", "amount": 3000},
        ]
    )
    with patch("pandas.read_excel", return_value=data):
        result = excel_module("wrong.xlsx")

    assert len(result) == 3
    assert result[0] == {"id": 1, "state": "EXECUTED", "date": "2024-01-15T10:30:00", "amount": 1000}
    assert result[1] == {"id": 2, "state": "CANCELED", "date": "2024-01-15T10:30:00", "amount": 2000}
    assert result[2] == {"id": 3, "state": "EXECUTED", "date": "2024-01-15T10:30:00", "amount": 3000}
