class MyDict(dict):
    def __setitem__(self, key, value):
        print(f"Setting item {key} to {value}")
        super().__setitem__(key, value)


my_dict = MyDict()
my_dict['a'] = 1  # "Setting item a to 1" 출력
print(my_dict)    # {'a': 1}

# 업데이트 시 __setitem__이 호출되지 않음
my_dict.update({'b': 2, 'c': 3})  # 출력 없음
print(my_dict)    # {'a': 1, 'b': 2, 'c': 3}
