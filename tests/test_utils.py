from json import JSONDecodeError
from unittest.mock import mock_open
from unittest.mock import patch

import pytest
from src.external_api import exchange_rates_data
from src.utils import convertation_currency
from src.utils import dict_transactions_to_json


def test_dict_transactions_to_json() -> None:
    with patch("os.path.exists") as file_exist:
        file_exist.return_value = False
        assert dict_transactions_to_json(' ') == []
        file_exist.return_value = True

def test_right_result() -> None:
    with patch("os.path.exists") as file_exist:
        file_exist.return_value = True
        with patch("builtins.open", mock_open(read_data= '[{"id": 456862849}]')):
            result = dict_transactions_to_json("")
            assert result[0].get('id') == 456862849

def test_wrong_format() -> None:
    with patch("os.path.exists") as file_exist:
        file_exist.return_value = True
        with patch("builtins.open", pytest.raises(JSONDecodeError)):
            dict_transactions_to_json("")
            assert dict_transactions_to_json("") == []




def test_convertation_currency(fix_currency: list[dict]) -> None:
    assert convertation_currency(fix_currency[2]) == 79114.93
    with patch("src.external_api.exchange_rates_data") as mock_data:
        mock_data.return_value = 1.01
        assert convertation_currency(fix_currency[1]) == 1.01


@pytest.mark.parametrize(
    ("currency", "amount", "status_code", "exp_result"), [("rub", 3195.58, 400, 0), ("rub", 3195.58, 200, 3195.58)]
)
def test_exchange_rates_data(currency: str, amount: float, status_code: int, exp_result: float) -> None:
    with patch("requests.get") as mock_data:
        response = mock_data.return_value
        response.status_code = status_code
        response.json.return_value = {"result": exp_result}

        assert exchange_rates_data(currency, amount) == exp_result


def test_exchange_rates_data_2() -> None:
    with patch("requests.get") as mock_data:
        response = mock_data.return_value
        response.status_code = 200
        response.json.side_effect = JSONDecodeError("", "", 0)

        assert exchange_rates_data("currency", 1.0) == 0
