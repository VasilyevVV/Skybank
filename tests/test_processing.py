import pytest

from src.processing import filter_by_state, sort_by_date


# Тест по статусу "EXECUTED"
def test_filter_by_state_exec(input_dict_list, executed_dict_list):
    assert filter_by_state(input_dict_list, "EXECUTED") == executed_dict_list


# Тест по статусу "CANCELED"
def test_filter_by_state_cancel(input_dict_list, cancelled_dict_list):
    assert filter_by_state(input_dict_list, "CANCELED") == cancelled_dict_list


# Тест на пустой список словарей
def test_empty_list():
    with pytest.raises(ValueError) as exc_info:
        filter_by_state([])
        assert str(exc_info.value) == "Нет данных"


# Тест на отсутствие ключа state или на его некорректное (пустое) значение
def test_no_state(no_state_dict, result_no_state):
    assert filter_by_state(no_state_dict) == result_no_state


# Тест на сортировку
def test_sort_dy_date(input_dict_list, desc_sorted_list, ascending_sort_list):
    assert sort_by_date(input_dict_list) == desc_sorted_list
    assert sort_by_date(input_dict_list, revers=False) == ascending_sort_list


# Тест на пустой список словарей для сортировки по дате
def test_empty_dict():
    with pytest.raises(ValueError) as exc_info:
        sort_by_date([])
        assert str(exc_info.value) == "Нет данных"


# Тест на корректность сортировки при одинаковых датах
def test_equal_date(equal_date_list):
    assert sort_by_date(equal_date_list) == equal_date_list
    assert sort_by_date(equal_date_list, revers=False) == equal_date_list


# Тест на некорректныe форматs даты
def test_invalid_date(sort_invalid_date_list, sorted_invalid_date_list):
    with pytest.raises(ValueError) as exc_info:
        assert sort_by_date(sort_invalid_date_list) == sorted_invalid_date_list
