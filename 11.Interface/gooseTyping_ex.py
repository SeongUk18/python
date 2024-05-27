from typing import Protocol


class Quackable(Protocol):
    def quack(self) -> None:
        ...


class Flyable(Protocol):
    def fly(self) -> None:
        ...


class Duck:
    def quack(self) -> None:
        print("Quack")

    def fly(self) -> None:
        print("Fly")


class Goose:
    def quack(self) -> None:
        print("Honk")

    def fly(self) -> None:
        print("Fly")


def let_it_quack(animal: Quackable) -> None:
    animal.quack()


def let_it_fly(animal: Flyable) -> None:
    animal.fly()


duck = Duck()
goose = Goose()

let_it_quack(duck)   # 출력: Quack
let_it_quack(goose)  # 출력: Honk

let_it_fly(duck)     # 출력: Fly
let_it_fly(goose)    # 출력: Fly
