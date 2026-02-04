import re
from collections import Counter
from datetime import datetime


def filter_by_state(dict_list: list[dict], acc_state: str = "EXECUTED") -> list[dict]:
    """Функция принимает список словарей и значение ключа "state" (по умолчанию 'EXECUTED'
    и возвращает список словарей, содержащий только словари c указанным ключом state"""

    # Если на вход функции передан пустой список словарей
    if dict_list == []:
        raise ValueError("Нет данных")

    # Если список на входе не пустой
    else:
        # Заполнение списка - фильтрация по указанному значению ключа "state"
        account_list = [account for account in dict_list if account.get("state", "Unknown") == acc_state]
    # Возвращаем результат - отфильтрованный список
    return account_list


def sort_by_date(list_of_dicts: list[dict], revers: bool = True) -> list[dict]:
    """Функция принимает список словарей и возвращает список словарей, отсортированный по дате"""

    # Если на вход передан пустой список словарей
    if list_of_dicts == []:
        raise ValueError("Нет данных")
    else:
        # Включение в список для сортировки только словарей с ключом "date" и с корректной длиной строки
        list_before_sort = [
            account for account in list_of_dicts if ("date" in account and len(account.get("date", "Unknown")) == 26)
        ]
        """
        Преобразование значений для ключа "date" из строки в объекты даты для корректной сортировки и заполнение списка
        Дата должна быть указана строго в формате "ГГГГ-ММ-ДДТЧЧ:Мин:Сек.миксек", длина строки - 26 символов
        """
        # Создание списка словарей для сортировки с преобразованными значениями "date" в формат datetime
        list_to_sort = []
        for account_dict in list_before_sort:
            try:
                # Преобразование строковых значений "date" в объекты даты для каждого словаря в списке
                acc_date = datetime.strptime(account_dict.get("date", "Unknown"), "%Y-%m-%dT%H:%M:%S.%f")
                account_dict["date"] = acc_date
                list_to_sort.append(account_dict)
            # Если преобразование завершается исключением ValueError
            except ValueError:
                raise ValueError("Некорректный формат даты")
        # Сортировка списка словарей
        acc_sorted_list = sorted(list_to_sort, key=lambda account: account.get("date"), reverse=revers)
        # Преобразование значений "date" - объектов datetime обратно в строку
        for acc_info in list_to_sort:
            acc_info["date"] = datetime.strftime(acc_info["date"], "%Y-%m-%dT%H:%M:%S.%f")
    # Возвращаем отсортированный список с корректными датами
    return acc_sorted_list


def process_bank_search(tx_list: list[dict], search: str) -> list[dict]:
    """
    Функция принимает на вход список словарей с данными о банковских операциях и строку поиска.
    Возвращает список словарей, у которых в описании есть данная строка.
    """
    # Если строка поиска пустая - возвращается пустой список
    if search == "":
        return []
    # Проверка наличия ключа "description" и выборка в выходной список словарей
    # с описанием, указанным в строке поиска search, найденным в поле "description"
    result = [
        operation
        for operation in tx_list
        if operation.get("description") and re.search(search, operation["description"], flags=re.IGNORECASE)
    ]
    return result


def process_bank_operations(tx_data: list[dict], categories: list) -> dict:
    """
    Функция принимает список словарей с данными о банковских операциях и список категорий операций.
    Возвращает словарь, в котором ключи — это названия категорий,
    а значения — это количество операций в каждой категории.
    """
    # Если список описаний операций "categories" пустой - возвращается пустой словарь
    if len(categories) == 0:
        return {}
    # Составление списка всех категорий
    description_list = [desc["description"] for desc in tx_data if desc["description"] in categories]
    # Подсчёт количества оперций по категориям и преобразование в словарь
    result_dict = dict(Counter(description_list))
    # Получение отсортированного словаря на основе сортировки словаря по ключам (в т.ч. для тестирования)
    sorted_result = {k: result_dict[k] for k in sorted(result_dict)}
    return sorted_result
