class MyClass:
    __slots__ = ['x', 'y']

    def __init__(self, x, y):
        self.x = x
        self.y = y


obj = MyClass(1, 2)

print(obj.x)  # 1
print(obj.y)  # 2

# 새로운 속성 추가 시도
# obj.z = 3  # AttributeError: 'MyClass' object has no attribute 'z'
