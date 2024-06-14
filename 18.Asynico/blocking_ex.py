import asyncio
import concurrent.futures
import time


def blocking_task():
    time.sleep(5)
    return "Blocking task completed"


async def main():
    loop = asyncio.get_running_loop()
    with concurrent.futures.ThreadPoolExecutor() as pool:
        result = await loop.run_in_executor(pool, blocking_task)
        print(result)

asyncio.run(main())
