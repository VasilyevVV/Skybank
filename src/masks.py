import logging
import os

# Получаем абсолютный путь к корневой директории проекта (с учётом, что модуль находится в папке src)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Путь к папке logs, находящейся на том же уровне, что и  папка с модулями src - в корне проекта
log_path = os.path.join(BASE_DIR, "logs", "masks.log")


# Создание логгера, хендлера и форматтера для логирования в файл, перезаписываемый при каждом запуске программы
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(log_path, mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(filename)s - %(levelname)s: %(message)s.")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: int | str) -> str:
    """Функция принимает на вход номер карты и возвращает ее в формате XXXX XX** **** XXXX"""

    # Если номер карты - строка (не целое число), проверяем её длину
    if not isinstance(card_number, int):
        if len(card_number) == 0:
            logger.error("Пустой номер карты")
            raise ValueError("Пустой номер карты")

    # Если строка номера содержит пробелы, удаляем их
    card_number_str = str(card_number).replace(" ", "")

    # Если в номере есть не только цифры
    if not card_number_str.isdigit():
        logger.error(f"Некорректный номер карты: {card_number_str}")
        raise ValueError("Номер карты должен состоять только из цифр")

    # Если номер карты не равен 16 цифрам вызывается исключение ValueError
    elif len(card_number_str) != 16:
        logger.error(f"Некорректный номер карты: {card_number_str}")
        raise ValueError("Некорректный номер карты")

    # Если пройдены все проверки
    result = f"{card_number_str[0:4]} {card_number_str[4:6]}** **** {card_number_str[-4::]}"
    logger.info(f"Номер карты с маской: {result}")
    return result


def get_mask_account(account_number: int | str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску в формате **XXXX, где X — цифра номера"""

    # Если переданый на вход номер счёта - не целое число (строка)
    if not isinstance(account_number, int):
        # Если строка пустая
        if len(account_number) == 0:
            logger.error("Пустой номер счёта")
            raise ValueError("Пустой номер счёта")

        # Если строка с номером счёта не только из цифр
        elif not account_number.isdigit():
            logger.error(f"Некорректный номер счёта: {account_number}")
            raise ValueError("Номер счёта должен состоять только из цифр")

    # Если номер счёта меньше 20 цифр
    if len(str(account_number)) < 20:
        logger.error(f"Номер счёта менее 20 цифр: {account_number}")
        raise ValueError("Номер счёта должен быть не менее 20 цифр")

    # Если пройдены все проверки
    result = "**" + str(account_number)[-4::]
    logger.info(f"Номер счета с маской: {result}")
    return result
