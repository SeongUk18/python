# 두 개의 인자로 생성
c1 = complex(2, 3)
print(c1)  # (2+3j)

# 하나의 인자로 생성 (문자열)
c2 = complex("2+3j")
print(c2)  # (2+3j)

# 하나의 인자로 생성 (다른 숫자 형식)
c3 = complex(2)
print(c3)  # (2+0j)


class MyNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __complex__(self):
        return complex(self.real, self.imag)


num = MyNumber(2, 3)

# complex() 함수를 사용하여 MyNumber 인스턴스를 복소수로 변환
c = complex(num)
print(c)  # (2+3j)
