from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_info: str) -> str:
    """Функция обрабатывает информацию о картах и счетах. Возвращает строку с замаскированным номером"""
    # Если на вход подана пустая строка, вызывается исключение ValueError
    if account_info == "":
        raise ValueError("Нет информации о карте / счёте")
    # Преобразование строки с информацией о карте /счёте в список
    account_info_list = account_info.split(" ")
    # Задаем маскируемый номер - пустую строку
    masked_number = ""
    # Цифровая часть номера - последний элемент списка
    number_part = account_info_list[-1]
    # Если на входе строка с типом и номером карты, то номер - последний элемент - состоит из 16 символов
    if len(number_part) == 16:
        # Получаем мскируемый номер карты
        masked_number = get_mask_card_number(number_part)
    # Если на входе строка с номером счёта - последний элемент состоит из 20 цифр
    elif len(number_part) == 20:
        # Получаем мскируемый номер счёта
        masked_number = get_mask_account(number_part)
    # Если количество цифр в номере карты или счёта меньше 16 или больше 20, вызывается ошибка
    elif len(number_part) < 16 or len(number_part) > 20:
        raise ValueError("Некорректный номер карты или счета")
    # Если 16 <= номер <= 20 и в нём не только цифры, вызывается ошибка
    elif not number_part.isdigit():
        raise ValueError("Некорректный номер карты или счета")
    # Вывод: соединяем все элементы списка account_info_list, кроме последнего - номера счёта или карты
    # с маскированным номером кары или счёта
    account_info_mask = f"{" ".join(account_info_list[:-1])} {masked_number}"
    return account_info_mask


def get_date(date_string: str) -> str:
    """Функция принимает на вход строку с датой в формате "2025-07-16T02:26:18.671407"
    и возвращает строку с датой в формате "ДД.ММ.ГГГГ" ("16.07.2025")
    """
    # Если передана пустая строка, вызывается исключение ValueError
    if date_string == "":
        raise ValueError("Не указана дата")

    # Если строка не пустая, но короткая, вызывается исключение ValueError
    elif len(date_string) < 5:
        raise ValueError("Некорректная дата")
    # Если строка более 5 символов, т.е. возможно, указан год
    else:
        # Определение разделителя в строке "ГГГГ-ММ-ДД...."
        # Разделитель в строке даты - 5-й сивол после года: может быть "." или "-" или "/"
        separator = date_string[4]
        # Преобразование подстроки с датой "ГГГГ-ММ-ДД" в список составляющих дату в формате ['ГГГГ', 'ММ', 'ДД']
        date_parts = date_string[0:10].split(separator)

        # Проверка на цифровые значения в списке составляющих даты
        for part in date_parts:
            # Если в элементах списка не только цифры, или разделитель - цифра или буква, вызывается исключение
            if not str(part).isdigit() or separator.isdigit() or separator.isalpha():
                raise ValueError("Некорректная дата")
            else:
                # Разворачивание списка и преобразование в строку с разделителем "." (точка)
                date_dmy = ".".join(date_parts[::-1])
        return date_dmy
