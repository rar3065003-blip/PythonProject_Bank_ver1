import re
from collections import Counter


def process_bank_search(data:list[dict], search:str)->list[dict]:
    """ Функция принимает список банковских странзакций и возвращает
    список транзакций отфильтрованных по запросу"""
    search_result = []
    for item in data:
        if re.search(search, item['description'], flags=re.IGNORECASE):
            search_result.append(item)

    return search_result


def process_bank_operations(data:list[dict], categories:list)->dict:
    """ Функция принимает список транзакций,а возвращает словарь,
     где отражается вид и считает количество запрошенных операций"""
    matched_categories = []
    compiled_patterns = {}

    for category in categories:
         escaped_category = re.escape(category.lower())
         pattern = r'\b' + escaped_category + r'\b'
         compiled_patterns[category] = re.compile(pattern, re.IGNORECASE)

    for transaction in data:
        description = transaction.get('description', '').lower()
        if not description:
            continue

        found_category = None

        for category, pattern in compiled_patterns.items():
            if pattern.search(description):
                found_category = category.lower()
                break

        if found_category:
            matched_categories.append(found_category)

    counter = Counter(matched_categories)
    result = dict(counter)

    for category in categories:
        lower_category = category.lower()
        if lower_category not in result:
            result[lower_category] = 0

    return result
