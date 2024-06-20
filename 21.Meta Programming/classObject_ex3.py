def create_class(class_name, base_classes, attributes):
    return type(class_name, base_classes, attributes)


# 동적 클래스 생성
MyDynamicClass = create_class('MyDynamicClass', (object,), {'attr': 100, 'method': lambda self: f"Method called with {self.attr}"})

# 인스턴스 생성
dynamic_instance = MyDynamicClass()
print(dynamic_instance.attr)  # 출력: 100
print(dynamic_instance.method())  # 출력: Method called with 100
