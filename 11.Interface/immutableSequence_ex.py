class ImmutableSequence:
    def __init__(self, data):
        self._data = tuple(data)  # 불변 시퀀스를 위해 튜플 사용

    def __getitem__(self, index):
        return self._data[index]

    def __len__(self):
        return len(self._data)

    def __contains__(self, item):
        return item in self._data


immutable_seq = ImmutableSequence([1, 2, 3, 4, 5])

print(immutable_seq[2])  # 출력: 3
print(len(immutable_seq))  # 출력: 5
print(3 in immutable_seq)  # 출력: True
# immutable_seq[2] = 30  # 오류 발생: 불변 시퀀스는 항목을 설정할 수 없음
