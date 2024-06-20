from collections import OrderedDict


class Descriptor:
    def __init__(self, name=None):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        print(f"Getting {self.name}")
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        print(f"Setting {self.name} to {value}")
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        print(f"Deleting {self.name}")
        del instance.__dict__[self.name]


class CustomMeta(type):
    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        return OrderedDict()

    def __new__(cls, name, bases, classdict):
        for key, value in classdict.items():
            if isinstance(value, Descriptor):
                value.name = key
        return super().__new__(cls, name, bases, classdict)


class MyClass(metaclass=CustomMeta):
    attr1 = Descriptor()
    attr2 = Descriptor()


instance = MyClass()
instance.attr1 = 10  # 출력: Setting attr1 to 10
print(instance.attr1)  # 출력: Getting attr1, 10
