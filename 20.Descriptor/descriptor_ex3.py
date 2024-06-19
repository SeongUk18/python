class OverridingDescriptor:
    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name, None)

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name


class MyClass:
    attr = OverridingDescriptor()


obj = MyClass()
obj.attr = 10  # __set__ 호출
print(obj.attr)  # __get__ 호출, 10 출력
