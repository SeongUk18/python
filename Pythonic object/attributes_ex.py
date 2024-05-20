class Base:
    def __init__(self):
        self._protected_attr = "This is a protected attribute"


class Derived(Base):
    def access_protected(self):
        return self._protected_attr


base = Base()
print(base._protected_attr)  # This is a protected attribute 가능하지만 권장되지 않음

derived = Derived()
print(derived.access_protected())  # This is a protected attribute 서브클래스에서 접근 가능


class MyClass:
    def __init__(self):
        self.__private_attr = "This is a private attribute"

    def get_private_attr(self):
        return self.__private_attr


obj = MyClass()

# print(obj.__private_attr)  # AttributeError: 'MyClass' object has no attribute '__private_attr'
print(obj.get_private_attr())  # This is a private attribute 공개 메서드를 통해 접근 가능

# 이름 맹글링을 사용하여 접근 (권장되지 않음)
print(obj._MyClass__private_attr)  # This is a private attribute 가능하지만 권장되지 않음
