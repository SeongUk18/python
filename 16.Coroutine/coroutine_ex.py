def simple_coroutine():
    print("Coroutine started")
    x = yield
    print(f"Received: {x}")
    y = yield x + 1
    print(f"Received: {y}")
    yield y + 1


# 코루틴 객체 생성 (Created 상태)
coro = simple_coroutine()

# 코루틴 실행 시작 (Running 상태)
print(next(coro))  # "Coroutine started" 출력, 첫 번째 yield에서 중단 (Suspended 상태)

# 코루틴 재개 (Running 상태)
print(coro.send(10))  # "Received: 10" 출력, 두 번째 yield에서 중단 (Suspended 상태)

# 코루틴 재개 (Running 상태)
print(coro.send(20))  # "Received: 20" 출력, 세 번째 yield에서 중단 (Suspended 상태)

# 코루틴 종료 (Closed 상태)
coro.close()
