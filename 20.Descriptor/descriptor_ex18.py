class DescriptorWithDoc:
    """This is a descriptor with a docstring."""

    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name, None)

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]


class MyClass:
    attr = DescriptorWithDoc("attr")


# 사용 예
help(MyClass.attr)  # 디스크립터의 __doc__ 문자열 출력
