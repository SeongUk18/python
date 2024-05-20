from datetime import date


class Date:
    def __init__(self, year, month, day):
        self.date = date(year, month, day)

    def __int__(self):
        epoch = date(1970, 1, 1)
        delta = self.date - epoch
        return delta.days

    def __float__(self):
        epoch = date(1970, 1, 1)
        delta = self.date - epoch
        return float(delta.days)


d = Date(2023, 5, 20)

# 정수로 변환
print(int(d))    # 19497 특정 기준 날짜(1970-01-01)로부터의 일수

# 부동 소수점 숫자로 변환
print(float(d))  # 19497.0 특정 기준 날짜(1970-01-01)로부터의 일수 (부동 소수점 형식)