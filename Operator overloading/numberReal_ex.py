import numbers

# 실수 검사 예시
print(isinstance(3.14, numbers.Real))  # True
print(isinstance(2, numbers.Real))     # True (정수는 실수의 하위 집합)
print(isinstance(1 + 2j, numbers.Real))  # False (복소수는 실수가 아님)
print(isinstance(3.0, numbers.Real))   # True (float 타입)
