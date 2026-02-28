import logging
from logging import Logger
from pathlib import Path


def setup_logging_utils() -> Logger:
    """Логирование функции utils с записью в файл application"""
    # Получаем абсолютный путь к папке logs относительно текущего файла
    current_dir = Path(__file__).resolve().parent
    logs_dir = current_dir.parent / "logs"
    logs_dir.mkdir(exist_ok=True)  # Создаёт директорию, если её нет

    log_file = logs_dir / "application.log"

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    # Очищаем существующие обработчики, чтобы избежать дублирования логов
    logger.handlers.clear()

    try:
        # Обработчик файла — используем абсолютный путь
        file_handler = logging.FileHandler(log_file, mode="a", encoding="utf-8")
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    except Exception as e:
        # Если не удалось создать FileHandler, выводим ошибку в консоль
        print(f"Ошибка создания FileHandler: {e}. Логирование в файл недоступно.")
        # В качестве запасного варианта используем StreamHandler
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)

    return logger
