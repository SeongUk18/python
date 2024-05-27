from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

    def describe(self):
        return "This is an animal."


class Dog(Animal):
    def sound(self):
        return "Bark"


dog = Dog()
print(dog.describe())  # 출력: This is an animal.
print(dog.sound())     # 출력: Bark


