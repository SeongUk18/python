from abc import ABC, abstractmethod


# 인터페이스 상속
class MyInterface(ABC):
    @abstractmethod
    def do_something(self):
        pass


# 구현 상속
class MyBaseClass:
    def do_something(self):
        print("Doing something in MyBaseClass")


class MyClass(MyBaseClass, MyInterface):
    pass

# MyClass는 MyBaseClass의 구현을 상속받고, MyInterface의 계약을 준수한다.
