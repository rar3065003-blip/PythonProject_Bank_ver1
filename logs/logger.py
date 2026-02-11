import logging
from src.masks import get_mask_card_number

def setup_logging():
    logging.basicConfig(level=logging.DEBUG,
                        format= '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        filename ='application.log',
                        filemode='w')
    global get_mask_card_number_logger, get_mask_account, dict_transactions, convertation_currency

    # логеры компонентов программ
    # директория masks
    get_mask_card_number_logger = logging.getLogger('app.get_mask_card_number')
    get_mask_account = logging.getLogger('app.get_mask_account')
    # директория utils
    dict_transactions = logging.getLogger('app.dict_transactions')
    convertation_currency = logging.getLogger('app.convertation_currency')

setup_logging()
