from functools import wraps
import time


def async_timed(func):
    @wraps(func)
    async def wrapper(*args, **kwargs): # 通用型函数变量
        print(f"starting {func} with args {args} {kwargs}")
        start = time.time()
        try:
            return await func(*args, **kwargs)
        finally:
            end = time.time()
            total = end - start
            print(f"finished {func} with total: {total: .4f}") # 保留4位小数

    return wrapper