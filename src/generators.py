from typing import Iterator


def filter_by_currency(transactions: list, currency: str = "RUB") -> Iterator[dict]:
    """
    Функция принимает на вход список словарей, представляющих транзакции.
    Возвращает итератор, поочередно выдающий транзакции,
    где валюта операции соответствует заданной (по умолчанию "USD")
    """
    for one_transaction in transactions:
        # Отбираем только те транзакции, в которых валюта операции соответствует заданной (например, "RUB").
        if "operationAmount" in one_transaction:
            # Для JSON-структуры
            tx_currency = one_transaction.get("operationAmount", {}).get("currency", {}).get("code", "unknown")
        # Для CSV и XLSX-структур
        else:
            tx_currency = one_transaction.get("currency_code")
        if tx_currency == currency:
            yield one_transaction


def transaction_descriptions(transactions: list) -> Iterator[str]:
    """
    Функция - генератор, принимает список словарей с транзакциями
    и возвращает описание каждой операции по очереди.
    """
    for transaction in transactions:
        # Если описание транзакции отсутствует - нет ключа "description", то описание = "n/a"
        tx_description = transaction.get("description", "n/a")
        if tx_description != "n/a":
            yield tx_description


def card_number_generator(start: str | int, stop: str | int) -> Iterator[str]:
    """
    Функция - генератор, выдает номера банковских карт в формате "XXXX XXXX XXXX XXXX", где X — цифра номера карты.
    Принимает начальное и конечное значения для генерации диапазона номеров.
    Генерирует номера карт в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999.
    """
    # Проверка корректности начального значения start, если это не целое число
    if not isinstance(start, int):
        # если строка - это целое число, иначе генерация исключения ValueError
        if str(start).isdigit():
            start_value = int(start)
        else:
            raise ValueError("Некорректное начальное значение")
    else:
        start_value = start
    # Проверка корректности конечного значения stop, если это не целое число
    if not isinstance(stop, int):
        # если строка - это целое число, иначе генерация исключения ValueError
        if str(stop).isdigit():
            stop_value = int(stop)
        else:
            raise ValueError("Некорректное конечное значение")
    else:
        stop_value = stop
    # Сравнение start_value < stop_value
    if start_value <= stop_value:
        # Если диапазон коррекктный - генерация номерров карт в формате "XXXX XXXX XXXX XXXX"
        for i in range(start_value, stop_value + 1):
            # card_number = str(i).zfill(16)
            card_number = f"{i:016d}"
            formatted_card_num = f"{card_number[0:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"
            yield formatted_card_num
