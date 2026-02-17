from logs.logger_masks import setup_logging

logger = setup_logging()


def get_mask_card_number(numbers_1: int) -> str:
    """Принимает на вход номер карты и возвращает маску номера карты"""
    logger.info("Запуск функции get_mask_card_number")
    numbers = str(numbers_1)
    if len(numbers) != 16:
        logger.error("Не корректное число цифр номера карты")
        return "Введите 16 цифр"
    else:
        part_1 = list(numbers[:4])
        part_2 = list(numbers[4:8])
        part_3 = list(numbers[8:12])
        part_4 = list(numbers[12:16])

        part_2[2:4] = ["X", "X"]
        part_3[:] = ["X", "X", "X", "X"]

        result = part_1 + part_2 + part_3 + part_4
        temp = "".join(result)
        hidden_number = " ".join(temp[i : i + 4] for i in range(0, len(temp), 4))
        logger.info("Окончание работы функции get_mask_card_number")
    return hidden_number


def get_mask_account(account_1: int) -> str:
    """Функция принимает номер счета, выводит маску номера счета типа **ХХХХ"""
    logger.info("Запуск функции get_mask_account")
    account = str(account_1)
    if len(account) != 20:
        logger.error("Некорректное количество цифр номера счета")
        return "Введите  номер счета 20 цифр"
    else:
        part_account = account[-4:]
        part_mask = "XX"
        part_sum = part_mask + part_account
        logger.info("Окончание работы функции get_mask_account")
    return part_sum
