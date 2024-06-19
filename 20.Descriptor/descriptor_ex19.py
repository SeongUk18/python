class ManagedAttribute:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name, None)

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        print(f"Deleting {self.name}")
        del instance.__dict__[self.name]


class MyClass:
    attr = ManagedAttribute("attr")


# 사용 예
obj = MyClass()
obj.attr = 10
print(obj.attr)  # 10 출력
del obj.attr  # "Deleting attr" 출력
try:
    print(obj.attr)  # None 출력
except AttributeError as e:
    print(e)
