class MyClass:
    def my_method(self):
        print("This is a method")


# 인스턴스 생성
instance = MyClass()

# 바인딩된 메소드 호출
instance.my_method()  # "This is a method" 출력

# 바인딩되지 않은 메소드 접근
unbound_method = MyClass.my_method
unbound_method(instance)  # "This is a method" 출력
