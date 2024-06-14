import asyncio
import aiohttp


async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


async def main(urls):
    tasks = [fetch(url) for url in urls]

    for future in asyncio.as_completed(tasks):
        result = await future
        print(result[:100])  # 첫 100자를 출력

urls = [
    'http://example.com',
    'http://example.org',
    'http://example.net',
]

asyncio.run(main(urls))
