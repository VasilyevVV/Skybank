from unittest.mock import Mock, patch

import pytest
from requests import HTTPError

from src.external_api import API_KEY, get_exchange_rates, get_transaction_sum


# Проверка суммы транзакции в RUB. transaction_dict_rub, transaction_unknown - фикстуры-словари с транзакциями
def test_transaction_sum(transaction_dict_rub, transaction_unknown):
    assert get_transaction_sum(transaction_dict_rub) == 10808.80
    assert get_transaction_sum(transaction_unknown) == 0.0


# Тест с некорректными транзакциями (словарями), в том числе с пустым
def test_invalid_transaction(invalid_transaction_1, invalid_transaction_2, invalid_transaction_3):
    with pytest.raises(ValueError) as exc_info:
        get_transaction_sum({})
    assert str(exc_info.value) == "Ошибка чтения транзакции"
    # Ошибка в ключе "operationAmount"
    with pytest.raises(ValueError) as exc_info1:
        get_transaction_sum(invalid_transaction_1)
    assert str(exc_info1.value) == "Ошибка чтения транзакции"
    # Ошибка в ключе "currency"
    with pytest.raises(ValueError) as exc_info2:
        get_transaction_sum(invalid_transaction_2)
    assert str(exc_info2.value) == "Ошибка чтения транзакции"
    # Ошибка в ключе "code"
    with pytest.raises(ValueError) as exc_info3:
        get_transaction_sum(invalid_transaction_3)
    assert str(exc_info3.value) == "Ошибка чтения транзакции"


# Тест на пусттое значение кода валюты - code
def test_blank_code_transaction(blank_code_transaction):
    with pytest.raises(ValueError) as exc_info:
        get_transaction_sum(blank_code_transaction)
    assert str(exc_info.value) == "Ошибка при указании валюты для конвертирования"


# Tecn функции get_exchange_rates при успешном обращении к сервису конвертирования, mock_responce - фикстура
@patch("requests.get")
def test_exchange_rates(mock_get, mock_responce):
    mock_get.return_value.json.return_value = mock_responce
    mock_get.return_value.status_code = 200
    assert get_exchange_rates(10000, "EUR") == 938874.5
    mock_get.assert_called_once_with(
        "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=EUR&amount=10000", headers={"apikey": API_KEY}
    )


# Тестирование функции get_exchange_rates при неуспешных запросах к сервису конвертирования
@pytest.mark.parametrize(
    "response_status_code, response_reason, expected",
    [
        (400, "Bad Request", "Ошибка выполнения запроса. Возможная причина: "),
        (401, "Unauthorized", "Ошибка выполнения запроса. Возможная причина: "),
        (403, "Forbidden", "Ошибка выполнения запроса. Возможная причина: "),
        (522, "Server Error", "Ошибка выполнения запроса. Возможная причина: "),
    ],
)
@patch("requests.get")
def test_bad_request_exchange_rates(mock_get, response_status_code, response_reason, expected):
    mock_response = Mock()
    mock_response.status_code = response_status_code
    mock_response.reason = response_reason
    mock_get.return_value = mock_response
    with pytest.raises(HTTPError) as err_info:
        get_exchange_rates(100, "EUR")
    assert str(err_info.value) == f"{expected}{response_reason}"
