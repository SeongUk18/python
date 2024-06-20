# type을 사용한 동적 클래스 생성
MyClass = type('MyClass', (object,), {'attr': 100})

# MyClass 인스턴스 생성
instance = MyClass()
print(instance.attr)  # 출력: 100
