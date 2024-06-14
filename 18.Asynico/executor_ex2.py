import asyncio
import concurrent.futures
import time


def cpu_bound():
    print(f"start cpu_bound at {time.strftime('%X')}")
    count = 0
    for _ in range(10**7):
        count += 1  # CPU 바운드 작업
    print(f"end cpu_bound at {time.strftime('%X')}")
    return count


async def main():
    loop = asyncio.get_running_loop()

    with concurrent.futures.ProcessPoolExecutor() as pool:
        # CPU 바운드 작업을 프로세스 풀에서 실행
        result = await loop.run_in_executor(pool, cpu_bound)
        print(f"Result: {result}")

asyncio.run(main())
