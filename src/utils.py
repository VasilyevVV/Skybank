import json
import logging
import os
from json import JSONDecodeError

# Получаем абсолютный путь к корневой директории проекта (с учётом, чтомодуль находится в папке src)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Путь к папке logs, находящейся на том же уровне, что и  папка с модулями src - в корне проекта
log_path = os.path.join(BASE_DIR, "logs", "utils.log")


# Создание логгера, хендлера и форматтера для логирования в файл, перезаписываемый при каждом запуске программы
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(log_path, mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(filename)s - %(levelname)s: %(message)s.")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_transaction_data(filepath: str) -> list[dict]:
    """
    Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях.
    Если файл пустой, содержит не список или не найден, возвращает пустой список.
    """
    try:
        with open(filepath, "r", encoding="utf-8") as tx_file:
            try:
                transaction_data = json.load(tx_file)
                logger.info(f'Файл "{filepath}" успешно открыт и прочитан')
                return transaction_data
            except JSONDecodeError:
                filename = os.path.basename(filepath)
                logger.error(f'Ошибка декодирования файла "{filename}"')
                return []
    except FileNotFoundError:
        logger.error(f'Файл "{filepath}" не найден')
        return []
