import csv
import pandas as pd
from pandas import DataFrame


def csv_module(df: str) -> list[dict]:
    """Для обработки выбран CSV-файл."""
    result_dict = []
    with open(df, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            result_dict.append(row)
        return result_dict



def excel_module(df: str| None = None) -> list[dict]:
    """Для обработки выбран xlsx-файл"""
    if df:
        reader: DataFrame = pd.read_excel(df, engine="openpyxl")
        reader.notnull()
        result_2= reader.to_dict(orient="records")
        return result_2
    else:
        raise ValueError("Файл не указан")

