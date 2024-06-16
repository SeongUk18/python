class MyClass:
    def __init__(self, value):
        self.value = value


obj = MyClass(10)
print(getattr(obj, 'value'))  # 10
print(getattr(obj, 'nonexistent', 'default'))  # default


class MyClass:
    pass


obj = MyClass()
setattr(obj, 'value', 10)
print(obj.value)  # 10


class MyClass:
    def __init__(self, value):
        self.value = value


obj = MyClass(10)
delattr(obj, 'value')
# print(obj.value)  # AttributeError: 'MyClass' object has no attribute 'value'


class MyClass:
    def __init__(self, value):
        self.value = value


obj = MyClass(10)
print(hasattr(obj, 'value'))  # True
print(hasattr(obj, 'nonexistent'))  # False
