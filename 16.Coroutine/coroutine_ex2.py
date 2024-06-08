def coroutine(func):
    def wrapper(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)  # 코루틴 초기화
        return gen
    return wrapper


@coroutine
def simple_coroutine():
    print("Coroutine started")
    while True:
        x = yield
        print(f"Received: {x}")


# 코루틴 생성 및 초기화가 자동으로 수행됨
coro = simple_coroutine()

# 코루틴에 값 보내기
coro.send(10)  # "Received: 10" 출력
coro.send(20)  # "Received: 20" 출력
