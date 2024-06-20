def create_class(class_name):
    class DynamicClass:
        def __init__(self, value):
            self.value = value

        def display(self):
            print(f"{class_name}: {self.value}")

    return DynamicClass


# 클래스 팩토리 호출
MyClass = create_class("MyClass")

# 클래스 인스턴스 생성
instance = MyClass("Hello, World!")
instance.display()  # 출력: MyClass: Hello, World!
