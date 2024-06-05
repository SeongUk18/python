for i in range(5):
    if i == 3:
        break
else:
    print("반복문이 중단되지 않았습니다.")

# 결과: (출력 없음, 3에서 break로 종료)

for i in range(5):
    print(i)
else:
    print("반복문이 중단되지 않았습니다.")

# 결과:
# 0
# 1
# 2
# 3
# 4
# 반복문이 중단되지 않았습니다.
