# 함수를 인수로 받는 고위 함수 예제
def apply_twice(func, value):
    return func(func(value))

def add_five(x):
    return x + 5

result = apply_twice(add_five, 10)  # 20

# 함수를 반환하는 고위 함수 예제
def make_multiplier(x):
    def multiplier(n):
        return n * x
    return multiplier

double = make_multiplier(2)  # 2배를 하는 함수 생성
print(double(5))  # 결과: 10