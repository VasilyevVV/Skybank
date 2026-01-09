import requests
import os
from dotenv import load_dotenv


# Загрузка переменных из .env-файла
load_dotenv()
# Получение API-ключа из файла .env
API_KEY = os.getenv("API_KEY")


def get_transaction_sum(transaction: dict) -> float:
    """
    Функция принимает на вход словарь-транзакцию и возвращает сумму транзакции (amount) в рублях.
    Если транзакция в USD или EUR вызывается функция get_exchange_rates
    с обращением к сервису (внешнему API) для определения текущего курса валют и конвертации суммы операции в рубли
    с использованием Exchange Rates Data API: https://apilayer.com/exchangerates_data-api
    """
    # Получение значений для валюты транзакции и её суммы из словаря-транзакции
    from_currency = ["EUR", "USD"]
    tx_result = 0.0
    try:
        tx_currency = transaction["operationAmount"]["currency"]["code"]
        tx_amount = transaction["operationAmount"].get("amount", "0.0")
    # Если при чтении словаря-транзакции произошла ошибка (не найден какой-либо ключ)
    except KeyError as exc_key:
        raise ValueError("Ошибка чтения транзакции") from exc_key
        return tx_result
    # Если валюта транзакции не указана - пустая строка
    if tx_currency == "":
        raise ValueError("Ошибка при указании валюты для конвертирования")
        return tx_result
    # Если транзакиия в RUB - вывод результата
    elif tx_currency == "RUB":
        tx_result = round(float(tx_amount), 2)
    # Если транзакиия не в EUR и не в USD - возвращаем 0.0
    elif tx_currency not in from_currency:
        print(f'Указанный код валюты: "{tx_currency}" не поддерживается.')
        return 0.0
    # Если транзакиия в EUR или в USD - обращение к сервису https://api.apilayer.com/exchangerates_data
    else:
        tx_result = get_exchange_rates(tx_amount, tx_currency)
    return tx_result


def get_exchange_rates(amount: float, currency: str) -> float:
    """Функция обращения к сервису - внешнему API для получения текущего курса валют
    и конвертации суммы операции в рубли, с использованием запроса к Exchange Rates Data API:
    https://apilayer.com/exchangerates_data-api
    """
    # Валюта, в которую следует конвертировать: RUB
    convert_to = "RUB"
    # Формирование url, headers (API-ключ)
    url_str = f"https://api.apilayer.com/exchangerates_data/convert?to={convert_to}&from={currency}&amount={amount}"
    request_header = {"apikey": API_KEY}
    # Запрос конвертации с помощью сервиса api.apilayer.com/exchangerates_data/convert
    response = requests.get(url_str, headers=request_header)
    status_code = response.status_code
    reason = response.reason
    # Проверка успешности запроса (статус-код = 200)
    if status_code == 200:
        # Десериализация результата запроса из JSON-формата в объект Python (словарь) с помощью json()
        response_data = response.json()
        tx_result = response_data["result"]
        # Округление и вывод результата
        return round(float(tx_result), 2)
    else:
        # Вывод сообщения об ошибке, если запрос не выполнен
        raise requests.HTTPError(f"Ошибка выполнения запроса. Возможная причина: {reason}")
        return 0.0
