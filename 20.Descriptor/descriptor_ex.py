class MyDescriptor:
    def __get__(self, instance, owner):
        return instance._value

    def __set__(self, instance, value):
        instance._value = value

    def __delete__(self, instance):
        del instance._value


class MyClass:
    descriptor = MyDescriptor()


# 사용 예
obj = MyClass()
obj.descriptor = 10  # __set__ 호출
print(obj.descriptor)  # __get__ 호출, 10 출력
del obj.descriptor  # __delete__ 호출
