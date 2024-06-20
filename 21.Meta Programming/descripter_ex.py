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


def add_descriptor(cls):
    for key, value in cls.__dict__.items():
        if isinstance(value, Descriptor):
            value.name = key
    return cls


@add_descriptor
class MyClass:
    attr1 = Descriptor()
    attr2 = Descriptor()


# 인스턴스 생성
instance = MyClass()

# 속성 설정
instance.attr1 = 10  # 출력: Setting attr1 to 10
instance.attr2 = 20  # 출력: Setting attr2 to 20

# 속성 접근
print(instance.attr1)  # 출력: Getting attr1, 10
print(instance.attr2)  # 출력: Getting attr2, 20

# 속성 삭제
del instance.attr1  # 출력: Deleting attr1
