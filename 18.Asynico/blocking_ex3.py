import aiohttp
import asyncio


async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


async def main():
    result = await fetch('http://example.com')
    print(result)

asyncio.run(main())
