class CustomNumber:
    def __init__(self, value):
        self.value = value

    # 객체의 문자열 표현
    def __repr__(self):
        return f"CustomNumber({self.value})"

    # 덧셈 연산
    def __add__(self, other):
        return CustomNumber(self.value + other.value)

    # 곱셈 연산
    def __mul__(self, other):
        return CustomNumber(self.value * other.value)


# CustomNumber 인스턴스 생성 및 연산 예시
num1 = CustomNumber(5)
num2 = CustomNumber(3)

# 덧셈 연산
print(num1 + num2)  # CustomNumber(8)

# 곱셈 연산
print(num1 * num2)  # CustomNumber(15)


# __str__() vs __repr__()
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __repr__(self):
        return f"Date({self.year}, {self.month}, {self.day})"

    def __str__(self):
        return f"{self.year}-{self.month}-{self.day}"

d = Date(2020, 1, 5)
print(repr(d))  # Date(2020, 1, 5)
print(str(d))   # 2020-1-5
print(d)        # __str__ 메소드의 결과인 '2020-1-5' 출력, __str__이 없으면 __repr__의 결과 출력
