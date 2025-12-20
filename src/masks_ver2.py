def masks_user(name_number: str) -> str:
    numbers = str(numbers_1)
    result = f"{part_1} {part_2}XX XXXX {part_4}"

    return result


def get_mask_account(account_1: int) -> str:
    """Функция принимает номер счета, выводит маску номера счета типа **ХХХХ"""
    account = str(account_1)
    if len(account) != 20:
        return "Введите  номер счета 20 цифр"
    else:
        part_account = f"**{account[-4:]}"

    return part_account
