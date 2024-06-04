import itertools


# 등차수열 생성 함수
def arithmetic_sequence(start, step):
    return itertools.count(start, step)


# 예제 사용
start = 0  # 시작 값
step = 2  # 공차

sequence = arithmetic_sequence(start, step)

# 등차수열의 처음 10개 항 출력
for _ in range(10):
    print(next(sequence))

'''
0
2
4
6
8
10
12
14
16
18
'''