from abc import ABCMeta


class MyABC(metaclass=ABCMeta):
    def __subclasscheck__(cls, subclass):
        # 사용자 정의 서브클래스 체크 로직
        return hasattr(subclass, 'my_method')


class A:
    def my_method(self):
        pass


# 클래스 등록
MyABC.register(A)


class B:
    pass


print(issubclass(A, MyABC))  # 출력: True (A 클래스는 my_method를 가지고 있음)
print(issubclass(B, MyABC))  # 출력: False (B 클래스는 my_method를 가지고 있지 않음)

