# __str__(), __repr__()
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def __repr__(self):
        return f"Point({self.x}, {self.y})"


point = Point(1, 2)
print(point) # Point(1, 2)
print(repr(point)) # Point(1, 2)


# 덕 타이핑과 이터레이터
class IterableContainer:
    def __init__(self, items):
        self.items = items

    def __iter__(self):
        return iter(self.items)


container = IterableContainer([1, 2, 3])
for item in container:
    print(item) # 1 2 3


# 예외 처리
class Calculator:
    def divide(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return "Cannot divide by zero"

calc = Calculator()
print(calc.divide(10, 2)) # 5.0
print(calc.divide(10, 0)) # Cannot divide by zero