class MyClass:
    def __init__(self):
        self.__private_attr = "This is a private attribute"

    def get_private_attr(self):
        return self.__private_attr

    def __private_method(self):
        return "This is a private method"

    def call_private_method(self):
        return self.__private_method()


obj = MyClass()

# 직접 접근 시도
# print(obj.__private_attr)  # AttributeError: 'MyClass' object has no attribute '__private_attr'
# print(obj.__private_method())  # AttributeError: 'MyClass' object has no attribute '__private_method'

# 공개 메서드를 통해 접근
print(obj.get_private_attr())  # This is a private attribute
print(obj.call_private_method())  # This is a private method

# 이름 장식을 통해 접근 (권장되지 않음)
print(obj._MyClass__private_attr)  # This is a private attribute
print(obj._MyClass__private_method())  # This is a private method