def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


fib = fibonacci()
for _ in range(10):
    print(next(fib))  # 첫 10개의 피보나치 수 출력
