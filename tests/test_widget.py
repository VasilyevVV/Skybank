import pytest

from src.widget import get_date, mask_account_card


# Тест корректности обработки информации о карте / счёте
@pytest.mark.parametrize(
    "card_acc_info, expected",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Visa Platinum 8990922113665228", "Visa Platinum 8990 92** **** 5228"),
        ("МИР 2574446287251099", "МИР 2574 44** **** 1099"),
        ("Счет 64686473678894779579", "Счет **9579"),
        ("Счет 35383033474447895560", "Счет **5560"),
    ],
)
def test_mask_account_card(card_acc_info, expected):
    assert mask_account_card(card_acc_info) == expected


# Тест на не цифровые символы в номере карты / счёта
@pytest.mark.parametrize(
    "card_acc_info",
    [
        ("Maestro 1,5683786870519F"),
        ("Visa Gold 59994142284263uf"),
        ("Счет 7V6541084301358743+5"),
        ("Счет ADCD30334744478955**"),
        ("МИР A2B4071689553291+2"),
    ],
)
def test_invalid_character(card_acc_info):
    with pytest.raises(ValueError):
        mask_account_card(card_acc_info)


# Тест на некорректную длину (формат) номера карты - 16 цифр, или счёта - 20 цифр.
@pytest.mark.parametrize(
    "acc_info",
    [
        ("Maestro 1568378"),
        ("Visa Gold 5999414228426325789614"),
        ("Счет 78471"),
        ("Счет 30334744478955787879745102574"),
    ],
)
def test_incorrect_account_info(acc_info):
    with pytest.raises(ValueError):
        mask_account_card(acc_info)


# Тест на пустую строку на входе функции mask_account_card
def test_empty_account_info():
    with pytest.raises(ValueError) as exc_info:
        mask_account_card("")

    assert str(exc_info.value) == "Нет информации о карте / счёте"


# Тест корректной работы функции get_date
@pytest.mark.parametrize(
    "date_str, expected",
    [
        ("2025-07-08T02:26:18.671407", "08.07.2025"),
        ("2025/02/28T05:16:25.641954", "28.02.2025"),
        ("2024.08.31T12:16:25.1534", "31.08.2024"),
    ],
)
def test_get_date(date_str, expected):
    assert get_date(date_str) == expected


# Тест на пустую строку на входе функции get_date
def test_epty_date():
    with pytest.raises(ValueError) as exc_info:
        get_date("")

    assert str(exc_info.value) == "Не указана дата"


# Тест на некорректную строку с датой - временем
@pytest.mark.parametrize(
    "date_str, expected",
    [
        ("202U-07-08T02:28:18", ValueError),
        ("2025-+6-28T05:16:25.641954", ValueError),
        ("2026.05.Ь0T12:16:25.1534", ValueError),
        ("1234567890T0A:BC:DE", ValueError),
        ("2025Y12.28T07:50:12", ValueError),
        ("543", ValueError),
    ],
)
def test_invalid_date(date_str, expected):
    with pytest.raises(ValueError):
        get_date(date_str)
