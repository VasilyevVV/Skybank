import os

from src.config import BASE_DIR_PRO
from src.generators import filter_by_currency
from src.processing import filter_by_state, process_bank_search, sort_by_date
from src.read_tx_files import read_tx_csv, read_tx_excel
from src.utils import get_transaction_data
from src.widget import get_date, mask_account_card

# Определение констант для цвета шрифтов в диалоговых сообщениях
RED = "\033[1;31m"
GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
BLUE = "\033[34m"
RESET = "\033[0m"

# Имена программы и пользователя
program = "\033[1;32mSkybank:\033[0m"
user_name = "\033[1;34mПользователь: \033[0m"


# Отдельная функция для получения ответа от пользователя в диалогах
def get_answer() -> str:
    """Функция запрашивает у пользователя ввести какое-либо значение.
    Возвращает ответ без пробелов сначала или в конце введенного пользователем значения
    """
    answer = input(f"{user_name}").strip()
    return answer.strip()


# Отдельная функция для получения ответа от пользователя: только "да" или "нет"
def get_yes_no_answer() -> str:
    """Функция запрашивает пользователя ввести "Да" или "Нет".
    Возвращает строку: "да" либо "нет".
    """
    answer = input(f"{user_name}").strip()
    while answer.lower() not in {"да", "нет"}:
        print(f"{program} {YELLOW}Введите {GREEN}Да {YELLOW}или {GREEN}Нет{RESET}")
        answer = input(f"{user_name}").strip()
    return answer.lower()


def status_request():
    """Вывод сообщений для запроса статуса, по которому будут отфильтрованы операции"""
    print(f"{program} Введите статус, по которому необходимо выполнить фильтрацию.")
    print(f"Доступные для фильтровки статусы: {GREEN}EXECUTED, CANCELED, PENDING{RESET}")


