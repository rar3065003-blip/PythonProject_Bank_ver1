import json
import os
from json import JSONDecodeError


def dict_transactions(file_json_dict:str) -> list[dict]:
    list_result = []
    file_exist:bool = os.path.exists(file_json_dict)
    if not file_exist: return list_result
    with open(file_json_dict, encoding = "utf8") as f:
        try:
            x = json.load(f)
        except JSONDecodeError:
            return list_result
    if not isinstance(x, list):
        return list_result
    return x
