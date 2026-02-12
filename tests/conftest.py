import pytest


# Исходный список для проверки правильности отбора filter_by_state
@pytest.fixture
def input_dict_list():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33"},
    ]


# Список для проверки отбора со статусом "EXECUTED"
@pytest.fixture
def executed_dict_list():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58"},
    ]


# Список для проверки отбора со статусом "CANCELED"
@pytest.fixture
def cancelled_dict_list():
    return [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33"},
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
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58"},
    ]


# Для теста сортировки по возрастанию sort_by_date
@pytest.fixture
def ascending_sort_list():
    return [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29"},
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
        # В крайней транзакции отсутствует ключ "description", по умолчанию присваивается "n/a"
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


# Фикстура - словарь с транзакцией в "RUB"
@pytest.fixture
def transaction_dict_rub():
    return {
        "id": 45743855,
        "state": "EXECUTED",
        "date": "2025-05-02T10:50:00.291521",
        "operationAmount": {"amount": "10808.80", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    }


# Фикстура - словарь с транзакцией в неизвестной валюте (не в EUR или USD)
@pytest.fixture
def transaction_unknown():
    return {
        "id": 441945886,
        "state": "CANCELLED",
        "date": "2024-07-02T03:20:00.521621",
        "operationAmount": {"amount": "7.80", "currency": {"name": "abc", "code": "ABC"}},
        "description": "Перевод",
        "from": "VISA 1596837868705199",
        "to": "Счет 64686473678894779589",
    }


# Фикстура с некорректным ключом "operationAmount"
@pytest.fixture
def invalid_transaction_1():
    return {
        "id": 441975216,
        "state": "EXECUTED",
        "date": "2025-10-12T07:20:15.291521",
        "operation": {"amount": "100.00", "currency": {"name": "руб.", "code": "EUR"}},
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    }


# Фикстура с некорректным ключом "currency"
@pytest.fixture
def invalid_transaction_2():
    return {
        "id": 441975216,
        "state": "EXECUTED",
        "date": "2025-10-12T07:20:15.291521",
        "operationAmount": {"amount": "10808.80", "curr": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    }


# Фикстура с некорректным ключом "code"
@pytest.fixture
def invalid_transaction_3():
    return {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2025-03-27T11:55:14.915214",
        "operationAmount": {"amount": "10.00", "currency": {"name": "руб.", "cod": "USD"}},
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    }


# Фикстура с пустым значением валюты - "code" ("")
@pytest.fixture
def blank_code_transaction():
    return {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2024-01-02T05:57:10.152146",
        "operationAmount": {"amount": "80.80", "currency": {"name": "руб.", "code": ""}},
        "description": "Перевод со счета на счет",
        "from": "Visa GOLD 1596837868705199",
        "to": "Счет 64686473678894779589",
    }


@pytest.fixture
def unknown_tx_currency():
    return {
        "id": 441945886,
        "state": "CANCELLED",
        "date": "2024-07-02T03:20:00.521621",
        "operationAmount": {"amount": "7.80", "currency": {"name": "abc", "code": "ABC"}},
        "description": "Перевод",
        "from": "VISA 1596837868705199",
        "to": "Счет 64686473678894779589",
    }


# Фикстура - результат успешного запроса к сервису конвертации
@pytest.fixture
def mock_responce():
    return {
        "success": True,
        "query": {"from": "EUR", "to": "RUB", "amount": 100},
        "info": {"timestamp": 1767870547, "rate": 93.88745},
        "date": "2026-01-07",
        "result": 938874.5,
    }


# Фикстура - результат успешного чтения csv-файла - список словарей
@pytest.fixture
def dict_list_csv():
    return [
        {
            "id": "650703",
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": "16210",
            "currency_name": "Sol",
            "currency_code": "PEN",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
            "description": "Перевод организации",
        },
        {
            "id": "4234093",
            "state": "EXECUTED",
            "date": "2021-07-08T07:31:21Z",
            "amount": "23182",
            "currency_name": "Ruble",
            "currency_code": "RUB",
            "from": "Visa 0773092093872450",
            "to": "Discover 8602781449570491",
            "description": "Перевод с карты на карту",
        },
        {
            "id": "3107343",
            "state": "EXECUTED",
            "date": "2023-01-25T13:33:00Z",
            "amount": "33639",
            "currency_name": "Krona",
            "currency_code": "SEK",
            "from": "",
            "to": "Счет 35662766798195077538",
            "description": "Открытие вклада",
        },
    ]


# Фикстура - результат успешного чтения Excel-файла - список словарей
@pytest.fixture
def dict_list_excel():
    return [
        {
            "id": 1962667,
            "state": "EXECUTED",
            "date": "2023-10-22T09:43:32Z",
            "amount": 18588,
            "currency_name": "Peso",
            "currency_code": "COP",
            "from": "Mastercard 7286844946221431",
            "to": "Счет 76145988629288763144",
            "description": "Перевод организации",
        },
        {
            "id": 5294458,
            "state": "EXECUTED",
            "date": "2022-06-20T18:08:20Z",
            "amount": 16836,
            "currency_name": "Yuan Renminbi",
            "currency_code": "CNY",
            "from": "Visa 2759011965877198",
            "to": "Счет 38287443300766991082",
            "description": "Перевод с карты на карту",
        },
        {
            "id": 3226899,
            "state": "EXECUTED",
            "date": "2023-04-17T09:21:15Z",
            "amount": 21680,
            "currency_name": "Koruna",
            "currency_code": "CZK",
            "from": "",
            "to": "Счет 88329674734590848775",
            "description": "Открытие вклада",
        },
        {
            "id": 4234093,
            "state": "EXECUTED",
            "date": "2021-07-08T07:31:21Z",
            "amount": 23182,
            "currency_name": "Ruble",
            "currency_code": "RUB",
            "from": "Visa 0773092093872450",
            "to": "Discover 8602781449570491",
            "description": "Перевод с карты на карту",
        },
    ]


# Фикстура для тестирования функции поиска операций по описанию.
# Результат поиска по слову "Перевод"
@pytest.fixture
def list_operations():
    return [
        {
            "id": "650703",
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": "16210",
            "currency_name": "Sol",
            "currency_code": "PEN",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
            "description": "Перевод организации",
        },
        {
            "id": "4234093",
            "state": "EXECUTED",
            "date": "2021-07-08T07:31:21Z",
            "amount": "23182",
            "currency_name": "Ruble",
            "currency_code": "RUB",
            "from": "Visa 0773092093872450",
            "to": "Discover 8602781449570491",
            "description": "Перевод с карты на карту",
        },
        {
            "id": "3107343",
            "state": "EXECUTED",
            "date": "2023-01-25T13:33:00Z",
            "amount": "33639",
            "currency_name": "Krona",
            "currency_code": "SEK",
            "from": "",
            "to": "Счет 35662766798195077538",
            "description": "Открытие вклада",
        },
    ]


@pytest.fixture
def finded_json_list():
    return [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        }
    ]
