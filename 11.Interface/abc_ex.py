from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

    @abstractmethod
    def move(self):
        pass


class Dog(Animal):
    def sound(self):
        return "Bark"

    def move(self):
        return "Run"


class Cat(Animal):
    def sound(self):
        return "Meow"

    def move(self):
        return "Jump"


dog = Dog()
cat = Cat()

print(dog.sound())  # 출력: Bark
print(dog.move())   # 출력: Run

print(cat.sound())  # 출력: Meow
print(cat.move())   # 출력: Jump

# animal = Animal()  # TypeError: Can't instantiate abstract class Animal with abstract methods move, sound
