from src.widget import mask_account_card, get_date

if __name__ == "__main__":
    result_1 = mask_account_card('Maestro 1596837868705199')
    result_2 = mask_account_card('Счет 73654108430135874305')
    result_3 = get_date('2024-03-11T02:26:18.671407')
    print(result_1)
    print(result_2)
    print(result_3)
