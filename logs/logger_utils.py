import logging
from logging import Logger


def setup_logging_utils() -> Logger:
    """Логирование функции utils с записью в файл application"""
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    file_handler = logging.FileHandler("../logs/application.log", mode="w", encoding="utf8")
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s " "- %(levelname)s - %(message)s",
    )
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger
