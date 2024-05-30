import numbers


class Vector:
    def __init__(self, *components):
        self.components = list(components)

    def __neg__(self):
        """부호 변경: -벡터"""
        return Vector(*[-c for c in self.components])

    def __abs__(self):
        """벡터의 절대값 (유클리드 거리)"""
        return sum(c ** 2 for c in self.components) ** 0.5

    def __invert__(self):
        """비트 반전: ~벡터 (정수로 가정)"""
        return Vector(*[~c for c in self.components])

    def __add__(self, other):
        """벡터 덧셈: 길이가 다른 벡터도 더할 수 있도록 구현"""
        if isinstance(other, Vector):
            max_len = max(len(self.components), len(other.components))
            new_components = [
                (self.components[i] if i < len(self.components) else 0) +
                (other.components[i] if i < len(other.components) else 0)
                for i in range(max_len)
            ]
            return Vector(*new_components)
        else:
            # 다른 타입의 객체와 덧셈
            return NotImplemented

    def __radd__(self, other):
        """벡터 덧셈: other + 벡터"""
        return self.__add__(other)

    def __mul__(self, other):
        """스칼라 곱: 벡터 * 스칼라"""
        if isinstance(other, numbers.Real):
            new_components = [c * other for c in self.components]
            return Vector(*new_components)
        else:
            return NotImplemented

    def __rmul__(self, other):
        """스칼라 곱: 스칼라 * 벡터"""
        return self.__mul__(other)

    def __repr__(self):
        return f"Vector({', '.join(map(str, self.components))})"


# 사용 예시
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5)
v3 = v1 + v2
print(v3)  # Vector(5, 7, 3)

v4 = Vector(1, 2)
v5 = Vector(3, 4, 5, 6)
v6 = v4 + v5
print(v6)  # Vector(4, 6, 5, 6)

print(-v1)  # Vector(-1, -2, -3)
print(abs(v1))  # 3.7416573867739413
print(~Vector(3, -4))  # Vector(-4, 3)

# __radd__ 예시
v7 = Vector(1, 2, 3)
v8 = Vector(4, 5, 6)
print(v7 + v8)  # Vector(5, 7, 9)
print(v8 + v7)  # Vector(5, 7, 9)

# 스칼라 곱 예시
v9 = Vector(1, 2, 3)
v10 = v9 * 3
print(v10)  # Vector(3, 6, 9)
v11 = 3 * v9
print(v11)  # Vector(3, 6, 9)
