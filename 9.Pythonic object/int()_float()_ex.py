class MyNumber:
    def __init__(self, value):
        self.value = value

    def __int__(self):
        return int(self.value)

    def __float__(self):
        return float(self.value)


num = MyNumber(42.7)

# 정수로 변환
print(int(num))    # 42

# 부동 소수점 숫자로 변환
print(float(num))  # 42.7


