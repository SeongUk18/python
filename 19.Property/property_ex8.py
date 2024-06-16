class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age must be non-negative")
        self._age = value

    @age.deleter
    def age(self):
        print(f"Deleting age of {self._name}")
        del self._age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @name.deleter
    def name(self):
        print(f"Deleting name of person with age {self._age}")
        del self._name


# 객체 생성
person = Person("Alice", 30)

# 속성 접근 및 설정
print(person.age)  # 30
person.age = 25
print(person.age)  # 25

# 속성 삭제
del person.age
# 출력: Deleting age of Alice

try:
    print(person.age)
except AttributeError as e:
    print(e)  # 'Person' object has no attribute '_age'

# 이름 속성 삭제
del person.name
# AttributeError: 'Person' object has no attribute '_age'
