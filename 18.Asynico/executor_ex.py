import asyncio
import concurrent.futures
import time


def blocking_io():
    print(f"start blocking_io at {time.strftime('%X')}")
    time.sleep(5)  # 블로킹 I/O 작업 (예: 파일 읽기/쓰기)
    print(f"end blocking_io at {time.strftime('%X')}")


async def main():
    loop = asyncio.get_running_loop()

    with concurrent.futures.ThreadPoolExecutor() as pool:
        # 블로킹 작업을 스레드 풀에서 실행
        await loop.run_in_executor(pool, blocking_io)

asyncio.run(main())
'''
start blocking_io at 15:56:35
end blocking_io at 15:56:40
'''