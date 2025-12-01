def filter_by_state(list_of_dicts: list, acc_state="EXECUTED") -> list:
    """Функция принимает список словарей и значение ключа state (по умолчанию 'EXECUTED'
    и возвращает список словарей, содержащий только словари c указанным ключом state"""
    # account_list = []
    account_list = [account for account in list_of_dicts if account.get("state") == acc_state]
    return account_list


def sort_by_date(list_of_dicts: list, revers=True) -> list:
    """функция принимает список словарей и возвращает список, отсортированный по дате"""
    acc_sorted_list = []

    return acc_sorted_list
