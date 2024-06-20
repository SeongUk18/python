class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class SingletonClass(metaclass=SingletonMeta):
    def __init__(self):
        print("Instance created")


# 인스턴스 생성
singleton1 = SingletonClass()
singleton2 = SingletonClass()

# 두 인스턴스는 동일한 객체를 참조
print(singleton1 is singleton2)  # True
