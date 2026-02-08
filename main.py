from src.utils import convertation_currency
from src.utils import dict_transactions
from src.widget import get_date
from src.widget import mask_account_card

if __name__ == "__main__":
    result_1 = mask_account_card("Maestro 1596837868705199")
    result_2 = mask_account_card("Счет 73654108430135874305")
    result_3 = get_date("2024-03-11T02:26:18.671407")
    print(result_1)
    print(result_2)
    print(result_3)

    results: list[dict] = dict_transactions("../data/operations.json")
    for i in results:
        result_data: float = convertation_currency(i)
        print(result_data)
        break
