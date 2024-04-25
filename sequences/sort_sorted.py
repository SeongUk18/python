numbers = [3, 1, 4, 1, 5, 9, 2, 6]
numbers.sort()
print(numbers)  # [1, 1, 2, 3, 4, 5, 6, 9]

numbers = [3, 1, 4, 1, 5, 9, 2, 6]
sorted_numbers = sorted(numbers)
print(sorted_numbers)  # [1, 1, 2, 3, 4, 5, 6, 9]
print(numbers)  # [3, 1, 4, 1, 5, 9, 2, 6] 원본은 변경되지 않음

words = ["banana", "apple", "cherry"]
sorted_words = sorted(words, key=len)  # 길이에 따라 정렬
print(sorted_words)  # ['apple', 'banana', 'cherry']