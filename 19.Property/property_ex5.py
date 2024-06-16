class MyClass:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if value < 0:
            raise ValueError("Value must be non-negative")
        self._value = value

    @value.deleter
    def value(self):
        del self._value


# 예제 사용
obj = MyClass(10)
print(obj.value)  # 10

obj.value = 20
print(obj.value)  # 20

try:
    obj.value = -10
except ValueError as e:
    print(e)  # Value must be non-negative

del obj.value
