from abc import ABC, abstractmethod


class MyABC(ABC):
    @abstractmethod
    def my_method(self):
        pass

    @classmethod
    def __subclasshook__(cls, subclass):
        if cls is MyABC:
            if any("my_method" in B.__dict__ for B in subclass.__mro__):
                return True
        return NotImplemented


class A:
    def my_method(self):
        pass


class B:
    pass


print(issubclass(A, MyABC))  # 출력: True (A 클래스는 my_method를 가지고 있음)
print(issubclass(B, MyABC))  # 출력: False (B 클래스는 my_method를 가지고 있지 않음)
