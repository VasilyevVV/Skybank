from functools import wraps
from time import localtime, strftime, time
from typing import Any, Callable


def log(filename=None) -> Any:
    """Функция-декоратор: автоматически логирует начало и конец выполнения функции, а также ее результаты
    или возникшие ошибки. Необязательный аргумент filename определяет, куда будут записываться логи:
    - если filename задан, логи записываются в указанный файл
    - сли filename не задан, логи выводятся в консоль.
    """

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapped(*args, **kwargs) -> Any:
            start_time = time()
            # Попытка вызвать функцию и получить результат, с фиксацией времени начала и окончания
            try:
                result = func(*args, **kwargs)
                end_time = time()
                # Формирование строки об успешном завершении
                log_string = (
                    f"Функция: {func.__name__}: OK. "
                    f"Старт: {strftime('%Y-%m-%d %H:%M:%S', localtime(start_time))} "
                    f"Стоп: {strftime('%Y-%m-%d %H:%M:%S', localtime(end_time))}."
                )
            except Exception as exc:
                result = "ERROR"
                # Формирование сообщения об ошибке
                log_string = f"{func.__name__}: {result}: {str(exc)}. Inputs: {args}, {kwargs}."
            # Если имя лог-файла указано, открываем его в режиме добавления записей
            if filename:
                with open(filename, "a+t", encoding="utf-8") as log_file:
                    print(log_string, file=log_file)
            else:
                # Если имя лог-файла не задано - вывод в консоль
                print(log_string)
            return result

        return wrapped

    return decorator
