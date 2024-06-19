class OverridingWithoutGet:
    def __set__(self, instance, value):
        print(f"Setting {value}")
        instance.__dict__['attr'] = value

    def __delete__(self, instance):
        print("Deleting attribute")
        del instance.__dict__['attr']


class MyClass:
    attr = OverridingWithoutGet()


# 사용 예
obj = MyClass()
obj.attr = 10  # __set__ 호출, "Setting 10" 출력
print(obj.attr)  # 인스턴스의 __dict__에서 직접 값 가져옴, 10 출력
del obj.attr  # __delete__ 호출, "Deleting attribute" 출력
