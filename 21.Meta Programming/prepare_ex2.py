from collections import OrderedDict


class OrderedMeta(type):
    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        return OrderedDict()

    def __new__(cls, name, bases, classdict):
        classdict['ordered'] = [key for key in classdict.keys() if not key.startswith('__')]
        return super().__new__(cls, name, bases, classdict)


class MyClass(metaclass=OrderedMeta):
    x = 1
    y = 2


print(MyClass.ordered)  # 출력: ['x', 'y']
