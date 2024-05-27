# 객체의 메소드 호출하기
from operator import methodcaller

class Person:
    def __init__(self, name):
        self.name = name

    def greet(self, greeting):
        return f"{greeting}, {self.name}!"

person = Person("John")
say_hello = methodcaller('greet', 'Hello')
print(say_hello(person))  # 출력: Hello, John!

# 고급 사용법: 여러 인자 전달
class Calculator:
    def multiply(self, a, b):
        return a * b

calc = Calculator()
get_product = methodcaller('multiply', 10, 5)
print(get_product(calc))  # 출력: 50

# 리스트의 객체들에 대해 메소드 호출하기
people = [Person("Alice"), Person("Bob"), Person("Charlie")]
greetings = list(map(methodcaller('greet', 'Hi'), people))
print(greetings)  # 출력: ['Hi, Alice!', 'Hi, Bob!', 'Hi, Charlie!']

# 중첩 메소드 호출
# 이 예제는 `methodcaller`의 단순 사용 예시이며, 실제 체인 호출을 위해서는 추가적인 로직이 필요할 수 있다.
getter = methodcaller('get', 'key')
print(getter({"key": "value"}))  # 출력: value