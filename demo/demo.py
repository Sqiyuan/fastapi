import asyncio
from utils.utils import async_timed
 
# 类似于 async_timed(main())
@async_timed
async def main():
    print('Hello ...')
    await asyncio.sleep(1)
    print('... World!')

if  __name__ == '__main__':
    asyncio.run(main())




    