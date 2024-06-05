count = 0
while count < 5:
    if count == 3:
        break
    count += 1
else:
    print("반복문이 중단되지 않았습니다.")

# 결과: (출력 없음, 3에서 break로 종료)


count = 0
while count < 5:
    print(count)
    count += 1
else:
    print("반복문이 중단되지 않았습니다.")

# 결과:
# 0
# 1
# 2
# 3
# 4
# 반복문이 중단되지 않았습니다.
