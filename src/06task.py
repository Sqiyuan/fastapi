import asyncio
from functools import partial
from utils.utils import async_timed

async def greet(name, delay):
    await asyncio.sleep(delay)
    return f"Hello, {name}!"

# 1、exception方法
async def task_exception():
    await asyncio.sleep(1)
    raise ValueError(f"return Error")

@async_timed
async def main1():
    task = asyncio.create_task(task_exception())
    await asyncio.sleep(1.5)
    print(task.exception())


# 2、add_done_callback方法
def callback(tag, future):
    print("="*20)
    print(type(future))
    print(future.result())
    print(f"tag:{tag}")
    print("="*20)

async def main2():
    task = asyncio.create_task(greet("World", 2))
    # partial: 创建一个偏函数，作用是可以将这个函数提前准备好一些参数
    # task.add_done_callback(partial(callback, tag="task"))
    # 如果是通过位置传递参数，那么tag就必须放在第一个参数位置
    task.add_done_callback(partial(callback, "task"))
    await task


# 3、cancel：取消任务
async def sth():
    print("I'm doing something")
    await asyncio.sleep(20)
    print("I'm done")

async def main():
    task = asyncio.create_task(sth(), name="sth")
    try:
        print(f"name:{task.get_name()}")
        task.set_name("new_name")
        await asyncio.sleep(1)
        print(f"new_name:{task.get_name()}")
        task.cancel()
        await task
    except asyncio.CancelledError as e:
        print(e)
        print(f"Cancelled:{task.cancelled()}")

if __name__ == "__main__":
    asyncio.run(main())