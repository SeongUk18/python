import weakref


class MyClass:
    __slots__ = ['x', 'y', '__dict__', '__weakref__']

    def __init__(self, x, y):
        self.x = x
        self.y = y


obj = MyClass(1, 2)

# 동적 속성 추가
obj.z = 3
print(obj.z)  # 3
print(obj.__dict__)  # {'z': 3}

# 약한 참조
weak_ref = weakref.ref(obj)
print(weak_ref)  # <weakref at ...; to 'MyClass' at ...>
print(weak_ref())  # <__main__.MyClass object at ...>

del obj  # 원본 객체 삭제
print(weak_ref())  # None (원본 객체가 삭제되었기 때문에 약한 참조도 사라짐)