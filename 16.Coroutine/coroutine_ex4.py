def exception_handling_coroutine():
    print("Coroutine started")
    try:
        while True:
            try:
                x = yield
                print(f"Received: {x}")
            except ValueError:
                print("ValueError handled")
    except GeneratorExit:
        print("Coroutine ending")


# 코루틴 생성 및 초기화
coro = exception_handling_coroutine()
next(coro)

# 코루틴에 값 보내기
coro.send(10)  # "Received: 10" 출력
coro.send(20)  # "Received: 20" 출력

# 코루틴에 예외 던지기
coro.throw(ValueError)  # "ValueError handled" 출력

# 코루틴 종료
coro.close()  # "Coroutine ending" 출력
