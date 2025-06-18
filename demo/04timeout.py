import asyncio
from utils.utils import async_timed

async def greet(name, delay):
    await asyncio.sleep(delay)
    return f"Hello, {name}!"

# timeout
@async_timed
async def main():
    try:
        async with asyncio.timeout(2): # 超时后 下面所有的任务都会被取消
            tasks = [
                asyncio.create_task(greet("Alice", 1)),
                asyncio.create_task(greet("Bob", 2)),
                asyncio.create_task(greet("Charlie", 1)),
            ]
            for task in tasks:
                print(await task)
    except asyncio.TimeoutError:
        print("Timeout!")

if __name__ == "__main__":
    asyncio.run(main())