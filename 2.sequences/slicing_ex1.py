numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 인덱스 2부터 5까지 요소를 슬라이싱 (5는 포함되지 않음)
print(numbers[2:5])  # [2, 3, 4]

# 리스트의 처음부터 인덱스 5까지 요소를 슬라이싱 (5는 포함되지 않음)
print(numbers[:5])  # [0, 1, 2, 3, 4]

# 인덱스 5부터 리스트 끝까지 요소를 슬라이싱
print(numbers[5:])  # [5, 6, 7, 8, 9]

# 전체 리스트를 슬라이싱 (복사)
print(numbers[:])  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 간격(스텝)을 2로 설정하여 인덱스 0부터 2씩 증가하며 슬라이싱
print(numbers[::2])  # [0, 2, 4, 6, 8]

# 리스트를 역순으로 슬라이싱
print(numbers[::-1])  # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# 문자열 슬라이싱
greeting = "Hello, World!"
print(greeting[7:12])  # World

# 튜플 슬라이싱
tuple_data = (0, 1, 2, 3, 4, 5)
print(tuple_data[2:4])  # (2, 3)

my_slice = slice(1, 5, 2)  # 인덱스 1부터 5까지, 간격 2로 요소를 선택

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
result = numbers[my_slice]
print(result)  # [1, 3]

# 동일한 슬라이스를 다른 리스트에 적용
more_numbers = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
another_result = more_numbers[my_slice]
print(another_result)  # [11, 13]

# 문자열에 적용
text = "Hello, World!"
text_slice = text[my_slice]
print(text_slice)  # "el"
