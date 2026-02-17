import csv

import pandas as pd


def csv_module(df: str) -> list[dict]:
    """Функция принимает файл в формате csv
    и возвращает список словарей"""
    result_dict = []
    with open(df, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            result_dict.append(row)
        return result_dict


def excel_module(df: str) -> list[dict]:
    """Функция принимает файл в формате xlsx
    и возвращает список словарей"""
    reader = pd.read_excel(df, engine="openpyxl")
    result_2 = reader.to_dict(orient="records")
    return result_2
