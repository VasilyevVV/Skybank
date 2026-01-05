import pytest


# исходный список для проверки правильности отбора filter_by_state
@pytest.fixture
def input_dict_list():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


# список для проверки отбора со статусом "EXECUTED"
@pytest.fixture
def executed_dict_list():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


# список для проверки отбора со статусом "CANCELED"
@pytest.fixture
def cancelled_dict_list():
    return [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


# Для проверки отсутствия ключа "state"
@pytest.fixture
def no_state_dict():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 594226727, "state": "", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "date": "2019-07-03T18:35:29.512364"},
        {"id": 725065468, "state": "EXECUTED", "date": "2021-12-24T08:21:33.484541"},
    ]


# Результат проверки на отсутствие ключа "state"
@pytest.fixture
def result_no_state():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 725065468, "state": "EXECUTED", "date": "2021-12-24T08:21:33.484541"},
    ]


# Для теста сортировки по убыванию sort_by_date
@pytest.fixture
def desc_sorted_list():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


# Для теста сортировки по возрастанию sort_by_date
@pytest.fixture
def ascending_sort_list():
    return [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]


# Для теста сортировки с одинаковыми датами
@pytest.fixture
def equal_date_list():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 594226727, "state": "None", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 41428829, "state": "CANCELED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 725065468, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]


# Для теста на корректный формат даты и на отсутствие ключа "date"
@pytest.fixture
def sort_invalid_date_list():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2025-09-15T08:07"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-15T02:08:58.425572"},
        {"id": 596226727, "state": "CANCELED", "date": "2024-09-12T21:27:25.241689"},
        {"id": 926328627, "state": "EXECUTED", "date": "2026-05-12T12:37:29.548657"},
        {"id": 615064591, "state": "CANCELED", "date": "2015-10-14T+ERROR-TIME-123"},
        {"id": 6150017, "state": "Unknown", "dat": "T08:21:33.419441"},
        {"id": 56712, "state": "CANCELED"},
    ]


# Результат сортировки при некорректной дате и / или при отсутствии ключа "date"
@pytest.fixture
def sorted_invalid_date_list():
    return [
        {"id": 926328627, "state": "EXECUTED", "date": "2026-05-12T12:37:29.548657"},
        {"id": 596226727, "state": "CANCELED", "date": "2024-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-15T02:08:58.425572"},
    ]


# Фикстуры для модуля generators
# Фикстура для тестирования filter_by_currency и transaction_descriptions - список словарей с транзакциями
@pytest.fixture
def transaction_list():
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 915142746,
            "state": "EXECUTED",
            "date": "2025-07-22T15:00:10.206574",
            "operationAmount": {"amount": "100000.00", "currency": {"name": "RUB", "code": "RUB"}},
            "description": "Перевод с карты на карту",
            "from": "Счет 48250000428972523791",
            "to": "Счет 75651108381000108108",
        },
        {
            "id": 286415217,
            "state": "EXECUTED",
            "date": "2025-10-27T09:12:46.547291",
            "operationAmount": {"amount": "155000.00", "currency": {"name": "EUR", "code": "EUR"}},
            "description": "Перевод между счетами",
            "from": "Счет 48751008611657918424",
            "to": "Счет 48771004605963020451",
        },
        {
            "id": 746816925,
            "state": "EXECUTED",
            "date": "2025-11-04T17:02:50.654274",
            "operationAmount": {"amount": "700000.00", "currency": {"name": "RUB", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 46002542891275228743",
            "to": "Счет 78811081008108108108",
        },
        # В крайней транзакции отсуутствует ключ "description", по умолчанию присваивается "n/a"
        {
            "id": 461125253,
            "state": "CANCELLED",
            "date": "2024-01-12T10:05:22.564821",
            "operationAmount": {"amount": "100.00", "currency": {"name": "CAN", "code": "CAN"}},
            "from": "Счет 40007542921478218770",
            "to": "Счет 58210001007508241908",
        },
    ]


# Фикстура список usd-транзакций
@pytest.fixture
def usd_expected():
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
    ]


# Фикстура список RUB-транзакций
@pytest.fixture
def rub_expected():
    return [
        {
            "id": 915142746,
            "state": "EXECUTED",
            "date": "2025-07-22T15:00:10.206574",
            "operationAmount": {"amount": "100000.00", "currency": {"name": "RUB", "code": "RUB"}},
            "description": "Перевод с карты на карту",
            "from": "Счет 48250000428972523791",
            "to": "Счет 75651108381000108108",
        },
        {
            "id": 746816925,
            "state": "EXECUTED",
            "date": "2025-11-04T17:02:50.654274",
            "operationAmount": {"amount": "700000.00", "currency": {"name": "RUB", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 46002542891275228743",
            "to": "Счет 78811081008108108108",
        },
    ]


# Фикстура - список с описанием транзакций
@pytest.fixture
def trans_descript_list():
    return [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод между счетами",
        "Перевод со счета на счет",
    ]


# Фикстура - список транзакций, полученный из json-файла
@pytest.fixture
def transaction_list_from_json():
    return [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        },
        {
            "id": 587085106,
            "state": "EXECUTED",
            "date": "2018-03-23T10:45:06.972075",
            "operationAmount": {"amount": "48223.05", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Открытие вклада",
            "to": "Счет 41421565395219882431",
        },
    ]
