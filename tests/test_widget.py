import pytest
from src.widget import mask_account_card, get_date

# Тест корректности обработки информации о карте / счёте
@pytest.mark.parametrize("card_acc_info, expected", [("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
                                                     ("Visa Platinum 8990922113665228", "Visa Platinum 8990 92** **** 5228"),
                                                     ("МИР 2574446287251099", "МИР 2574 44** **** 1099"),
                                                     ("Счет 64686473678894779579", "Счет **9579"),
                                                     ("Счет 35383033474447895560", "Счет **5560")
                                                     ])
def test_mask_account_card(card_acc_info, expected):
    assert mask_account_card(card_acc_info) == expected


# Тест на не цифровые символы в номере карты / счёта
@pytest.mark.parametrize("card_acc_info", [("Maestro 1,56837868705199"),
                                           ("Visa Gold 59994142284263uf"),
                                           ("Счет 7V6541084301358743+5"),
                                           ("Счет ADCD30334744478955**")])
def test_invalid_character(card_acc_info):
    with pytest.raises(ValueError) as exc_info:
        mask_account_card(card_acc_info)
        assert str(exc_info.value) == "Номер карты должен состоять только из цифр" or str(exc_info.value) == "Некорректный номер счета. Номер может содержать только цифры"


# Тест на некорректную длину (формат) номера карты - 16 цифр, или счёта - 20 цифр.
@pytest.mark.parametrize("acc_info", [("Maestro 1568378"),
                                      ("Visa Gold 5999414228426325789614"),
                                      ("Счет 78471"),
                                      ("Счет 30334744478955787879745102574")])
def test_incorrect_acc_info(acc_info):
    with pytest.raises(ValueError) as exc_info:
        mask_account_card(acc_info)
    assert str(exc_info.value) == "Некорректный номер карты или счета"

# Тест на поустую строку на входе функции mask_account_card
def test_empty_account_info():
    with pytest.raises(ValueError) as exc_info:
        mask_account_card("")
        assert str(exc_info.value) == "Отсутствует информация о карте / счёте"


@pytest.mark.parametrize("date_str, expected", [("2025-07-08T02:26:18.671407", "08.07.2025"),
                                                ("2025/02/28T05:16:25.641954", "28.02.2025"),
                                                ("2024.08.31T12:16:25.1534", "31.08.2024")
                                                ])
# Тест корректной работы функции get_date
def test_get_date(date_str, expected):
    assert get_date(date_str) == expected


# Тест на поустую строку на входе функции get_date
def test_epty_date():
    with pytest.raises(ValueError) as exc_info:
        get_date("")
        assert str(exc_info.value) == "Отсутствует информация о карте / счёте"


