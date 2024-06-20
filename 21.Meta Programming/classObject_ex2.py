# 동적 클래스 생성
DynamicClass = type('DynamicClass', (object,), {'class_attr': 42, 'class_method': lambda cls: f"Class method called with {cls.class_attr}"})

# 클래스 객체를 통해 속성 접근 및 메서드 호출
print(DynamicClass.class_attr)  # 출력: 42
print(DynamicClass.class_method(DynamicClass))  # 출력: Class method called with 42

# 인스턴스 생성
dynamic_instance = DynamicClass()