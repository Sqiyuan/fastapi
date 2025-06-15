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

async def greet1(name, delay):
    await asyncio.sleep(delay)
    if name == "Alice":
        raise ValueError("Alice is not a valid name")
    return f"Hello, {name}!"

@async_timed
#用taskgroup创建任务组
async def main_3():
    try:
        async with asyncio.TaskGroup() as tg:
            task1 = tg.create_task(greet1("Alice", 2))
            task2 = tg.create_task(greet1("Bob", 3))
            task3 = tg.create_task(greet1("Charlie", 4))
    except Exception as e:
        print(e)
    # 协程正常运行结束
    # print(task1.result())
    # print(task2.result())
    # print(task3.result())
    # 出现异常导致提前结束协程（sleep时间短于异常也会done）
    # done: 返回协程是否结束
    # cancelled: 返回协程是否被取消
    print(task1.done())
    print(task2.cancelled())
    print(task3.cancelled())

if  __name__ == "__main__":
    asyncio.run(main_3())