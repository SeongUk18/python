class NonOverriding:
    def __get__(self, instance, owner):
        return "NonOverriding descriptor value"


class MyClass:
    attr = NonOverriding()


# 사용 예
obj = MyClass()
print(obj.attr)  # "NonOverriding descriptor value" 출력

# 인스턴스 레벨에서 속성 덮어쓰기
obj.attr = "Instance attribute value"
print(obj.attr)  # "Instance attribute value" 출력

# 클래스 레벨에서 디스크립터 접근
print(MyClass.attr)  # "NonOverriding descriptor value" 출력
