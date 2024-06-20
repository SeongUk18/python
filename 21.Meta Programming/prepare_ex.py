class MyMeta(type):
    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        print("Preparing namespace")
        return {}


class MyClass(metaclass=MyMeta):
    pass

