# 상속
class Parent:
    __slots__ = ['x']

    def __init__(self, x):
        self.x = x


class Child(Parent):
    __slots__ = ['y']

    def __init__(self, x, y):
        super().__init__(x)
        self.y = y


c = Child(1, 2)
print(c.x)  # 1
print(c.y)  # 2


# 동적 속성 추가 불가
class MyClass:
    __slots__ = ['x']

    def __init__(self, x):
        self.x = x


obj = MyClass(1)
obj.x = 10  # 허용됨
# obj.y = 20  # AttributeError: 'MyClass' object has no attribute 'y'


class MyClass:
    __slots__ = ['x', '__dict__']

    def __init__(self, x):
        self.x = x


obj = MyClass(1)
obj.y = 20  # 허용됨
print(obj.y)  # 20


# 서브 클래스에서의 사용
class Parent:
    __slots__ = ['x']


class Child(Parent):
    __slots__ = ['y']


obj = Child()
obj.x = 1  # 허용됨
obj.y = 2  # 허용됨


# __weakref__와 함께 사용
import weakref


class MyClass:
    __slots__ = ['x', '__weakref__']

    def __init__(self, x):
        self.x = x


obj = MyClass(1)
weak_ref = weakref.ref(obj)
print(weak_ref())  # <__main__.MyClass object at ...>

# Pickle 지원 문제
import pickle


class MyClass:
    __slots__ = ['x']

    def __init__(self, x):
        self.x = x

    def __getstate__(self):
        return self.x

    def __setstate__(self, state):
        self.x = state


obj = MyClass(1)
data = pickle.dumps(obj)  # 직렬화
obj2 = pickle.loads(data)  # 역직렬화
print(obj2.x)  # 1