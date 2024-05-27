class Duck:
    def fly(self):
        print("Duck is flying")


class Goose:
    def fly(self):
        print("Goose is flying")


class Penguin:
    def swim(self):
        print("Penguin is swimming")


def let_it_fly(bird):
    bird.fly()


duck = Duck()
goose = Goose()
penguin = Penguin()

let_it_fly(duck)   # 출력: Duck is flying
let_it_fly(goose)  # 출력: Goose is flying
# let_it_fly(penguin)  # 오류 발생: AttributeError: 'Penguin' object has no attribute 'fly'
