def get_mask_card_number(card_number: int | str) -> str:
    """Функция принимает на вход номер карты и возвращает ее в формате XXXX XX** **** XXXX"""
    card_number_str = str(card_number).replace(" ", "")
    return f"{card_number_str[0:4]} {card_number_str[4:6]}** **** {card_number_str[-4::]}"


def get_mask_account(account_number: int | str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску в формате **XXXX, где X — цифра номера"""
    return "**" + str(account_number)[-4::]
