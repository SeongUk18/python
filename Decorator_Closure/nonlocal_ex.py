def outer():
    count = 0

    def inner():
        nonlocal count  # 바깥쪽 함수의 변수 count를 참조
        count += 1
        return count

    return inner

counter = outer()
print(counter())  # 출력: 1
print(counter())  # 출력: 2
print(counter())  # 출력: 3