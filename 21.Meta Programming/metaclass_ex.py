class MyMeta(type):
    def __new__(cls, name, bases, dct):
        print(f"Creating class {name}")
        return super().__new__(cls, name, bases, dct)

    def __init__(cls, name, bases, dct):
        print(f"Initializing class {name}")
        super().__init__(name, bases, dct)


class MyClass(metaclass=MyMeta):
    def __init__(self):
        print("Instance of MyClass created")

# 클래스 생성 시 출력
# Creating class MyClass
# Initializing class MyClass


# 인스턴스 생성 시 출력
instance = MyClass()
# Instance of MyClass created
