import json
import os
from json import JSONDecodeError
from unittest.mock import mock_open, patch

import pytest

from src.utils import BASE_DIR, get_transaction_data


# Тест корректного чтения json-файла и получения списка словарей
def test_get_transaction_list(transaction_list_from_json):
    test_path = os.path.join(BASE_DIR, "tests", "test_operations.json")
    assert get_transaction_data(test_path) == transaction_list_from_json


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
    """Тестирование функции get_transaction_data в случае отсутствия или некорректного пути к файлу"""
    assert get_transaction_data(test_file_path) == expected


# Тест c mock при отсутствии файла или невозможности открыть файл
def test_file_not_found():
    with patch("builtins.open", side_effect=FileNotFoundError("File not found")) as mock_open:
        result = get_transaction_data("mock.json")
        assert result == []
        mock_open.assert_called_once_with("mock.json", "r", encoding="utf-8")


# Тест с mock на ошибки с декодированием JSON-файла
def test_json_decode_error():
    with patch("builtins.open") as mock_open:
        with patch("json.load", side_effect=JSONDecodeError("Invalid JSON", "doc", 0)):
            assert get_transaction_data("mock.json") == []
            mock_open.assert_called_once_with("mock.json", "r", encoding="utf-8")


# Тест на успешное открытие и декодирование файла транзакций
def test_load_jsonfile(transaction_list_from_json):
    test_data = transaction_list_from_json
    m = mock_open(read_data=json.dumps(test_data))
    with patch("builtins.open", m):
        result = get_transaction_data("mock.json")
        assert result == test_data
        m.assert_called_once_with("mock.json", "r", encoding="utf-8")
