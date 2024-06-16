class MyClass:
    def __init__(self, value):
        self.value = value


obj = MyClass(10)
print(obj.__dict__)  # {'value': 10}


class MyClass:
    __slots__ = ['value']

    def __init__(self, value):
        self.value = value


obj = MyClass(10)
print(obj.value)  # 10
# print(obj.__dict__)  # AttributeError: 'MyClass' object has no attribute '__dict__'
