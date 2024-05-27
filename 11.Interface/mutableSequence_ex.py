from collections.abc import MutableSequence


class MyList(MutableSequence):
    def __init__(self, data=None):
        self._data = list(data) if data is not None else []

    def __getitem__(self, index):
        return self._data[index]

    def __setitem__(self, index, value):
        self._data[index] = value

    def __delitem__(self, index):
        del self._data[index]

    def __len__(self):
        return len(self._data)

    def insert(self, index, value):
        self._data.insert(index, value)

    def __str__(self):
        return f"{self._data}"


my_list = MyList([1, 2, 3])
print(my_list)  # 출력: [1, 2, 3]

my_list.append(4)
print(my_list)  # 출력: [1, 2, 3, 4]

my_list[1] = 10
print(my_list)  # 출력: [1, 10, 3, 4]

del my_list[2]
print(my_list)  # 출력: [1, 10, 4]

print(len(my_list))  # 출력: 3
