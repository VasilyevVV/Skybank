import os

import pytest

from src.config import TEST_FILE_DIR
from src.processing import filter_by_state, process_bank_operations, process_bank_search, sort_by_date
from src.read_tx_files import read_tx_csv


# Тест обработки списка словарей с разными статусами ("EXECUTED", "CANCELED")
def test_filter_by_state_exec(input_dict_list, executed_dict_list, cancelled_dict_list):
    assert filter_by_state(input_dict_list, "EXECUTED") == executed_dict_list
    assert filter_by_state(input_dict_list, "CANCELED") == cancelled_dict_list


# Тест на пустой список словарей
def test_empty_list():
    with pytest.raises(ValueError):
        filter_by_state([])


# Тест на отсутствие ключа state или на его некорректное (пустое) значение
def test_no_state(no_state_dict, result_no_state):
    assert filter_by_state(no_state_dict) == result_no_state


# Тест на корректность сортировки
def test_sort_dy_date(input_dict_list, desc_sorted_list, ascending_sort_list):
    assert sort_by_date(input_dict_list) == desc_sorted_list
    assert sort_by_date(input_dict_list, revers=False) == ascending_sort_list


# Тест на пустой список словарей для сортировки по дате
def test_empty_dict():
    with pytest.raises(ValueError):
        sort_by_date([])


# Тест на корректность сортировки при одинаковых датах
def test_equal_date(equal_date_list):
    assert sort_by_date(equal_date_list) == equal_date_list
    assert sort_by_date(equal_date_list, revers=False) == equal_date_list


# Тест на некорректные форматы даты
def test_invalid_date(sort_invalid_date_list, sorted_invalid_date_list):
    with pytest.raises(ValueError):
        sort_by_date(sort_invalid_date_list) == sorted_invalid_date_list


# Тест функции выборки операций с указанным описанием ("description")
def test_find_tx_by_description(dict_list_csv, list_operations, transaction_list_from_json, finded_json_list):
    # Поиск операций со словом "Перевод" - первые 2 операции в списке list_operations
    assert process_bank_search(dict_list_csv, "перевод") == list_operations[0:2]
    # Поиск операций со словом "вклад" - 3-я операция в списке list_operations
    assert process_bank_search(dict_list_csv, "вклад") == list_operations[2:]
    # Если строка поиска - пустая
    assert process_bank_search(dict_list_csv, "") == []
    # Если не найдено ни одной операции с казанным описание
    assert process_bank_search(dict_list_csv, "неизвестно") == []
    # Поиск в списке словарей, полученных из json-файла
    assert process_bank_search(transaction_list_from_json, "Перевод") == finded_json_list


# Тест функции подсчёта категорий операций c разными списками категорий
@pytest.mark.parametrize(
    "categories, expected_dict",
    [
        (["Перевод с карты на карту"], {"Перевод с карты на карту": 12}),
        (
            ["Перевод организации", "Перевод со счета на счет", "Открытие вклада", "Перевод с карты на карту"],
            {
                "Открытие вклада": 5,
                "Перевод организации": 1,
                "Перевод с карты на карту": 12,
                "Перевод со счета на счет": 2,
            },
        ),
        ([], {}),
    ],
)
def test_count_category(categories, expected_dict):
    # Используется тестовый CSV-файл
    test_file_path = os.path.join(TEST_FILE_DIR, "test_tx2.csv")
    tx_test_data = read_tx_csv(test_file_path)
    assert process_bank_operations(tx_test_data, categories) == expected_dict
