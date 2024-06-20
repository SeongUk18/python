def create_custom_class(class_name, base_class, methods):
    class CustomClass(base_class):
        def __init__(self, value):
            self.value = value

    for method_name, method in methods.items():
        setattr(CustomClass, method_name, method)

    CustomClass.__name__ = class_name
    return CustomClass


# 기본 클래스 정의
class BaseClass:
    def base_method(self):
        print("Base method")


# 추가할 메서드 정의
methods = {
    "custom_method": lambda self: print(f"Custom method in {self.value}")
}

# 클래스 팩토리 호출
CustomClass = create_custom_class("CustomClass", BaseClass, methods)

# 클래스 인스턴스 생성
instance = CustomClass("MyCustomClass")
instance.base_method()  # 출력: Base method
instance.custom_method()  # 출력: Custom method in MyCustomClass
