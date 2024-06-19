class Descriptor:
    def __get__(self, instance, owner):
        return self

    def my_method(self):
        return "Descriptor method"


class MyClass:
    attr = Descriptor()


# 사용 예
obj = MyClass()
print(obj.attr.my_method())  # "Descriptor method" 출력 (정상 동작)

# 인스턴스 레벨에서 속성 설정
obj.attr = "Instance value"
print(obj.attr)  # "Instance value" 출력 (디스크립터 가려짐)

# 디스크립터의 메서드 호출 시도
try:
    print(obj.attr.my_method())  # AttributeError 발생
except AttributeError as e:
    print(e)  # "'str' object has no attribute 'my_method'" 출력

# 클래스 레벨에서 디스크립터 접근
print(MyClass.attr.my_method())  # "Descriptor method" 출력 (클래스 레벨 접근)
