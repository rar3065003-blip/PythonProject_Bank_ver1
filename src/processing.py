def filter_by_state(user_calculate: list, state: str = "EXECUTED") -> list:
    """принимает список словарей и возвращает новый список словарей по значению 'state'"""
    result_selection = []
    for i in user_calculate:
        if i["state"] == state:
            result_selection.append(i)

    return result_selection


def sort_by_date(date_calculate: list, reverse: bool = True) -> list:
    """Принимает список словарей и порядок сортировки возвращает новый список с сортировкой по дате"""

    return sorted(date_calculate, key=lambda item: item["date"], reverse=reverse)
