def function():
    return "Hello World!"

class MyClass:
    def __call__(self):
        return "Instance is callable!"

# 함수 테스트
print(callable(function))  # True

# 람다 테스트
lambda_func = lambda x: x * 2
print(callable(lambda_func))  # True

# 클래스 테스트
print(callable(MyClass))  # True

# 인스턴스 테스트
my_instance = MyClass()
print(callable(my_instance))  # True (인스턴스가 __call__ 메서드를 가지고 있기 때문)

# 일반 객체 테스트
class NotCallable:
    pass

not_callable_instance = NotCallable()
print(callable(not_callable_instance))  # False


# 사용자 정의 callable
class Adder:
    def __init__(self, value):
        self.value = value

    def __call__(self, x):
        return self.value + x

# Adder 인스턴스 생성
adder = Adder(5)

# 인스턴스를 함수처럼 사용
print(adder(10))  # 15