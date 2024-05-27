def make_multiplier(x):
    def multiplier(y):
        return x * y
    return multiplier

# 클로저 생성
double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))  # 10
print(triple(5))  # 15