# 위치 매개변수
def print_values(a, b, c):
    print(f"a = {a}, b = {b}, c = {c}")

print_values(1, 2, 3)
# 출력: a = 1, b = 2, c = 3

# 키워드 매개변수
def print_values(a, b, c):
    print(f"a = {a}, b = {b}, c = {c}")

print_values(c=3, a=1, b=2)
# 출력: a = 1, b = 2, c = 3

# 기본값이 있는 매개변수
def print_values(a, b, c=3):
    print(f"a = {a}, b = {b}, c = {c}")

print_values(1, 2)
# 출력: a = 1, b = 2, c = 3

# 가변 매개변수
def print_values(*args, **kwargs):
    print(args)   # 튜플
    print(kwargs) # 딕셔너리

print_values(1, 2, 3, d=4, e=5)
# 출력: (1, 2, 3)
# 출력: {'d': 4, 'e': 5}

# 키워드 전용 매개변수
def print_values(a, *, b, c):
    print(f"a = {a}, b = {b}, c = {c}")

print_values(1, b=2, c=3)
# 출력: a = 1, b = 2, c = 3