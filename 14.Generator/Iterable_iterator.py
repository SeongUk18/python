my_list = [1, 2, 3]
iterator = iter(my_list)

print(next(iterator))  # 출력: 1
print(next(iterator))  # 출력: 2
print(next(iterator))  # 출력: 3
# 다음 호출은 StopIteration 예외를 발생시킨다.
