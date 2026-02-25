import os
from collections.abc import Callable

from src.csv_excel_module import csv_module, excel_module
from src.utils import dict_transactions_to_json


BASE_DIR = os.path.dirname(__file__)
print(BASE_DIR)
dict_file = {1: dict_transactions_to_json, 2: csv_module, 3: excel_module}
path_file = {1: BASE_DIR + "/data/operations.json",
             2: BASE_DIR + "/data/transactions.csv",
             3: BASE_DIR + "/data/transactions_excel.xlsx"}
def main():
    transaction = []

    while True:
        print("Выберите необходимый пункт меню:\n"
            "1. Получить информацию о транзакциях из JSON-файла\n"
            "2. Получить информацию о транзакциях из CSV-файла\n"
            "3. Получить информацию о транзакциях из XLSX-файла:")

        user_input :int = int(input())
        get_func: Callable| None = dict_file.get(user_input)

        if get_func:
            print(get_func.__doc__)
            path:str = path_file.get(user_input)
            transaction = get_func(path)
            break

    print(transaction)


if __name__ == '__main__':
    main()