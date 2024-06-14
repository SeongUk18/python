import asyncio


async def main():
    print("Callback 1")
    await asyncio.sleep(1)

    print("Callback 2")
    await asyncio.sleep(1)

    print("Callback 3")
    result = "Result 3"
    print(result)

asyncio.run(main())
'''
Callback 1
Callback 2
Callback 3
Result 3
'''