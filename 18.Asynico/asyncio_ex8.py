import asyncio


async def fetch_data(id):
    print(f"Fetching data for {id}...")
    await asyncio.sleep(1)
    print(f"Data for {id} fetched!")
    return f"Data {id}"


async def main():
    tasks = [asyncio.create_task(fetch_data(i)) for i in range(5)]
    results = await asyncio.gather(*tasks)
    print("All data fetched:", results)

asyncio.run(main())

'''
Fetching data for 0...
Fetching data for 1...
Fetching data for 2...
Fetching data for 3...
Fetching data for 4...
Data for 0 fetched!
Data for 2 fetched!
Data for 4 fetched!
Data for 1 fetched!
Data for 3 fetched!
All data fetched: ['Data 0', 'Data 1', 'Data 2', 'Data 3', 'Data 4']
'''