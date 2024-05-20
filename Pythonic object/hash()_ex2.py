class ImmutableList:
    def __init__(self, items):
        self._items = tuple(items)  # 불변 튜플로 변환

    def __eq__(self, other):
        if isinstance(other, ImmutableList):
            return self._items == other._items
        return False

    def __hash__(self):
        return hash(self._items)


list1 = ImmutableList([1, 2, 3])
list2 = ImmutableList([1, 2, 3])
list3 = ImmutableList([4, 5, 6])

# 집합에 추가
lists = {list1, list2, list3}
print(lists)  # {<__main__.ImmutableList object at 0x000001A9EB827FD0>, <__main__.ImmutableList object at 0x000001A9EB827970>}

# 딕셔너리 키로 사용
list_dict = {list1: "A", list3: "B"}
print(list_dict[list2])  # A (list1과 list2는 동일한 요소를 가지므로 동일 키로 인식)