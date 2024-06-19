class DescriptorWithSetName:
    def __init__(self, name=None):
        self.name = name

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name, None)

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]


class MyClass:
    attr = DescriptorWithSetName()


# 사용 예
obj = MyClass()
obj.attr = 10
print(obj.attr)  # 10 출력
del obj.attr
print(obj.attr)  # None 출력
