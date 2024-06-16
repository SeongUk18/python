class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = None
        self.age = age  # 초기화 시 검증을 위해 setter를 사용

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not (0 <= value <= 120):
            raise ValueError("Age must be between 0 and 120")
        self._age = value


# 올바른 나이 설정
try:
    person1 = Person("Alice", 30)
    print(f"{person1.name}의 나이: {person1.age}")  # 출력: Alice의 나이: 30
except ValueError as e:
    print(e)

# 잘못된 나이 설정
try:
    person2 = Person("Bob", 150)
except ValueError as e:
    print(e)  # 출력: Age must be between 0 and 120

# 나이 값 변경
try:
    person1.age = 25
    print(f"{person1.name}의 변경된 나이: {person1.age}")  # 출력: Alice의 변경된 나이: 25
    person1.age = -10  # 이 줄은 예외를 발생시킨다.
except ValueError as e:
    print(e)  # 출력: Age must be between 0 and 120
