import random


class MyList:
    def __init__(self, items):
        self._items = items

    def __getitem__(self, index):
        return self._items[index]

    def __len__(self):
        return len(self._items)


# MyList 클래스의 인스턴스 생성
my_list = MyList([1, 2, 3, 4, 5])

# random.choice() 예시
print(random.choice(my_list))  # my_list 중 랜덤한 아이템 반환

# 슬라이싱 예시
sliced_list = my_list[1:4]
print(sliced_list)  # 출력: [2, 3, 4]

# reversed() 예시
for item in reversed(my_list):
    print(item, end=' ')  # 출력: 5 4 3 2 1

print()  # 줄바꿈

# sorted() 예시 - 역순으로 정렬
new_list = MyList([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
sorted_list = sorted(new_list, reverse=True)
print(sorted_list)  # 출력: [9, 6, 5, 5, 5, 4, 3, 3, 2, 1, 1]
