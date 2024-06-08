def simple_generator():
    yield 1
    yield 2
    yield 3


gen = simple_generator()

print(next(gen))  # 1 출력
print(next(gen))  # 2 출력
print(next(gen))  # 3 출력
