class MyClass:
    def __getattr__(self, name):
        return f"Attribute {name} not found"


obj = MyClass()
print(obj.nonexistent)  # Attribute nonexistent not found


class MyClass:
    def __setattr__(self, name, value):
        print(f"Setting {name} to {value}")
        super().__setattr__(name, value)


obj = MyClass()
obj.value = 10  # Setting value to 10
print(obj.value)  # 10


class MyClass:
    def __init__(self, value):
        self.value = value

    def __delattr__(self, name):
        print(f"Deleting {name}")
        super().__delattr__(name)


obj = MyClass(10)
del obj.value  # Deleting value
# print(obj.value)  # AttributeError: 'MyClass' object has no attribute 'value'


class MyClass:
    def __dir__(self):
        return ['custom_attr', 'another_attr']


obj = MyClass()
print(dir(obj))  # ['another_attr', 'custom_attr']
