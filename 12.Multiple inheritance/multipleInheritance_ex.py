class Parent1:
    def method1(self):
        print("Method from Parent1")


class Parent2:
    def method2(self):
        print("Method from Parent2")


class Child(Parent1, Parent2):
    pass


child = Child()
child.method1()  # Parent1의 method1 호출
child.method2()  # Parent2의 method2 호출
