import asyncio
from utils.utils import async_timed

async def greet(name, delay):
    await asyncio.sleep(delay)
    return f"Hello, {name}!"

# 1、wait for
@async_timed
async def main():
   
    result = await asyncio.wait_for(greet("Alice", 2), timeout=1)
    # 如果协程超时了，那就没法继续运行了
    print(result)

# 2、wait
@async_timed
async def main_2():
    try:
        tasks = [
            asyncio.create_task(greet("Alice", 2)),
            asyncio.create_task(greet("Bob", 1)),
            asyncio.create_task(greet("Charlie", 3)),
        ]
        # 获取已经完成的任务和超时的任务
        done, pending = await asyncio.wait(tasks, timeout=2)
        for task in done:
            print(task.result())
    except asyncio.TimeoutError:
        print("Timeout!")


if __name__ == "__main__":
    asyncio.run(main_2())