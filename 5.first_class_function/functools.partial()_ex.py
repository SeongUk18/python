# 함수 인자 일부 적용
from functools import partial

def multiply(x, y):
    return x * y

# 첫 번째 인자 x를 2로 고정
double = partial(multiply, 2)

# double 함수 사용
print(double(5))  # 10

# 고급 사용법: 키워드 인자 사용
def greet(greeting, name):
    return f"{greeting}, {name}!"

# 인사말을 'Hello'로 고정
say_hello = partial(greet, greeting='Hello')

# say_hello 함수 사용
print(say_hello(name="Alice"))  # Hello, Alice!

# 고차 함수와 함께 사용
# 여러 숫자에 대해 특정 숫자를 더하는 함수
add_numbers = partial(sum, [10, 20, 30])

# 추가 인자 없이 사용
print(add_numbers())  # 60