import asyncio
import concurrent.futures
import time


def cpu_bound_task():
    time.sleep(5)
    return "CPU-bound task completed"


async def main():
    loop = asyncio.get_running_loop()
    with concurrent.futures.ProcessPoolExecutor() as pool:
        result = await loop.run_in_executor(pool, cpu_bound_task)
        print(result)

asyncio.run(main())
