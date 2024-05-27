from typing import Protocol


class Flyable(Protocol):
    def fly(self):
        ...


class Duck:
    def fly(self):
        print("Duck is flying")


class Goose:
    def fly(self):
        print("Goose is flying")


def let_it_fly(bird: Flyable):
    bird.fly()


duck = Duck()
goose = Goose()

let_it_fly(duck)   # 출력: Duck is flying
let_it_fly(goose)  # 출력: Goose is flying
