import asyncio


async def my_coroutine():
    print("Hello")
    await asyncio.sleep(1)  # 비동기적으로 1초 대기
    print("World")

# 코루틴 실행
asyncio.run(my_coroutine())
