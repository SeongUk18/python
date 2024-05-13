# 약한 참조 생성
import weakref

class MyClass:
    def __init__(self, value):
        self.value = value

obj = MyClass(10)
r = weakref.ref(obj)

print(r())  # MyClass 인스턴스 출력
# <__main__.MyClass object at 0x000001F254B2E7F0>
del obj
print(r())  # None, obj가 가비지 컬렉션된 후
# None

# 약한 사전 (WeakKeyDictionary와 WeakValueDictionary)
import weakref

class MyClass:
    pass

obj = MyClass()
weak_dict = weakref.WeakValueDictionary()
weak_dict['primary'] = obj

print(weak_dict['primary'])  # MyClass 인스턴스 출력
del obj
print(weak_dict.get('primary'))  # None, obj가 가비지 컬렉션된 후

# 약한 집합 (WeakSet)
import weakref

class MyClass:
    pass

obj = MyClass()
weak_set = weakref.WeakSet()
weak_set.add(obj)

print(obj in weak_set)  # True
del obj
# print(obj in weak_set)  NameError: name 'obj' is not defined, obj가 가비지 컬렉션된 후