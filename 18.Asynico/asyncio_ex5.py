import asyncio


async def set_after(future):
    await asyncio.sleep(1)
    future.set_result("Completed")

async def main():
    future = asyncio.Future()
    await set_after(future)
    print(future.result())

asyncio.run(main())
