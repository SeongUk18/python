class ReadOnlyDescriptor:
    def __init__(self, value):
        self._value = value

    def __get__(self, instance, owner):
        return self._value

    def __set__(self, instance, value):
        raise AttributeError("This attribute is read-only")


class MyClass:
    attr = ReadOnlyDescriptor(10)


# 사용 예
obj = MyClass()
print(obj.attr)  # 10 출력
try:
    obj.attr = 20  # AttributeError 발생
except AttributeError as e:
    print(e)  # "This attribute is read-only" 출력
