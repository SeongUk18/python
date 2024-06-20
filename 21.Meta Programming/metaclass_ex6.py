class AttributeAddingMeta(type):
    def __new__(cls, name, bases, dct):
        dct['added_attr'] = 'I am an added attribute'
        return super().__new__(cls, name, bases, dct)


class MyClass(metaclass=AttributeAddingMeta):
    pass


instance = MyClass()
print(instance.added_attr)  # 출력: I am an added attribute
