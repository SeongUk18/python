class Parent:
    __slots__ = ['a']

    def __init__(self, a):
        self.a = a


class Child(Parent):
    __slots__ = ['b']

    def __init__(self, a, b):
        super().__init__(a)
        self.b = b


child = Child(1, 2)

print(child.a)  # 1
print(child.b)  # 2

# 새로운 속성 추가 시도
# child.c = 3  # AttributeError: 'Child' object has no attribute 'c'
