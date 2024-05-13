# del
x = [1, 2, 3]
y = x
del x  # x에 대한 참조를 제거하지만, y가 여전히 리스트 [1, 2, 3]을 참조하고 있으므로 리스트는 메모리에 남아 있다.

# Garbage Collection
import gc

class A:
    def __init__(self, b_instance):
        self.b = b_instance

class B:
    def __init__(self, a_instance):
        self.a = a_instance

gc.enable()  # 가비지 컬렉션 활성화

a = A(None)
b = B(a)
a.b = b

del a
del b

gc.collect()  # 가비지 컬렉터를 강제로 호출하여 순환 참조를 제거