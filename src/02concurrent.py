import asyncio

from utils.utils import async_timed

async def greet(name, delay):
    await asyncio.sleep(delay)
    return f"Hello, {name}!"

#  同步代码
@async_timed
async def main_1():
    print(await greet("Alice", 3))
    print(await greet("Bob", 2))
    print(await greet("Charlie", 1))


@async_timed
async def main_2():
    # 并发运行 必须将协程创建为task对象
    tasks = [
        asyncio.create_task(greet("Alice", 3)),
        asyncio.create_task(greet("Bob", 2)),
        asyncio.create_task(greet("Charlie", 1)),
    ]
    for task in tasks:
        print(await task)


if  __name__ == "__main__":
    asyncio.run(main_2())