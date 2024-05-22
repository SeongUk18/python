import reprlib


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

    def __eq__(self, other):
        if not isinstance(other, Vector):
            return False
        return self._values == other._values

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


v = Vector(3, 4)
print(v.magnitude)  # 5.0, 벡터의 크기를 동적으로 계산하여 반환

# print(v.nonexistent)  # AttributeError 발생: 'Vector' object has no attribute 'nonexistent'
