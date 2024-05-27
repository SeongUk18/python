class MyList:
    def __init__(self, items):
        self._items = items

    # 클래스의 인스턴스에서 [] 연산자를 사용할 때 호출
    def __getitem__(self, index):
        return self._items[index]

    # 클래스의 인스턴스에 대해 len() 함수가 호출될 때 사용
    def __len__(self):
        return len(self._items)


# MyList 클래스의 인스턴스 생성
my_list = MyList([1, 2, 3, 4, 5])

# __getitem__ 메소드를 통해 특정 인덱스의 아이템 접근
print(my_list[2])  # 출력: 3

# __len__ 메소드를 통해 리스트의 길이 구하기
print(len(my_list))  # 출력: 5
