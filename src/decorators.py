import time
import functools
from collections.abc import Callable


def log(filename = None):
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            msg = f'{start}ms {func.__name__} started \n'
            result = None
            try:
                result = func(*args, **kwargs)
            except Exception as w:
                msg += f'{func.__name__} raised with arguments {args, kwargs} but it didn`t worked, error:{str(w)} \n'
            finally:
                finish = time.time()
                raise_time = finish - start
                msg += f'{raise_time}ms {func.__name__} finished'
                if filename:
                    with open(filename, mode = "a", encoding = "utf-8") as x:
                        x.write(msg + "\n")
                else:
                    print(msg)
            return result

        return wrapper
    return decorator






