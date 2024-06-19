class PositiveValue:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if value > 0:
            instance.__dict__[self.name] = value
        else:
            raise ValueError(f"{self.name} must be > 0")


class MyClass:
    value = PositiveValue("value")


# 사용 예
obj = MyClass()
obj.value = 10
print(obj.value)  # 10 출력
try:
    obj.value = -5  # ValueError 발생
except ValueError as e:
    print(e)  # "value must be > 0" 출력
