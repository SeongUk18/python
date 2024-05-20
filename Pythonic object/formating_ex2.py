class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __format__(self, format_spec):
        if format_spec == "":
            format_spec = "({x}, {y})" # 기본 포맷

        if format_spec == "repr":
            return f"Point(x={self.x}, y={self.y})"
        elif format_spec == "str":
            return f"({self.x}, {self.y})"
        else:
            return format_spec.format(x=self.x, y=self.y)


p = Point(1, 2)

print(format(p)) # 기본 포맷: (1, 2)
print(format(p, "repr")) # repr 포맷: Point(x=1, y=2)
print(format(p, "str")) # str 포맷: (1, 2)
print(format(p, "{x} - {y}")) # 사용자 정의 포맷: 1 - 2

# f-string 사용한 예제
print(f"{p}") # (1, 2)
print(f"{p:repr}") # Point(x=1, y=2)
print(f"{p:str}") # (1, 2)
print(f"{p:{p.x}/{p.y}}") # 1/2
