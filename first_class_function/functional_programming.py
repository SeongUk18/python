# map
numbers = [1, 2, 3, 4]
squared = map(lambda x: x ** 2, numbers)
print(list(squared))  # [1, 4, 9, 16]

# filter
numbers = [1, 2, 3, 4, 5]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))  # [2, 4]

# reduce
from functools import reduce
numbers = [1, 2, 3, 4]
total = reduce(lambda x, y: x + y, numbers)
print(total)  # 10

# 대안
# 리스트 컴프리헨션
numbers = [1, 2, 3, 4]
# map 대체
squared = [x ** 2 for x in numbers]
# filter 대체
even_numbers = [x for x in numbers if x % 2 == 0]

# 제너레이터 표현식
numbers = range(1, 1000)  # 큰 범위
# map 대체
squared = (x ** 2 for x in numbers)
# filter 대체
even_numbers = (x for x in numbers if x % 2 == 0)