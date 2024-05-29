class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __neg__(self):
        """부호 변경: -벡터"""
        return Vector(-self.x, -self.y)

    def __abs__(self):
        """벡터의 절대값 (유클리드 거리)"""
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __invert__(self):
        """비트 반전: ~벡터 (정수로 가정)"""
        return Vector(~self.x, ~self.y)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"


# 사용 예시
v = Vector(3, -4)
print(-v)     # Vector(-3, 4)
print(abs(v)) # 5.0 (3-4-5 삼각형의 피타고라스 거리)
print(~v)     # Vector(-4, 3)
