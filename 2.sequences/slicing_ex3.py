numbers = [0, 1, 2, 3, 4, 5]
numbers[2:4] = [9, 9]  # 인덱스 2부터 3까지의 요소를 [9, 9]로 변경
print(numbers)  # [0, 1, 9, 9, 4, 5] 출력

numbers = [0, 1, 2, 3, 4, 5]
numbers[2:4] = []  # 인덱스 2부터 3까지의 요소를 삭제
print(numbers)  # [0, 1, 4, 5] 출력

numbers = [0, 1, 2, 3, 4, 5]
numbers[2:2] = [8, 9]  # 인덱스 2의 위치에 [8, 9] 삽입
print(numbers)  # [0, 1, 8, 9, 2, 3, 4, 5] 출력

numbers = [0, 1, 2, 3, 4, 5]
del numbers[1:4]  # 인덱스 1부터 3까지의 요소를 삭제
print(numbers)  # [0, 4, 5] 출력


list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined_list = list1 + list2  # [1, 2, 3, 4, 5, 6]

rows = 3
cols = 2
wrong_matrix = [[0] * cols] * rows  # 이 방법은 문제를 일으킬 수 있음

wrong_matrix[0][0] = 1
print(wrong_matrix)  # 출력: [[1, 0], [1, 0], [1, 0]]

# 올바른 방법
correct_matrix = [[0] * cols for _ in range(rows)]
correct_matrix[0][0] = 1
print(correct_matrix)  # 출력: [[1, 0], [0, 0], [0, 0]]


numbers = [1, 2, 3]
numbers += [4, 5]  # 리스트에 [4, 5] 추가
print(numbers)  # 출력: [1, 2, 3, 4, 5]

numbers = [1, 2, 3]
numbers *= 2  # 리스트를 2번 반복
print(numbers)  # 출력: [1, 2, 3, 1, 2, 3]