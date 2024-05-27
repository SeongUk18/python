def outer():
    x = 10  # outer 함수의 로컬 변수

    def inner():
        return x  # x는 여기에서 자유변수

    return inner

my_func = outer()
print(my_func())  # 출력: 10