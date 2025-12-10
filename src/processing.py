from datetime import datetime


def filter_by_state(list_of_dicts: list, acc_state: str = "EXECUTED") -> list:
    """Функция принимает список словарей и значение ключа "state" (по умолчанию 'EXECUTED'
    и возвращает список словарей, содержащий только словари c указанным ключом state"""

    # Если на вход функции передан пустой список словарей
    if list_of_dicts == []:
        raise ValueError("Нет данных")

    # Если список на входе не пустой
    else:
        # Заполнение списка - фильтрация по указанному значению ключа "state"
        account_list = [account for account in list_of_dicts if account.get("state", "Unknown") == acc_state]
    # Возвращаем результат - отфильтрованный список
    return account_list


def sort_by_date(list_of_dicts: list, revers: bool = True) -> list:
    """Функция принимает список словарей и возвращает список, отсортированный по дате"""

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
    # Возвращаем отсортированнный список с корректными датами
    return acc_sorted_list
