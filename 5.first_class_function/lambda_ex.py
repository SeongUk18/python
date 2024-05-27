# 간단한 연산
# 두 수를 더하는 람다 함수
add = lambda x, y: x + y
print(add(5, 3))  # 8

# 리스트 정렬
# 이름을 성으로 정렬하기
names = ['John Doe', 'Jane Smith', 'Alice Johnson']
sorted_names = sorted(names, key=lambda name: name.split()[-1])
print(sorted_names)  # ['John Doe', 'Alice Johnson', 'Jane Smith']

# map() 함수 사용
# 각 숫자의 제곱 계산
numbers = [1, 2, 3, 4, 5]
squared = map(lambda x: x ** 2, numbers)
print(list(squared))  # [1, 4, 9, 16, 25]

# filter() 함수 사용
# 홀수만 필터링
numbers = [1, 2, 3, 4, 5]
odds = filter(lambda x: x % 2 != 0, numbers)
print(list(odds))  # [1, 3, 5]

# reduce() 함수 사용
from functools import reduce
numbers = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, numbers)
print(product)  # 24