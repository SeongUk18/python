# 기본 예
t = (1, 2)
a, b = t
print(a)  # 1 출력
print(b)  # 2 출력

# 변수 값 교환
a, b = b, a

# 병렬 할당과 튜플 언패킹
t = (1, 2, 3)
a, b, c = t

# 확장된 언패킹
t = (1, 2, 3, 4, 5)
a, *b, c = t
print(a)  # 1 출력
print(b)  # [2, 3, 4] 출력
print(c)  # 5 출력


# 언패킹을 통한 반환값 받기
def calc_operations(x, y):
    return x + y, x - y  # 합과 차를 튜플 형태로 반환


sum_result, diff_result = calc_operations(10, 5)
print("Sum:", sum_result)  # Sum: 15
print("Difference:", diff_result)  # Difference: 5

