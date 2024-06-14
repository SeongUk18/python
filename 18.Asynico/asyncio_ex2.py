from aiohttp import web
import asyncio


async def handle(request):
    await asyncio.sleep(1)
    return web.Response(text="Hello, World!")

app = web.Application()
app.add_routes([web.get('/', handle)])

web.run_app(app)
