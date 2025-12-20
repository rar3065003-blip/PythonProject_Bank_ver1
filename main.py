from src.widget import mask_account_card

if __name__ == "__main__":
    result_1= mask_account_card('Maestro 1596837868705199')
    result_2 = mask_account_card('Счет 73654108430135874305')
    print(result_1 )
    print(result_2 )
    # get_mask_card_number(7000792289606361)
    # get_mask_account(73654108430135874305)
