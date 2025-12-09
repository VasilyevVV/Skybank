from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_info: str) -> str:
    """Функция обрабатывает информацию о картах и счетах. Возвращает строку с замаскированным номером"""
    if account_info == "":  # Если на вход подана пустая строка
        raise ValueError("Отсутствует информация о карте / счёте")
    account_info_list = account_info.split(" ")
    masked_number = ""
    num_part = account_info_list[-1]  # Частьт строки - номер карты или счёта (последний элемент в списке)
    # Если на входе строка с типом и номером карты, то номер - последний элемент - состоит из 16 символов
    if len(num_part) == 16:
        masked_number = get_mask_card_number(num_part)
    # Если на входе строка с номером счёта - последний элемент состоит из 20 цифр
    elif len(num_part) == 20:
        masked_number = get_mask_account(num_part)
    # Если количество цифр в номере карты или счёта меньше 16 или больше 20
    elif len(num_part) < 16 or len(num_part) > 20:
        raise ValueError("Некорректный номер карты или счета")
    elif not num_part.isdigit():
        raise ValueError("Некорректный номер карты или счета")
    # Вывод: все элементы входной строки без последнего (ноvера счёта или карты)
    # и номер (кары или счёта)  с маской
    account_info_mask = f"{" ".join(account_info_list[:-1])} {masked_number}"
    return account_info_mask


# acc_info = "Счет 35383033474447895560"
# print(mask_account_card(acc_info))


def get_date(date_string: str) -> str:
    """Функция принимает на вход строку с датой в формате "2025-07-16T02:26:18.671407"
    и возвращает строку с датой в формате "ДД.ММ.ГГГГ" ("16.07.2025"
    """
    # Определение не передана ли пустая строка
    if date_string == "":
        raise ValueError("Не указана дата")
    elif len(date_string) < 5:  # Указана какая-либо короткая строка
        raise ValueError("Некорректная дата")
    else:
        # Определение разделителя в подстроке "ГГГГ-ММ-ДД...."
        separator = date_string[4]  # Разделитель в строке даты - сивол после года: может быть: "." или "-" или "/"
        # Деление на подстроки - создание списка элементов, составляющих дату ГГГГ, ММ, ДД
        date_parts = date_string[0:10].split(separator)
        # Проверка на цифровые значения в списке составляющих дату.
        # Если хотя бы в одном из них есть не цифры, или разделитель - цифра или буква - вызо исключения
        for part in date_parts:
            if not str(part).isdigit() or separator.isdigit() or separator.isalpha():
                raise ValueError("Некорректная дата")
            else:
                # Разворачивание списка и преобразование в строку с разделителем "." (точка)
                date_dmy = ".".join(date_parts[::-1])
        return date_dmy
