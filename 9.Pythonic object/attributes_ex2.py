class MyClass:
    def __init__(self):
        self._protected_attr = "This is a protected attribute"

    def _protected_method(self):
        return "This is a protected method"


# 외부 접근 (권장되지 않음)
obj = MyClass()
print(obj._protected_attr) # This is a protected attribute
print(obj._protected_method()) # This is a protected attribute


class MyClass2:
    def __init__(self):
        self.__private_attr = "This is a private attribute"

    def get_private_attr(self):
        return self.__private_attr


# 공개 메서드를 통해 접근
obj2 = MyClass2()
print(obj2.get_private_attr()) # This is a private attribute

# 이름 맹글링을 통해 접근 (권장되지 않음)
print(obj2._MyClass2__private_attr) # This is a private attribute
