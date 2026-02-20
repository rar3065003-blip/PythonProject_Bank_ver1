import re

test_data = [
    {'id': '650703', 'state': 'EXECUTED', 'date': '2023-09-05T11:30:32Z',
     'amount': '16210', 'currency_name': 'Sol', 'currency_code': 'PEN',
     'from': 'Счет 58803664561298323391', 'to': 'Счет 39745660563456619397', 'description': 'Перевод организации'},
    {'id': '3598919', 'state': 'EXECUTED', 'date': '2020-12-06T23:00:58Z',
     'amount': '29740', 'currency_name': 'Peso', 'currency_code': 'COP',
     'from': 'Discover 3172601889670065', 'to': 'Discover 0720428384694643', 'description': 'Перевод с карты на карту'},
    {'id': '593027', 'state': 'CANCELED', 'date': '2023-07-22T05:02:01Z',
     'amount': '30368', 'currency_name': 'Shilling', 'currency_code': 'TZS',
     'from': 'Visa 1959232722494097', 'to': 'Visa 6804119550473710', 'description': 'Перевод с карты на карту'}
]

def process_bank_search(data:list[dict], search:str)->list[dict]:
    """ Функция принимает список банковских странзакций и возвращает
    список транзакций отфильтрованных по запросу"""
    search_result = []
    pattern = f'^{re.escape(search)}$'
    for item in data:
        if re.fullmatch(pattern, item['description']):
            search_result.append(item)

    return search_result

# print(process_bank_search(test_data, 'Перевод с карты на карту'))




def process_bank_operations(data:list[dict], categories:list)->dict: # categories это description
    """ Функция принимает список транзакций,
     а возвращает словарь, где отражается вид и количество запрошенных операций"""
    result = {}
    text_dict = ""
    for dict in data:
       for value in dict.values():
           text_dict += str(value).lower()+ " "

    for word in categories:
        escape_word = re.escape(word.lower())
        pattern = r'\b' + escape_word +r'\b'
        matches = re.findall(pattern, text_dict)
        count = len(matches)
        result[word] = count
    return result


print(process_bank_operations(test_data, ['Перевод организации', 'Перевод с карты на карту' ]))
