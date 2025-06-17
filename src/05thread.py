import asyncio
import time
from utils.utils import async_timed

def get_url(url):
    print(f'开始获取URL：{url}')
    time.sleep(2)
    print('结束')
    return 'success'

async def greet(name, delay):
    await asyncio.sleep(delay)
    return print(f"Hello, {name}!")

@async_timed
async def main():
    await asyncio.gather(
        asyncio.to_thread(get_url, 'www.baidu.com'),
        greet('World', 2),
    )


if __name__ == '__main__':
    asyncio.run(main())