from collections import UserDict


class MyUserDict(UserDict):
    def __setitem__(self, key, value):
        print(f"Setting item {key} to {value}")
        super().__setitem__(key, value)


my_user_dict = MyUserDict()
my_user_dict['a'] = 1  # "Setting item a to 1" 출력
print(my_user_dict)    # {'a': 1}

# 업데이트 시 __setitem__이 호출됨
my_user_dict.update({'b': 2, 'c': 3})  # "Setting item b to 2", "Setting item c to 3" 출력
print(my_user_dict)    # {'a': 1, 'b': 2, 'c': 3}
