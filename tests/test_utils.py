from unittest.mock import patch

import pytest

from src.external_api import exchange_rates_data
from src.utils import convertation_currency
from src.utils import dict_transactions


def test_dict_transactions()-> None:
    assert dict_transactions("../data/operation.json") == [] #
    data: list[dict] = dict_transactions("../data/operations.json")
    assert data[0]["id"] == 441945886
    assert dict_transactions("../tests/empty.json") == []
    assert dict_transactions("../tests/dict.json") == []

def test_convertation_currency(transaction_example:list[dict])-> None:
    assert convertation_currency(transaction_example[0]) == 31957.58
    with patch("src.external_api.exchange_rates_data") as mock_data:
        mock_data.return_value = 1.01
        assert convertation_currency(transaction_example[1]) == 1.01

@pytest.mark.parametrize(("currency", "amount", "status_code", "exp_result"),[
    ('rub', 3195.58, 400, 0 ),
    ('rub', 3195.58, 200, 3195.58 )  # почему не работает ? amount не чувствителен result

] )
def test_exchange_rates_data(currency, amount, status_code, exp_result)-> None:
    with patch("requests.get") as mock_data:
        response = mock_data.return_value   
        response.status_code = status_code
        response.json.return_value = {"result": exp_result}

        assert exchange_rates_data(currency, amount) == exp_result
