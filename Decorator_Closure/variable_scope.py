x = 'global x'  # 전역 변수

def test():
    y = 'local y'  # 로컬 변수
    print(y)
    print(x)  # 전역 변수 x에 접근 가능

test()
# print(y)  # 에러 발생, y는 test 함수의 로컬 범위에 속함

def outer():
    z = 'outer z'  # 인클로징 변수

    def inner():
        nonlocal z
        z = 'inner z'  # outer의 z를 변경
        print(z)

    inner()
    print(z)  # 출력: 'inner z', 변경 사항이 반영됨

outer()

def change_global():
    global x
    x = 'changed global x'  # 전역 변수 x를 변경

change_global()
print(x)  # 출력: 'changed global x'