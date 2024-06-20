class MyMeta(type):
    def __new__(cls, name, bases, dct):
        dct['added_attr'] = 'I am added by MyMeta'
        return super().__new__(cls, name, bases, dct)


class MyClass(metaclass=MyMeta):
    pass


# 클래스 객체를 통해 추가된 속성 접근
print(MyClass.added_attr)  # 출력: I am added by MyMeta

# 인스턴스 생성
instance = MyClass()
print(instance.added_attr)  # 출력: I am added by MyMeta
