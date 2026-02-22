from src.csv_excel_module import csv_module, excel_module
from src.generators import filter_by_currency
from src.process_bank import process_bank_search
from src.processing import filter_by_state, sort_by_date
from src.utils import convertation_currency
from src.utils import dict_transactions
from src.widget import get_date
from src.widget import mask_account_card

def run_project():
    global result_ance
    while True:
        print("Привет!\nДобро пожаловать в программу работы с банковскими транзакциями.")
        user_input = (input("Выберите необходимый пункт меню: "
                         "1. Получить информацию о транзакциях из JSON-файла\n"
                         "2. Получить информацию о транзакциях из CSV-файла\n"
                         "3. Получить информацию о транзакциях из XLSX-файла\n"
                            "Ваш выбор:"))
        if user_input == "1":
            print("Для обработки выбран JSON-файл")
            result = dict_transactions("../data/operations.json")
            break
        if user_input == "2":
            print("Для обработки выбран CSV - файл")
            result = csv_module("data/transactions.csv")
            break
        if user_input == "3":
            print("Для обработки выбран XLSX - файл")
            result = excel_module("data/transactions_excel.xlsx")
            break
        else:
            print("Повторите ввод пункта меню")

    while True:
        valid_statuses = ["EXECUTED", "CANCELED", "PENDING"]
        status_input = input("Введите статус, по которому необходимо выполнить фильтрацию.\n"
              "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n"
                             "Ваш выбор:")
        status_upper = status_input.upper()
        if status_upper in valid_statuses:
            filtered_result = filter_by_state(result, status_upper)
            break
        else:
            print(f"Статус операции '{status_input}' недоступен.")
            continue

    while True:
        user_ance = input("Отсортировать операции по дате? Да/Нет :")
        if user_ance.lower() == "да":
            while True:
                sort_qest = input("Отсортировать по возрастанию или по убыванию? :").lower()
                if sort_qest == "по возрастанию":
                    result_ance = sort_by_date(filtered_result, reverse=False)
                    break
                if sort_qest == "по убыванию":
                    result_ance = sort_by_date(filtered_result, reverse=True)
                    break
                else:
                    print("Неверный вариант сортировки. Введите 'по возрастанию' или 'по убыванию'.")

            break

        elif user_ance.lower() == "нет":
            result_ance = filtered_result
            break
        else:
            print("Не верная команда сортировки. Введите 'Да' или 'Нет'.")

    while True:
        ance_user_transaction = input("Выводить только рублевые транзакции? Да/Нет")
        if ance_user_transaction.lower() == "да":
            result_user_transaction = list(filter_by_currency(result_ance, "RUB" ))
            break
        if ance_user_transaction.lower() == "нет":
            result_user_transaction = result_ance
            break
        else:
            print("Валюта транзакции не выбрана")
            continue

    while True:
        user_filter_words = input("Отфильтровать список транзакций\n по определенному слову в описании? Да/Нет")
        if user_filter_words.lower() == "да":
            result_final = []
            user_request = input("Введите слово для поиска в описании: ")
            result_user_filter_words = process_bank_search(result_user_transaction , user_request )
            result_final = result_user_filter_words
            break
        elif user_filter_words.lower() == "нет":
            result_final = []
            result_final = result_user_transaction
            break

    fin_result = len(result_final)
    if fin_result == 0:
                print("Не найдено ни одной транзакции,\n подходящей под ваши условия фильтрации")
    else:
        print("Распечатываю итоговый список транзакций...")
        print(f"Всего банковских операций в выборке:{fin_result}\n")

        for i, transaction in enumerate(result_final, start=1):
            # 1. Обработка даты
            date_str = transaction.get('date', '')
            formatted_date = get_date(date_str) if date_str else "Дата неизвестна"

            # 2. Обработка описания
            description = transaction.get('description', 'Операция без описания')

            # 3. Маскировка полей from и to
            from_account = transaction.get('from', '')
            to_account = transaction.get('to', '')

            masked_from = mask_account_card(from_account) if from_account else ""
            masked_to = mask_account_card(to_account) if to_account else ""

            # 4. Обработка суммы и валюты
            operation_amount = transaction.get("operationAmount", {})
            if operation_amount:
                amount = operation_amount.get("amount", "0")
                currency_info = operation_amount.get("currency", {})
                currency = currency_info.get("name", "N/A")
            else:
                amount = "0"
                currency = "N/A"
            amount_str = f"{amount} {currency}"

            # 5. Форматированный вывод одной транзакции
            print(f"{formatted_date} {description}")
            if masked_from:
                print(f"{masked_from}")
            if masked_to:
                print(f"-> {masked_to}")
            print(f"Сумма: {amount_str}\n")  # перенос строки между транзакциями


if __name__ == "__main__":
    # result_1 = mask_account_card("Maestro 1596837868705199")
    # result_2 = mask_account_card("Счет 73654108430135874305")
    # result_3 = get_date("2024-03-11T02:26:18.671407")
    # print(result_1)
    # print(result_2)
    # print(result_3)
    #
    # results: list[dict] = dict_transactions("../data/operations.json")
    # for i in results:
    #     result_data: float = convertation_currency(i)
    #     print(result_data)
    #     break

    run_project()