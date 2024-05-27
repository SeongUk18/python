class MyClass:
    count = 0

    def __init__(self):
        MyClass.count += 1

    @classmethod
    def get_count(cls):
        return cls.count


obj1 = MyClass()
obj2 = MyClass()
print(MyClass.get_count()) # 2


class MyClass2:
    @staticmethod
    def is_even(number):
        return number % 2 == 0


print(MyClass2.is_even(4)) # True
print(MyClass2.is_even(5)) # False