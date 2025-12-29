from src.masks import get_mask_account
from src.masks import get_mask_card_number


def mask_account_card(user_card: str) -> str:
    """Принимает номер карты или счета и выводит ее маску"""
    user_number = str(user_card)
    count_code = 0
    for char in user_number:
        if char.isdigit():
            count_code += 1

    if count_code not in (16, 20):
        return "Введите корректный номер Вашей карты или счета"

    card_number = user_number.split()[-1]
    if count_code == 20:
        mask = get_mask_account(int(card_number))
        return f"Счет {mask}"

    elif count_code == 16:

        hidden_number = get_mask_card_number(int(card_number))
        return f"{(user_number[:-16])}{hidden_number}"

    return "Неизвестный формат карты"


def get_date(date_user: str) -> str:
    """Принимает данные с датой и выводит дату в формате ДД.ММ.ГГ"""
    date = date_user[0:10]
    year, month, day = date.split("-")

    return f"{day}.{month}.{year}"
