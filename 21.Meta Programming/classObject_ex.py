class MyClass:
    class_attr = 42

    def __init__(self, value):
        self.instance_attr = value

    def instance_method(self):
        return f"Instance method called with {self.instance_attr}"

    @classmethod
    def class_method(cls):
        return f"Class method called with {cls.class_attr}"


# 클래스 객체를 통해 속성 접근 및 메서드 호출
print(MyClass.class_attr)  # 출력: 42
print(MyClass.class_method())  # 출력: Class method called with 42

# 인스턴스 생성
instance = MyClass(100)
print(instance.instance_method())  # 출력: Instance method called with 100
