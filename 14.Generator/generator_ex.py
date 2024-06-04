def my_generator():
    yield 1
    yield 2
    yield 3


gen = my_generator()  # 제너레이터 객체 생성

print(next(gen))  # 출력: 1
print(next(gen))  # 출력: 2
print(next(gen))  # 출력: 3
# print(next(gen))  # StopIteration 예외 발생
