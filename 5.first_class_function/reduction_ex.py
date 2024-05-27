from functools import reduce

numbers = [1, 2, 3, 4, 5]
total_sum = reduce(lambda x, y: x + y, numbers)
print(total_sum)  # 15

# reduce
def add(x, y):
    return x + y

numbers = [1, 2, 3, 4, 5]
result = reduce(add, numbers)  # 15

# sum
numbers = [1, 2, 3, 4, 5]
total = sum(numbers)  # 15

# min, max
numbers = [5, 3, 9, 1, 10]
minimum = min(numbers)  # 1
maximum = max(numbers)  # 10

# all, any
conditions = [True, False, True]
all_true = all(conditions)  # False
any_true = any(conditions)  # True