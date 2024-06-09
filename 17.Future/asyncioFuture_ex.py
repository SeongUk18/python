import asyncio


async def main():
    future = asyncio.Future()

    async def set_future():
        await asyncio.sleep(1)
        future.set_result('Completed')

    asyncio.create_task(set_future())

    result = await future
    print(result)  # Output: Completed

asyncio.run(main())
