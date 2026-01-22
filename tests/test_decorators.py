import os
from time import localtime, strftime, time

import pytest

from src import masks
from src.config import BASE_DIR_PRO
from src.decorators import log


TEST_LOG_FILE = os.path.join(BASE_DIR_PRO, "logs", "my_testlog.txt")


# Декоририуемая функция get_mask_card_number из модуля masks
@log()
def masked_card(cardnumber: str):
    return masks.get_mask_card_number(cardnumber)


# Декоририуемая функция get_mask_account из модуля masks
@log(TEST_LOG_FILE)
def masked_info(account: str):
    return masks.get_mask_account(account)


# Tecn вываода в консоль при корректном входном аргументе
def test_logging_to_cons(capsys):
    start = strftime("%Y-%m-%d %H:%M:%S", localtime(time()))
    masked_card("7008792589506341")
    stop = strftime("%Y-%m-%d %H:%M:%S", localtime(time()))
    out, err = capsys.readouterr()
    assert out == f"Функция: masked_card: OK. Старт: {str(start)} Стоп: {str(stop)}.\n"
    assert err == ""


# Tecn вываода в консоль при некорректных аргументах (пустая строка, неправильно зажан номер карты)
@pytest.mark.parametrize(
    "input_data, expected",
    [
        ("", "Пустой номер карты"),
        ("00001008", "Некорректный номер карты"),
        ("12345+ABC", "Номер карты должен состоять только из цифр"),
    ],
)
def test_error_logging(input_data, expected, capsys):
    masked_card(input_data)
    captured_info = capsys.readouterr()
    assert captured_info.out == f"masked_card: ERROR: {expected}. Inputs: ('{input_data}',), " + "{}.\n"


# Тест записи в лог-файл, корректное завершение функции
def test_logging_to_file():
    start = strftime("%Y-%m-%d %H:%M:%S", localtime(time()))
    masked_info("41084301753743059521")
    stop = strftime("%Y-%m-%d %H:%M:%S", localtime(time()))
    with open(TEST_LOG_FILE, "r", encoding="utf-8") as file:
        full_log = file.readlines()
        log_str = full_log[-1]
        assert log_str == f"Функция: masked_info: OK. Старт: {str(start)} Стоп: {str(stop)}.\n"


# Tecn записи в лог-файл сообщений об ошибке при некорректных входных аргументах
@pytest.mark.parametrize(
    "account_data, expected",
    [
        ("", "masked_info: ERROR: Пустой номер счёта. Inputs: ('',), {}.\n"),
        ("12345+ABC", "masked_info: ERROR: Номер счёта должен состоять только из цифр. Inputs: ('12345+ABC',), {}.\n"),
        ("00001008", "masked_info: ERROR: Номер счёта должен быть не менее 20 цифр. Inputs: ('00001008',), {}.\n"),
    ],
)
def test_error_log_to_file(account_data, expected):
    masked_info(account_data)
    with open(TEST_LOG_FILE, "r", encoding="utf-8") as file:
        full_log = file.readlines()
        log_str = full_log[-1]
        assert log_str == expected
