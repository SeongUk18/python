import random


def random_gen():
    return random.randint(0, 10)


random_iter = iter(random_gen, 5)
for num in random_iter:
    print(num)  # 5가 반환되면 반복 종료
