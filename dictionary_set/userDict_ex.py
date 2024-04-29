from collections import UserDict


class MyDict(UserDict):
    def __init__(self, initial_data={}):
        super().__init__(initial_data)

    # 예제: 값을 설정할 때 항상 문자열로 변환하는 기능 추가
    def __setitem__(self, key, value):
        super().__setitem__(key, str(value))

    # 키가 없는 경우에 대한 처리 추가
    def __missing__(self, key):
        return f"{key} not found!"


# MyDict 인스턴스 생성 및 사용
my_dict = MyDict()
my_dict['alpha'] = 123
print(my_dict['alpha'])  # 출력: '123'
print(my_dict['beta'])  # 출력: 'beta not found!'