class MyMeta(type):
    def __new__(cls, name, bases, dct):
        print(f"Creating class {name}")
        return super().__new__(cls, name, bases, dct)


def class_decorator(cls):
    print(f"Decorating class {cls.__name__}")
    cls.decorated = True
    return cls


@class_decorator
class MyClass(metaclass=MyMeta):
    def __init__(self):
        print("MyClass instance created")

    def method(self):
        print("Method in MyClass")


print("Before creating MyClass instance")
instance = MyClass()
print("After creating MyClass instance")
print(f"MyClass is decorated: {hasattr(MyClass, 'decorated')}")

'''
Decorating class MyClass
Creating class MyClass
Before creating MyClass instance
MyClass instance created
After creating MyClass instance
MyClass is decorated: True
'''