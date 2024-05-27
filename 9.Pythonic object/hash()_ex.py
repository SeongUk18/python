class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False

    def __hash__(self):
        return hash((self.x, self.y))


p1 = Point(1, 2)
p2 = Point(1, 2)
p3 = Point(2, 3)

# 집합에 추가
points = {p1, p2, p3}
print(points)  # {<__main__.Point object at 0x00000279EE5B7E20>, <__main__.Point object at 0x00000279EE5B7FD0>}

# 딕셔너리 키로 사용
point_dict = {p1: "A", p3: "B"}
print(point_dict[p2])  # A (p1과 p2는 동일한 좌표를 가지므로 동일 키로 인식)