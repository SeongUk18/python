class MyClass:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if new_value > 0:
            self._value = new_value
        else:
            raise ValueError("Value must be > 0")


# 사용 예
obj = MyClass(10)
print(obj.value)  # 10 출력
obj.value = 20
print(obj.value)  # 20 출력
try:
    obj.value = -5  # ValueError 발생
except ValueError as e:
    print(e)  # "Value must be > 0" 출력
