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
