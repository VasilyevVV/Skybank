def get_mask_card_number(card_number: int | str) -> str:
    """Функция принимает на вход номер карты и возвращает ее в формате XXXX XX** **** XXXX"""
    if not isinstance(card_number, int):  # Если номер карты - строка (не целое число), проверяем её длину
        if len(card_number) == 0:
            raise ValueError("Пустой номер карты")
    card_number_str = str(card_number).replace(" ", "")  # Если номер содержит пробелы, удаляем их
    if not card_number_str.isdigit():  # если в номере не только цифры
        raise ValueError("Номер карты должен состоять только из цифр")
    elif (
        len(card_number_str) != 16
    ):  # если номер карты не равен 16 цифрам. Число цифр в номере карты можно изменить, пока такое условие - 16 цифр
        raise ValueError("Некорректный номер карты")
    # если пройдены все проверки
    return f"{card_number_str[0:4]} {card_number_str[4:6]}** **** {card_number_str[-4::]}"


def get_mask_account(account_number: int | str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску в формате **XXXX, где X — цифра номера"""
    if not isinstance(account_number, int):  # если на вход передан номер счёта - не целое число (строка)
        if len(account_number) == 0:  # если строка пустая
            raise ValueError("Пустой номер счёта")
        elif not account_number.isdigit():  # если строка с номером счёта не только из цифр
            raise ValueError("Номер счёта должен состоять только из цифр")
    # если номер счёта меньше 20 цифр
    if len(str(account_number)) < 20:
        raise ValueError("Номер счёта должен быть не менее 20 цифр")
    # если пройдены все проверки
    return "**" + str(account_number)[-4::]
