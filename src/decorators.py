import functools
import time
from collections.abc import Callable
from typing import Any

from config import ROOT_DIR


def log(filename: Any = None) -> Callable:
    """Функция записи лога выполнения исполняемой функции -
    сохраняет в лог в файл при задании имени или выводит в консоль"""

    def decorator(func: Callable) -> Callable:
        """Принимает вызов функции"""

        @functools.wraps(func)
        def wrapper(*args: tuple, **kwargs: dict) -> Any:
            """Оборачиваем функцию и запускаем запись и вычисление времени работы"""
            start = time.time()
            msg = f"{start} s {func.__name__} started \n"
            result = None
            try:
                result = func(*args, **kwargs)
            except Exception as w:
                msg = f"{func.__name__} raised with arguments {args, kwargs}\n but it didn`t worked, error:{str(w)} \n"
            finally:
                finish = time.time()
                raise_time = (finish - start) * 1000
                msg += f"{raise_time} s {func.__name__} finished"
                if filename:
                    with open(f"{ROOT_DIR}/data/{filename}", mode="a", encoding="utf-8") as x:
                        x.write(msg + "\n")
                else:
                    print(msg)
            return result

        return wrapper

    return decorator


@log("mylog.txt")
def my_function(x: int, y: int) -> Any:
    return x / y


my_function(5, 2)

# filename="mylog.txt"
