# main2.py
class MyClass:
    def __init__(self):
        print("MyClass instance created")

    def method(self):
        print("Method in MyClass")


print("Creating MyClass instance")
instance = MyClass()  # MyClass 인스턴스 생성
print("Calling method")
instance.method()  # 메서드 호출

'''
Creating MyClass instance
MyClass instance created
Calling method
Method in MyClass
'''