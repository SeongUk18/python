class Overriding:
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name, "Overriding descriptor default value")

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name


class MyClass:
    attr = Overriding()


# 사용 예
obj = MyClass()
print(obj.attr)  # "Overriding descriptor default value" 출력

# 인스턴스 레벨에서 속성 설정
obj.attr = "Instance attribute value"
print(obj.attr)  # "Instance attribute value" 출력

# 클래스 레벨에서 디스크립터 접근
print(MyClass.attr)  # 디스크립터 객체 자체 출력
