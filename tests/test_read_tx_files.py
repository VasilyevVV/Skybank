import os
from unittest.mock import patch

import pytest

from src.config import TEST_FILE_DIR
from src.read_tx_files import read_tx_csv, read_tx_excel


# Тест корректного чтения CSV-файлов с разными разделителями и получения списка словарей
def test_read_tx_csv(dict_list_csv):
    # путь к файлу с разделителями точка с запятой - ;
    test_file_path = os.path.join(TEST_FILE_DIR, "test_tx.csv")
    # путь к файлу с разделителями - запятыми
    test_comma_file_path = os.path.join(TEST_FILE_DIR, "test_comma_tx.csv")

    assert read_tx_csv(test_file_path) == dict_list_csv
    assert read_tx_csv(test_comma_file_path) == dict_list_csv


# Тест чтения CSV-файла в случае отсутствия или при некорректном пути к файлу
@pytest.mark.parametrize(
    "test_path, expected",
    [
        ("data/transaction", []),
        ("", []),
        ("tests/test_data/test_empty_tx.csv", []),
        ("tests/test_data/test_no_csv.txt", []),
    ],
)
def test_read_no_csv_file(test_path, expected):
    assert read_tx_csv(test_path) == expected


# Тест c mock при отсутствии файла или невозможности открыть файл
def test_file_not_found():
    with patch("builtins.open", side_effect=FileNotFoundError("File not found")) as mock_open:
        result = read_tx_csv("mock.csv")
        assert result == []
        mock_open.assert_called_once_with("mock.csv", mode="r", newline="", encoding="utf-8")


# Тест корректного чтения Excel-файла и получения списка словарей
def test_read_tx_excel(dict_list_excel):
    test_file_path = os.path.join(TEST_FILE_DIR, "test_tx_xls.xlsx")
    assert read_tx_excel(test_file_path) == dict_list_excel


# Тест чтения пустого Excel-файла
def test_read_empty_excel():
    test_file_path = os.path.join(TEST_FILE_DIR, "test_empty_xls.xlsx")
    assert read_tx_excel(test_file_path) == []


# Тест на открытие несуществующего Excel-файла или при некорректном пути к файлу
@pytest.mark.parametrize(
    "inv_file_path",
    [
        ("tx_file.xlsx"),
        ("../test_data/tx.xls"),
        (""),
    ],
)
def test_read_invalid_excel(inv_file_path):
    with pytest.raises(FileNotFoundError) as exc_info:
        read_tx_excel(inv_file_path)
    assert str(exc_info.value) == f"Файл не найден: {inv_file_path}"


# Тест чтения некорректного Excel-файла
@pytest.mark.parametrize("no_xls_file", [("test_no_csv.txt"), ("test_no_json.json"), ("test_empty.json")])
def test_incorrect_file(no_xls_file):
    test_file_path = os.path.join(TEST_FILE_DIR, no_xls_file)
    with pytest.raises(ValueError) as err_info:
        read_tx_excel(test_file_path)
    assert str(err_info.value) == f"Ошибка чтения файла: {test_file_path}"
