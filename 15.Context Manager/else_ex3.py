try:
    result = 10 / 2
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
else:
    print("계산이 성공적으로 완료되었습니다.")
    print("결과:", result)

# 결과:
# 계산이 성공적으로 완료되었습니다.
# 결과: 5.0

try:
    result = 10 / 0
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
else:
    print("계산이 성공적으로 완료되었습니다.")
    print("결과:", result)

# 결과:
# 0으로 나눌 수 없습니다.
