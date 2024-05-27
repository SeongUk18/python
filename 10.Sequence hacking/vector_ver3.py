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


v1 = Vector(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(v1)          # Vector([1, 2, 3, 4, 5, 6, ...])
print(v1[2:7])     # Vector([3, 4, 5, 6, 7])
print(v1[::-1])    # Vector([10, 9, 8, 7, 6, 5, ...])
