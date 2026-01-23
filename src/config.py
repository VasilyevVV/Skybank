import os

# Абсолютный путь к корневой директории проекта,
# с учётом, что рабочие модули и файлы находятся в папках src, tests, data, logs
BASE_DIR_PRO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Путь к каталогу с файлами для тестирования (json, csv, Excel): tests\test_data
TEST_FILE_DIR = os.path.join(BASE_DIR_PRO, "tests", "test_data")
