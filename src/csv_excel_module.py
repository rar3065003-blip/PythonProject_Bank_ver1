from typing import Any

import pandas as pd
import csv
import openpyxl

# Функция должна возвращать данные в виде структуры данных,
# например, списка словарей, а не выводить их в консоль.
# Такая структура позволит тебе легко работать с данными в дальнейшем.
# Возвращать данные в виде файла не требуется,
# так как целью является обработка и анализ информации,
# а не её повторная запись в файл.

def csv_module(df)-> list[dict]:
    """Функция принимает файл в формате csv
    и возвращает список словарей"""
    result_dict = []
    with open(df, newline='', encoding = 'utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            result_dict.append(row)
        return result_dict

result = csv_module('../data/transactions.csv')
print(result)
print(type(result))

def excel_module(df)-> list[dict]:
    """Функция принимает файл в формате xlsx
    и возвращает список словарей"""
    reader = pd.read_excel(df, engine="openpyxl")
    result_2 = reader.to_dict(orient='records')
    return result_2

result = excel_module('../data/transactions_excel.xlsx')
print(result)
print(type(result))

