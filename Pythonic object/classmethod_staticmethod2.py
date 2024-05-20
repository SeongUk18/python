class Example:
    count= 0

    def __init__(self):
        Example.count += 1

    @classmethod
    def get_count(cls):
        return cls.count

    @staticmethod
    def is_positive(number):
        return number > 0


# 클레스 메서드 호출
print(Example.get_count()) # 0

# 인스턴스 생성
ex1 = Example()
ex2 = Example()

# 클레스 메서드 호출
print(Example.get_count()) # 2

# 정적 메소드 호출
print(Example.is_positive(10)) # True
print(Example.is_positive(-5)) # False
