import asyncio


async def worker():
    print("Starting worker")
    await asyncio.sleep(2)
    print("Worker done")


async def main():
    tasks = []
    for _ in range(5):
        task = asyncio.create_task(worker())
        tasks.append(task)

    await asyncio.gather(*tasks)

asyncio.run(main())
'''
Starting worker
Starting worker
Starting worker
Starting worker
Starting worker
Worker done
Worker done
Worker done
Worker done
Worker done
'''