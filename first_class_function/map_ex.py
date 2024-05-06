# 예제 1: 숫자 리스트의 각 요소를 제곱
numbers = [1, 2, 3, 4, 5]
squared = map(lambda x: x ** 2, numbers)
print(list(squared))  # 결과: [1, 4, 9, 16, 25]

# 예제 2: 문자열 리스트를 대문자로 변환
names = ["alice", "bob", "charlie"]
upper_names = map(str.upper, names)
print(list(upper_names))  # 결과: ['ALICE', 'BOB', 'CHARLIE']

# 예제 3: 각 튜플의 첫 번째 요소에 연산 적용
data = [(1, 'apple'), (2, 'banana'), (3, 'cherry')]
incremented_data = map(lambda x: (x[0] + 1, x[1]), data)
print(list(incremented_data))  # 결과: [(2, 'apple'), (3, 'banana'), (4, 'cherry')]

