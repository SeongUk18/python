class MyClass:
    __slots__ = ['x', 'y', '__dict__']

    def __init__(self, x, y):
        self.x = x
        self.y = y


obj = MyClass(1, 2)
print(obj.x)  # 1
print(obj.y)  # 2

# 동적 속성 추가
obj.z = 3
print(obj.z)  # 3
print(obj.__dict__)  # {'z': 3}
