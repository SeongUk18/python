import reprlib
from functools import reduce
import operator


class Vector:
    def __init__(self, *args):
        self._values = list(args)

    def __len__(self):
        return len(self._values)

    def __getitem__(self, index):
        if isinstance(index, slice):
            # 슬라이스 객체를 처리
            return Vector(*self._values[index])
        elif isinstance(index, int):
            # 인덱스를 처리
            return self._values[index]
        else:
            # 슬라이스나 인덱스가 아닌 경우 예외 처리
            raise TypeError("Invalid argument type.")

    def __setitem__(self, index, value):
        self._values[index] = value

    def __iter__(self):
        return iter(self._values)

    def __repr__(self):
        return f"Vector({reprlib.repr(self._values)})"

    def __add__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        if len(self) != len(other):
            raise ValueError("Vectors must be the same length")
        return Vector(*[a + b for a, b in zip(self, other)])

    def __sub__(self, other):
        if not isinstance(other, Vector):
            raise NotImplemented
        if len(self) != len(other):
            raise ValueError("Vectors must be the same length")
        return Vector(*[a - b for a, b in zip(self, other)])

    def __mul__(self, scalar):
        if not isinstance(scalar, (int, float)):
            return NotImplemented
        return Vector(*[scalar * v for v in self])

    def __rmul__(self, scalar):
        return self.__mul__(scalar)

    def __getattr__(self, name):
        if name == 'magnitude':
            return sum(x**2 for x in self._values) ** 0.5
        raise AttributeError(f"'Vector' object has no attribute '{name}'")

    def __hash__(self):
        # 해시 값을 계산할 때 reduce()와 operator.xor 을 사용한다.
        return reduce(operator.xor, map(hash, self._values), 0)

    def __eq__(self, other):
        if not isinstance(other, Vector):
            return False
        # 길이 비교 최적화
        if len(self) != len(other):
            return False
        # 해시값 비교 최적화
        if hash(self) != hash(other):
            return False
        # 모든 요소 비교
        return self._values == other._values


v1 = Vector(1, 2, 3, 4, 5)
v2 = Vector(1, 2, 3, 4, 5)
v3 = Vector(1, 2, 3, 4, 6)

print(v1 == v2)  # True
print(v1 == v3)  # False

