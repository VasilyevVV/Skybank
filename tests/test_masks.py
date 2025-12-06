import pytest

from src.masks import get_mask_account, get_mask_card_number


# Тест на корректное преобразование с разными форматами: int, строка. Количество символов корректное, пробелы могут быть в разных местах.
@pytest.mark.parametrize(
    "card_number, expected",
    [
        (2200792289607341, "2200 79** **** 7341"),
        ("2200792289607341", "2200 79** **** 7341"),
        ("2200 7922 8960 7341", "2200 79** **** 7341"),
        ("0054752989607340", "0054 75** **** 7340"),
        ("0054 752989607341", "0054 75** **** 7341"),
        ("105 47 5 2989 6 07 342", "1054 75** **** 7342"),
    ],
)
def test_correct_card_mask(card_number, expected):
    assert get_mask_card_number(card_number) == expected


# Тест пустого номера карты (пустая строка)
def test_empty_card_mask():
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number("")
        assert str(exc_info.value) == "Пустой номер карты"


# Тест некорректной длины номера карты:больше или меньше 16 символов
@pytest.mark.parametrize(
    "card_number", [(2507), ("2200 79 5182"), (123456789789952375287), ("12345678901234567891234")]
)
def test_incorrect_card_number_length(card_number):
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number(card_number)
        assert str(exc_info.value) == "Некорректный номер карты"


# Тест на наличие символлов, отличных от цифр
@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("507,8024 + 4533.1628", ValueError),
        ("2200:7931& 7182*55V22", ValueError),
        ("1a2b 4568 89c8 9uT7", ValueError),
    ],
)
def test_card_invalid_characters(card_number, expected):
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number(card_number)
        assert str(exc_info.value) == "Номер карты должен состоять только из цифр"


### Тесты для функции get_mask_account ###
# Тест корректности маскирования номера счёта, с различной длиной счёта
@pytest.mark.parametrize(
    "account, expected",
    [
        (73654108430135874305, "**4305"),
        ("41084301753743059521", "**9521"),
        (447718628341772189634821, "**4821"),
        ("44771628341772189634821", "**4821"),
    ],
)
def test_correct_account_mask(account, expected):
    assert get_mask_account(account) == expected


# Тест на пустой номер счёта
def test_epmty_account_number():
    with pytest.raises(ValueError) as exc_info:
        get_mask_account("")
        assert str(exc_info.value) == "Пустой номер счёта"


# Тест на длину номера счёта - не менее 20 цифр
@pytest.mark.parametrize("account", [(7365), ("48430155"), (00), ("00000")])
def test_short_account_number(account):
    with pytest.raises(ValueError) as exc_info:
        get_mask_account(account)
        assert str(exc_info.value) == "Номер счёта должен быть не менее 20 цифр"


# Тест на наличие прочих символов, кроме цифр
@pytest.mark.parametrize("account", [("7365.1084 301+584305"), ("4а108и017537430546502!"), ("77186,2834+17721896U3")])
def test_account_invalid_characters(account):
    with pytest.raises(ValueError) as exc_info:
        get_mask_account(account)
        assert str(exc_info.value) == "Номер счёта должен состоять только из цифр"
