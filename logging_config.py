import os
import logging
import logging.config

from settings import LOG_PATH

os.makedirs('logs', exist_ok=True)

def setup_logging() -> None:
    """
    Функция, формирующая логгер
    """
    logger = logging.getLogger('my_log')
    logger.setLevel(logging.DEBUG)
    file_handler = logging.FileHandler(LOG_PATH, mode="w", encoding="utf-8")
    file_formatter = logging.Formatter("%(asctime)s - %(filename)s - %(levelname)s: %(message)s")
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)
