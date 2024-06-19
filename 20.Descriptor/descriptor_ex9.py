class MyClass:
    def method(self):
        print("Method called")


# 사용 예
obj = MyClass()
bound_method = obj.method
bound_method()  # "Method called" 출력

# 언바인딩 메서드는 더 이상 존재하지 않지만, 클래스에서 직접 호출하면 함수 객체가 반환된다.
unbound_method = MyClass.method
unbound_method(obj)  # "Method called" 출력
