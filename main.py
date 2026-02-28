import os
from collections.abc import Callable
from src.csv_excel_module import csv_module, excel_module
from src.processing import filter_by_state, sort_by_date
from src.utils import dict_transactions_to_json, filter_by_word
from src.generators import filter_by_currency
from src.widget import mask_account_card, get_date

BASE_DIR = os.path.dirname(__file__)
print(BASE_DIR)
dict_file = {1: dict_transactions_to_json, 2: csv_module, 3: excel_module}
path_file = {1: BASE_DIR + "/data/operations.json",
             2: BASE_DIR + "/data/transactions.csv",
             3: BASE_DIR + "/data/transactions_excel.xlsx"}
status = ["EXECUTED", "CANCELED", "PENDING"]

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

    while True:
        print("Введите статус, по которому необходимо выполнить фильтрацию. \n"
              f"Доступные для фильтровки статусы: {','.join(status)}")
        status_user_input:str = input().upper()
        if status_user_input in status:
            transaction = filter_by_state(transaction, status_user_input)
            print(f"Операции отфильтрованы по статусу {status_user_input}")
            break
        else:
            print(f"Статус операции '{status_user_input}' недоступен.")


    print("Отсортировать по дате? Да/Нет")
    user_input: bool = (input()).lower() == "да"
    if user_input:
        print("По возрастанию или по убыванию?")
        sort_reverse_user_input: bool = (input()).lower() == "по убыванию"
        transaction =  sort_by_date(transaction, sort_reverse_user_input)

    print("Выводить только рублевые транзакции? Да/Нет")
    user_input: bool = (input()).lower() == "да"
    if user_input:
        transaction = list(filter_by_currency(transaction, "RUB"))

    print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
    user_input: bool = (input()).lower() == "да"
    if user_input:
        print("Введите слово:")
        word_user_input: str = input()
        transaction = filter_by_word(transaction, word_user_input)

    print("Распечатываю итоговый список транзакций...")
    print(f"Всего банковских операций в выборке: {len(transaction)}")

    for trans in transaction:
        state = trans.get("state")
        date = get_date(trans.get("date"))
        amount = trans.get("amount")
        currency_name = trans.get("currency_name")
        currency_code = trans.get("currency_code")
        to_from = trans.get("from")
        to = mask_account_card(trans.get("to"))
        description = trans.get("description")

        print_out = f"{date} {description}"
        check_to = f"{to}"
        check_from = " -> " + mask_account_card(to_from) if to_from else ""
        print_sum = f"Сумма: {amount} {currency_code}"
        print(f"{print_out}\n{check_to}\n{check_from}\n{print_sum}")



if __name__ == '__main__':
    main()