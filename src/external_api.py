import os
from json import JSONDecodeError

import requests
from dotenv import load_dotenv
from requests import Response

load_dotenv()
API_KEY = os.getenv("API_KEY")


def exchange_rates_data(currency: str, amount: float) -> float:
    """Функция конвертации валюты по API"""
    url: str = "https://api.apilayer.com/exchangerates_data/convert"
    payload: dict = {"amount": amount, "from": currency, "to": "RUB"}
    headers: dict = {"apikey": API_KEY}
    response: Response = requests.get(url, headers=headers, params=payload)

    status_code: int = response.status_code
    if status_code == 200:
        try:
            result: dict = response.json()
            result_exch = result.get("result", 0)
            return result_exch
        except JSONDecodeError:
            return 0
    return 0
