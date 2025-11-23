from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_info: str) -> str:
    """Функция обрабатывает информацию о картах и счетах. Возвращает строку с замаскированным номером"""
    account_inf_list = account_info.split(" ")
    masked_number = ""
    # Если на входе строка с типом и номером карты, то номер - последний элемент - состоит из 16 символов
    if len(account_inf_list[-1]) == 16:
        masked_number = get_mask_card_number(account_inf_list[-1])
    # Если на входе строка с номером счёта - 20 цифр
    elif len(account_inf_list[-1]) == 20:
        masked_number = get_mask_account(account_inf_list[-1])
    # Вывод: все элементы входной строки без последнего (ноvера счёта или карты)
    # и номер (кары или счёта)  с маской
    account_info_mask = f"{" ".join(account_inf_list[:-1])} {masked_number}"
    return account_info_mask


def get_date(date_string: str) -> str:
    """Функция принимает на вход строку с датой в формате "2025-07-16T02:26:18.671407"
    и возвращает строку с датой в формате "ДД.ММ.ГГГГ" ("16.07.2025"
    """
    # Определение разделитель в подстроке ГГГГ-ММ-ДД
    separator = date_string[4]
    # Деление на подстроки - создание списка и разворачивание его с разделителем "." - точка
    date_parts = date_string[0:10].split(separator)
    date_dmy = ".".join(date_parts[::-1])
    return date_dmy
