from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass


class Fish:
    def sound(self):
        return "Blub"


# Fish를 Animal의 가상 서브클래스로 등록
Animal.register(Fish)

print(issubclass(Fish, Animal))  # 출력: True

fish = Fish()
print(isinstance(fish, Animal))  # 출력: True
