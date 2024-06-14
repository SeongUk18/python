import asyncio


async def my_coroutine():
    await asyncio.sleep(1)
    print("Hello, asyncio!")


async def main():
    try:
        await asyncio.wait_for(my_coroutine(), timeout=0.5)
    except asyncio.TimeoutError:
        print("Timed out!")

asyncio.run(main())