import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


# Тест функции filter_by_currency (по умолчанию currency="RUB")
def test_filter_by_currency(transaction_list, rub_expected, usd_expected):
    rub_transaction = filter_by_currency(transaction_list)
    usd_transactions = filter_by_currency(transaction_list, "USD")
    assert list(rub_transaction) == rub_expected
    assert list(usd_transactions) == usd_expected


# Тест функции filter_by_currency, когда указанная валюта отсутствует в списке транзакций
def test_missing_currency(transaction_list):
    with pytest.raises(StopIteration):
        tx = filter_by_currency([], "CNY")
        next(tx)


# Tecn функции filter_by_currenc на пустой список транзакций на входе
def test_empty_filter_by_currency():
    with pytest.raises(StopIteration):
        tx = filter_by_currency([], "USD")
        next(tx)


# Тест функции transaction_descriptions
def test_transaction_descriptions_2(transaction_list, trans_descript_list):
    descriptions = transaction_descriptions(transaction_list)
    assert [desc for desc in descriptions] == trans_descript_list


# Тест функции transaction_descriptions, если на входе пустой список
def test_empty_transaction_descriptions(transaction_list):
    with pytest.raises(StopIteration):
        descr = transaction_descriptions([])
        next(descr)


# Тест функции card_number_generator - генератора номеров карт
@pytest.mark.parametrize(
    "start, stop, expected_output",
    [
        (
            "000070021086001",
            "000070021086005",
            [
                "0000 0700 2108 6001",
                "0000 0700 2108 6002",
                "0000 0700 2108 6003",
                "0000 0700 2108 6004",
                "0000 0700 2108 6005",
            ],
        ),
        (
            1004,
            1008,
            [
                "0000 0000 0000 1004",
                "0000 0000 0000 1005",
                "0000 0000 0000 1006",
                "0000 0000 0000 1007",
                "0000 0000 0000 1008",
            ],
        ),
    ],
)
def test_card_number_generator(start, stop, expected_output):
    result = card_number_generator(start, stop)
    assert [card_number for card_number in result] == expected_output


# Тест функции card_number_generator с некорректно заданным диапазоном: stop меньше start
def test_incorrect_range():
    with pytest.raises(StopIteration):
        numbers = card_number_generator(5, "1")
        next(numbers)


# Тест функции card_number_generator с некорректно заданными start или stop (нечисловыми значениями)
@pytest.mark.parametrize(
    "start, stop, exp_out",
    [
        ("R108", 6005, ValueError),
        ("1008", "DF", ValueError),
    ],
)
def test_invalid_start_stop_values(start, stop, exp_out):
    with pytest.raises(exp_out):
        numbers = card_number_generator(start, stop)
        next(numbers)
