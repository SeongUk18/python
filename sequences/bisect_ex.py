import bisect

numbers = [10, 20, 30, 40, 50]

# 적절한 위치에 25 삽입
bisect.insort(numbers, 25)
print(numbers)  # 출력: [10, 20, 25, 30, 40, 50]

# 30의 삽입 위치를 찾기
position = bisect.bisect_left(numbers, 30)
print(position)  # 출력: 3

# 45를 삽입하되, 동일 값의 오른쪽에 삽입
bisect.insort_right(numbers, 40)
print(numbers)  # 출력: [10, 20, 25, 30, 40, 40, 50]
