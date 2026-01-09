import pytest

from src.utils import get_transaction_data


# Тест корректного чтения json-файла и получения списка словарей
def test_get_transaction_list(transaction_list_from_json):
    path = r"tests\test_operations.json"
    assert get_transaction_data(path) == transaction_list_from_json


@pytest.mark.parametrize(
    "test_file_path, expected",
    [
        ("data/operation", []),
        ("", []),
        ("tests/test_empty.json", []),
        ("tests/test_no_json.json", []),
    ],
)
def test_get_transaction_no_file(test_file_path, expected):
    """ Тестирование функции get_transaction_data в случае отсутствия или некорректного пути к файлу """
    assert get_transaction_data(test_file_path) == expected
