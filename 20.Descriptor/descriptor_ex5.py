class NonOverridingDescriptor:
    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name, None)

    def __set_name__(self, owner, name):
        self.name = name


class MyClass:
    attr = NonOverridingDescriptor()


obj = MyClass()
obj.attr = 10  # 인스턴스의 __dict__에 직접 설정됨
print(obj.attr)  # 인스턴스의 __dict__에서 직접 가져옴, 10 출력

# 디스크립터로 설정되지 않은 속성 접근 시 디스크립터의 __get__ 호출
del obj.__dict__['attr']
print(obj.attr)  # __get__ 호출, None 출력