def main() -> None:
    """Основная функция, реализующая алгоритм работы программы в режиме диалога с пользователем
    и выдачи результата на основе ответов пользователя
    """
    # 1. Выбор файла определённого типа с данными о транзакциях (опреациях)
    print(
        """Привет! Добро пожаловать в программу работы с банковскими транзакциями \033[1;32mSkybank\033[0m.\n
Выберите необходимый пункт меню:
"""
    )
    print(f"{RED}1.{RESET} Получить информацию о транзакциях из JSON-файла")
    print(f"{RED}2.{RESET} Получить информацию о транзакциях из CSV-файла")
    print(f"{RED}3.{RESET} Получить информацию о транзакциях из XLSX-файла")
    # Выбор пункта меню - с файлом какого типа будет работать программа
    menu1_item = get_answer()
    # Для проверки используется множество
    while menu1_item not in {"1", "2", "3"}:
        print(f"{program} {YELLOW}Некорректно выбран пункт меню.{RESET}\n" f"Введите 1, 2 или 3.")
        menu1_item = get_answer()

    # Сообщение о выбранном виде файла, открытие соответствующего файла
    # и получение из него списка операций (списка словарей)
    if menu1_item == "1":
        print(f"{program} Для обработки выбран JSON-файл.")
        file_path = os.path.join(BASE_DIR_PRO, "data", "operations.json")
        tx_list = get_transaction_data(file_path)
    elif menu1_item == "2":
        print(f"{program} Для обработки выбран CSV-файл.")
        file_path = os.path.join(BASE_DIR_PRO, "data", "transactions.csv")
        tx_list = read_tx_csv(file_path)
    else:
        print(f"{program} Для обработки выбран Excel-файл.")
        file_path = os.path.join(BASE_DIR_PRO, "data", "transactions_excel.xlsx")
        tx_list = read_tx_excel(file_path)

    # Вывод сообщений для запроса статуса, по которому следует отобрать операции
    status_request()
    # Запрос статуса для отбора операций
    menu_status_item = get_answer()
    while menu_status_item.upper() not in {"EXECUTED", "CANCELED", "PENDING"}:
        print(f'{program} {YELLOW}Статус операции{RESET} {RED}"{menu_status_item}"{RESET} {YELLOW}недоступен.{RESET}')
        status_request()
        menu_status_item = get_answer()

    # Отбор операций по выбранному статусу
    tx_list = filter_by_state(tx_list, menu_status_item)

    # Вывод сообщения, по какому статусу отфильтрованы операции
    if menu_status_item.upper() == "EXECUTED":
        print(f'{program} Операции отфильтрованы по статусу {GREEN}"EXECUTED"{RESET}')
    elif menu_status_item.upper() == "CANCELED":
        print(f'{program} Операции отфильтрованы по статусу {GREEN}"CANCELED"{RESET}')
    elif menu_status_item.upper() == "PENDING":
        print(f'{program} Операции отфильтрованы по статусу {GREEN}"PENDING"{RESET}')

    # Запрос сортировки операций по дате
    print(f"{program} Отсортировать операции по дате? {GREEN}Да/Нет{RESET}")
    sorting_menu = get_answer()
    while sorting_menu.lower() not in {"да", "нет"}:
        print(
            f"{program} Для сортировки операций по дате введите {GREEN}Да{RESET}\n"
            f"Для вывода без сортировки введите {GREEN}Нет{RESET}"
        )
        sorting_menu = get_answer()

    # Если выбрана сортировка операций по дате, то запрос - в каком порядке?
    if sorting_menu == "да":
        # Запрос порядка сортировки - по возрастанию / по убыванию
        print(f"{program} Отсортировать по возрастанию или по убыванию:{GREEN} В/У{RESET}?")
        direction = get_answer()
        while direction.upper() not in ("В", "У"):
            print(f"{program} Отсортировать по возрастанию или по убыванию:{GREEN} В/У{RESET}?")
            direction = get_answer()
        if direction == "В":
            tx_list = sort_by_date(tx_list, revers=False)
        elif direction == "У":
            tx_list = sort_by_date(tx_list)

    # Запрос о выводе только рублевых транзакций
    print(f"{program} Выводить только рублевые транзакции? {GREEN}Да/Нет{RESET}")
    only_rub = get_yes_no_answer()

    # Если выбраны только рублёвые транзакции, то filter_by_currency вызывается без параметра currency (по ум-ю "RUB")
    if only_rub.lower() == "да":
        rub_transactions = filter_by_currency(tx_list)
        filtered_tx = list(rub_transactions)
    else:
        filtered_tx = tx_list

    # Запрос: выбрать операции по определенному слову в описании?
    print(f"{program} Отфильтровать список транзакций по определенному слову в описании? {GREEN}Да/Нет{RESET}")
    search_attribute = get_yes_no_answer()
    # Если фильтровать оп описанию надо - то запрос критерия для отбора
    if search_attribute.lower() == "да":
        search_str = input(f"{program} Введите критерий для отбора: ").strip()
        while search_str == "":
            search_str = input(f"{program} Введите критерий для поиска: ").strip()
        filtered_tx = process_bank_search(filtered_tx, search_str)

    # Итоговый вывод результата
    print(f"{program} Распечатываю итоговый список транзакций...")
    # Если список транзакций пустой
    if len(filtered_tx) == 0:
        print(f"{program} {YELLOW}Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.{RESET}")
    # Если в результате отбора транзакции найдены
    else:
        print(f"{program}")
        print(f"Всего банковских операций в выборке: {len(filtered_tx)}\n")
        for tx in filtered_tx:
            tx_date = get_date(tx.get("date"))
            tx_description = tx.get("description", "N/A")
            print(f"{tx_date} {tx_description}")
            tx_to = ""
            if tx.get("to"):
                tx_to = mask_account_card(tx["to"])
            if tx.get("from"):
                tx_from = mask_account_card(tx["from"])
                print(f"{tx_from} -> {tx_to}")
            # если в операции отсутствует поле "from", например, Открытие вклада, то вывод в другом виде
            else:
                print(f"{tx_to}")
            # Для JSON-структуры
            if "operationAmount" in tx:
                tx_sum = tx.get("operationAmount", {}).get("amount")
                tx_currency = tx.get("operationAmount", {}).get("currency", {}).get("name", "Unknown")
            # Для CSV и XLSX-структур
            else:
                tx_sum = tx.get("amount", "N/A")
                tx_currency = tx.get("currency_code", "Unknown")
            print(f"Сумма: {tx_sum} {tx_currency}\n")


# Запуск программы
if __name__ == "__main__":
    main()
