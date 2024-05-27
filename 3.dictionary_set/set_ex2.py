# 기본적인 사용법
my_set = {1, 2, 3, 4, 5}
print(my_set)  # 출력 예시: {1, 2, 3, 4, 5}

# 빈 집합 생성
empty_set = set()
print(empty_set)  # 출력: set()

# 집합 리터럴과 연산
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# 합집합
union_set = a | b
print(union_set)  # 출력: {1, 2, 3, 4, 5, 6}

# 교집합
intersection_set = a & b
print(intersection_set)  # 출력: {3, 4}

# 차집합
difference_set = a - b
print(difference_set)  # 출력: {1, 2}

# 대칭 차집합
symmetric_difference_set = a ^ b
print(symmetric_difference_set)  # 출력: {1, 2, 5, 6}

# 기본 사용법
# {표현식 for 변수 in 반복가능객체 if 조건문}

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_numbers = {x for x in numbers if x % 2 == 0}
print(even_numbers)  # 출력: {2, 4, 6, 8}

words = ["apple", "banana", "cherry", "date"]
lengths = {len(word) for word in words}
print(lengths)  # 출력: {5, 6}

squared_numbers = {x**2 for x in range(10) if x**2 > 20}
print(squared_numbers)  # 출력: {25, 36, 49, 64, 81}