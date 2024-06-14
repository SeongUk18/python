import aiohttp
import asyncio


async def download_file(semaphore, session, url, file_path):
    async with semaphore:
        async with session.get(url) as response:
            response.raise_for_status()
            with open(file_path, 'wb') as f:
                while True:
                    chunk = await response.content.read(1024)
                    if not chunk:
                        break
                    f.write(chunk)
            print(f"Downloaded {file_path}")


async def main(urls, file_paths, max_concurrent_downloads):
    semaphore = asyncio.Semaphore(max_concurrent_downloads)
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url, file_path in zip(urls, file_paths):
            task = asyncio.create_task(download_file(semaphore, session, url, file_path))
            tasks.append(task)
        await asyncio.gather(*tasks)

# 다운로드할 URL 목록과 저장할 파일 경로 목록
urls = [
    'http://example.com/file1.txt',
    'http://example.com/file2.txt',
    'http://example.com/file3.txt',
]

file_paths = [
    'file1.txt',
    'file2.txt',
    'file3.txt',
]

# 비동기 다운로드 실행
asyncio.run(main(urls, file_paths))
