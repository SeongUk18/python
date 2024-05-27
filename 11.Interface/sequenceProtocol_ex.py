class MySequence:
    def __init__(self, data):
        self._data = data

    def __getitem__(self, index):
        return self._data[index]

    def __len__(self):
        return len(self._data)

    def __setitem__(self, index, value):
        self._data[index] = value

    def __delitem__(self, index):
        del self._data[index]

    def __contains__(self, item):
        return item in self._data


seq = MySequence([1, 2, 3, 4, 5])

print(seq[2])  # 출력: 3
print(len(seq))  # 출력: 5
seq[2] = 30
print(seq[2])  # 출력: 30
del seq[2]
print(len(seq))  # 출력: 4
print(30 in seq)  # 출력: False
