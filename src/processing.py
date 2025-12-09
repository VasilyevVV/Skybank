from datetime import datetime, timedelta


def filter_by_state(list_of_dicts: list, acc_state="EXECUTED") -> list:
    """Функция принимает список словарей и значение ключа state (по умолчанию 'EXECUTED'
    и возвращает список словарей, содержащий только словари c указанным ключом state"""
    if list_of_dicts == []:  # если передан пустой список словарей
        raise ValueError("Нет данных")
    else:
        account_list = [account for account in list_of_dicts if account.get("state", "Unknown") == acc_state]
    return account_list


def sort_by_date(list_of_dicts: list, revers=True) -> list:
    """функция принимает список словарей и возвращает список, отсортированный по дате"""
    if list_of_dicts == []:  # если передан пустой список словарей
        raise ValueError("Нет данных")
    else:
        # Включение в список для сортировки только словарей с ключом "date" и с корректной длиной строки для значения "date"
        list_bef_sort = [
            account for account in list_of_dicts if ("date" in account and len(account.get("date", "Unknown")) == 26)
        ]
        # Преобразование значений ключа "date" из строки в объекты даты для корректной сортировки и заполнение списка для сортировки
        # Дата должна быть указана строго в формате ГГГГ-ММ-ДДТЧЧ:Мин:Сек.мксек - 26 символов
        list_to_sort_date = []  # Список словарей для сортировки с преобразованными ключами "date" в формат datetime
        for account_dict in list_bef_sort:
            try:
                acc_date = datetime.strptime(account_dict.get("date", "Unknown"), "%Y-%m-%dT%H:%M:%S.%f")
                account_dict["date"] = acc_date
                list_to_sort_date.append(account_dict)
            except ValueError as exc_inf:
                raise ValueError("Некорректный формат даты")
        # Сортировка списка словарей
        acc_sorted_list = sorted(list_to_sort_date, key=lambda account: account.get("date"), reverse=revers)
        # Преобразование значений ключа "date" из datetime в строку
        for acc_info in list_to_sort_date:
            acc_info["date"] = datetime.strftime(acc_info["date"], "%Y-%m-%dT%H:%M:%S.%f")
    return acc_sorted_list
