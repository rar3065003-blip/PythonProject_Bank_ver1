from src.process_bank import process_bank_operations
from src.process_bank import process_bank_search


def test_process_bank_search(fix_tansaction_data: list[dict]) -> None:
    """Тестирование поиска по типу запроса из транзакций"""
    result = process_bank_search(fix_tansaction_data, "Перевод организации")
    # успешный тест
    result_2 = process_bank_search(fix_tansaction_data, "")
    # не успешный тест
    assert result[0]["id"] == "650703"
    assert result_2 == fix_tansaction_data


def test_process_bank_operations(fix_tansaction_data: list[dict]) -> None:
    """Тестирование вывода по запросу списка вариантов типа траннзакций"""
    result = process_bank_operations(fix_tansaction_data, ["Перевод организации", "Перевод с карты на карту"])
    result_2 = process_bank_operations(fix_tansaction_data, ["", ""])
    result_3 = process_bank_operations(fix_tansaction_data, ["ПЕРЕВОД ОРГАНИЗАЦИИ"])
    assert result == {"перевод организации": 1, "перевод с карты на карту": 2}
    assert result_2 == {"": 0}
    assert result_3 == {"перевод организации": 1}
