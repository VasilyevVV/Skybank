import json
from json import JSONDecodeError


def get_transaction_data(filepath: str) -> list[dict]:
    """
    Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях.
    Если файл пустой, содержит не список или не найден, возвращает пустой список.
    """
    try:
        with open(filepath, "r", encoding="utf-8") as transaction_file:
            try:
                transaction_data = json.load(transaction_file)
                return transaction_data
            except JSONDecodeError:
                print("Ошибка декодирования файла")
                return []
    except FileNotFoundError:
        print(f"Файл {filepath} не найден")
        return []
