import asyncio


async def say_hello():
    await asyncio.sleep(1)
    print("Hello, World!")


async def main():
    task1 = asyncio.create_task(say_hello())
    task2 = asyncio.create_task(say_hello())

    await task1
    await task2

asyncio.run(main())
