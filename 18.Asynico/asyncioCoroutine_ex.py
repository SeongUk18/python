import asyncio


# 예전 방식
@asyncio.coroutine
def my_coroutine():
    yield from asyncio.sleep(1)
    print("Hello, asyncio!")


loop = asyncio.get_event_loop()
loop.run_until_complete(my_coroutine())
loop.close()


# 변경된 방식
async def my_coroutine():
    await asyncio.sleep(1)
    print("Hello, asyncio!")

asyncio.run(my_coroutine())
