def coroutine(func):
    def wrapper(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)  # 코루틴 초기화
        return gen
    return wrapper


@coroutine
def accumulator():
    total = 0
    while True:
        value = yield total
        if value is None:
            break
        total += value


# 코루틴 생성 및 초기화
acc = accumulator()

# 코루틴에 값 보내기
print(acc.send(10))  # 출력: 10
print(acc.send(20))  # 출력: 30
print(acc.send(5))   # 출력: 35

# 코루틴 종료
acc.send(None)
