import logging


def setup_logging_masks():
    logging.basicConfig(level=logging.DEBUG,
                        format= '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        filename ='application.log',
                        filemode='w',
                        encoding='utf-8')
    global get_mask_card_number_logger, get_mask_account_logger

    get_mask_card_number_logger = logging.getLogger('app.get_mask_card_number')
    get_mask_account_logger = logging.getLogger('app.get_mask_account')

setup_logging_masks()

def get_mask_card_number(numbers_1: int) -> str:
    """Принимает на вход номер карты и возвращает маску номера карты"""
    get_mask_card_number_logger.info("Сообщение о запуске функции get_mask_card_number")

    numbers = str(numbers_1)
    if len(numbers) != 16:
        get_mask_card_number_logger.error("Не корректная длинна номера карты, %d", len(numbers))
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

    return hidden_number


def get_mask_account(account_1: int) -> str:
    """Функция принимает номер счета, выводит маску номера счета типа **ХХХХ"""
    get_mask_account_logger.info("Запуск функции get_mask_account")
    account = str(account_1)
    if len(account) != 20:
        get_mask_account_logger.error("Не корректная длинна номера карты, %d", len(account))
        return "Введите  номер счета 20 цифр"
    else:
        part_account = account[-4:]
        part_mask = "XX"
        part_sum = part_mask + part_account

    return part_sum


result = get_mask_account(1234568912345678978)
print(result)
result_2 = get_mask_card_number(123456891234567)
print(result_2)