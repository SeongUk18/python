import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __format__(self, format_spec):
        if format_spec.endswith("p"):
            # 극좌표 포맷
            r = math.sqrt(self.x ** 2 + self.y ** 2)
            theta = math.degrees(math.atan2(self.y, self.x))
            format_spec = format_spec[:-1]  # 'p' 제거
            return f"({r:{format_spec}}, {theta:{format_spec}}°)"
        elif format_spec == "":
            # 기본 포맷
            format_spec = "({x}, {y})"

        # 기본 및 사용자 정의 포맷
        return format_spec.format(x=self.x, y=self.y)


# 예제 사용
p = Point(3, 4)

print(format(p))                # 기본 포맷: (3, 4)
print(format(p, ".2f"))         # 기본 포맷, 2소수점 자리: (3.00, 4.00)
print(format(p, ".2fp"))        # 극좌표 포맷, 2소수점 자리: (5.00, 53.13°)

# f-string을 사용한 예제
print(f"{p}")                   # 기본 포맷: (3, 4)
print(f"{p:.2f}")               # 기본 포맷, 2소수점 자리: (3.00, 4.00)
print(f"{p:.2fp}")              # 극좌표 포맷, 2소수점 자리: (5.00, 53.13°)