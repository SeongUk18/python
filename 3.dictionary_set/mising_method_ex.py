class CustomDict(dict):
    def __missing__(self, key):
        # 존재하지 않는 키에 대한 처리
        return f"{key} is not in the dictionary"

# CustomDict 인스턴스 생성
my_dict = CustomDict({'a': 1, 'b': 2})

# 존재하는 키
print(my_dict['a'])  # 출력: 1

# 존재하지 않는 키
print(my_dict['c'])  # 출력: c is not in the dictionary