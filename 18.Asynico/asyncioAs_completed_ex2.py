import asyncio


async def my_task(id):
    await asyncio.sleep(id)
    return f"Task {id} completed"


async def main():
    tasks = [my_task(i) for i in range(5)]

    for future in asyncio.as_completed(tasks):
        result = await future
        print(result)

asyncio.run(main())
'''
Task 0 completed
Task 1 completed
Task 2 completed
Task 3 completed
Task 4 completed
'''