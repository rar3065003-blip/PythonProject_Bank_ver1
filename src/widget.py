def mask_account_card(user_number: str):
    """Принимает номер карты или счета и выводит ее маску"""
    user_number = input()
    count_code = 0
    mask = None
    for char in user_number:
        if char.isdigit():
            count_code += 1

    if count_code not in (16, 20):
        print("Введите корректный номер Вашей карты или счета")
    elif count_code == 20:
        mask = f"**{user_number[-4:]}"
        print(f'Счет {mask}')
    elif count_code == 16:
        mask_card = f"{user_number[-16:-10]}******{user_number[-4:]}"
        # temp = f'{user_number[ : -16]} {mask_card}'
        # temp = "".join(mask_card)
        # hidden_number = " ".join(temp[i: i + 4] for i in range(-16, 0, 4))
        # final_mask = f'{(user_number[ :-16])}{mask_card}'
        hidden_number = " ".join(mask_card[i: i + 4] for i in range(0, len(mask_card), 4))
        # print(final_mask)
        print(f'{(user_number[:-16])}{hidden_number}')