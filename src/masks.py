def get_mask_card_number(card_number: int | str) -> str:
    """Функция принимает на вход номер карты и возвращает ее в формате XXXX XX** **** XXXX"""

    # Если номер карты - строка (не целое число), проверяем её длину
    if not isinstance(card_number, int):
        if len(card_number) == 0:
            raise ValueError("Пустой номер карты")

    # Если строка номера содержит пробелы, удаляем их
    card_number_str = str(card_number).replace(" ", "")

    # Если в номере есть не только цифры
    if not card_number_str.isdigit():
        raise ValueError("Номер карты должен состоять только из цифр")

    # Если номер карты не равен 16 цифрам вызывается исключение ValueError
    elif len(card_number_str) != 16:
        raise ValueError("Некорректный номер карты")

    # Если пройдены все проверки
    return f"{card_number_str[0:4]} {card_number_str[4:6]}** **** {card_number_str[-4::]}"


def get_mask_account(account_number: int | str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску в формате **XXXX, где X — цифра номера"""

    # Если переданый на вход номер счёта - не целое число (строка)
    if not isinstance(account_number, int):
        # Если строка пустая
        if len(account_number) == 0:
            raise ValueError("Пустой номер счёта")

        # Если строка с номером счёта не только из цифр
        elif not account_number.isdigit():
            raise ValueError("Номер счёта должен состоять только из цифр")

    # Если номер счёта меньше 20 цифр
    if len(str(account_number)) < 20:
        raise ValueError("Номер счёта должен быть не менее 20 цифр")

    # Если пройдены все проверки
    return "**" + str(account_number)[-4::]
