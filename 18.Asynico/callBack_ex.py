import asyncio


def callback1(future):
    print("Callback 1")
    future2 = asyncio.Future()
    future2.add_done_callback(callback2)
    loop = asyncio.get_running_loop()
    loop.call_later(1, future2.set_result, "Result 2")


def callback2(future):
    print("Callback 2")
    future3 = asyncio.Future()
    future3.add_done_callback(callback3)
    loop = asyncio.get_running_loop()
    loop.call_later(1, future3.set_result, "Result 3")


def callback3(future):
    print("Callback 3")
    print(future.result())


async def main():
    future1 = asyncio.Future()
    future1.add_done_callback(callback1)
    loop = asyncio.get_running_loop()
    loop.call_later(1, future1.set_result, "Result 1")
    await asyncio.sleep(3)  # 이벤트 루프가 콜백을 실행할 시간을 주기 위해 대기

asyncio.run(main())
'''
Callback 1
Callback 2
Callback 3
Result 3
'''