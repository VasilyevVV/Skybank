import csv
import os

import pandas as pd


def find_delimiter(csv_filename: str) -> str:
    """Функция определяет символ-разделитель (delimiter) в csv-файле"""
    sniffer = csv.Sniffer()
    with open(csv_filename) as file:
        delimiter = sniffer.sniff(file.read(2048)).delimiter
    return delimiter


def read_tx_csv(file_path: str) -> list[dict]:
    """Функция для считывания финансовых операций из CSV-файла. Принимает в качестве аргумента путь к файлу CSV.
    Выдает список словарей с транзакциями. Если файл не найден или не является CSV, выдаёт пустой список
    """
    try:
        with open(file_path, mode="r", newline="", encoding="utf-8") as file:
            try:
                # Определение разделителя в csv-файле
                csv_delimiter = find_delimiter(file_path)
                # Создание объекта для преобразования строк в словари
                reader = csv.DictReader(file, delimiter=csv_delimiter)
                # Список словарей для дальнейшего построчного заполнения
                tx_dict_list = []
                # Заполнение списка словарями - строками из reader
                for row in reader:
                    tx_dict_list.append(row)
                return tx_dict_list
            except csv.Error:
                return []
    except FileNotFoundError:
        return []


def read_tx_excel(file_path: str) -> list[dict]:
    """Функция для считывания финансовых операций из Excel-файла. Принимает путь к файлу Excel в качестве аргумента.
    Выдает список словарей с транзакциями.
    Если файл не найден или не в формате Excel, сообщает о соответствующей ошибке
    """
    if os.path.exists(file_path):
        # Если файл существует
        try:
            df_excel = pd.read_excel(file_path, na_filter=False, parse_dates=False)
        except ValueError:
            raise ValueError(f"Ошибка чтения файла: {file_path}")
        else:
            result_dict = df_excel.to_dict(orient="records")
            return result_dict
    else:
        # Если файл по указанному пути не найден
        raise FileNotFoundError(f"Файл не найден: {file_path}")
