class A:
    def method(self):
        print("Method from A")


class B(A):
    def method(self):
        print("Method from B")
        super().method()


class C(A):
    def method(self):
        print("Method from C")
        super().method()


class D(B, C):
    def method(self):
        print("Method from D")
        super().method()


d = D()
d.method()
'''
Method from D
Method from B
Method from C
Method from A
'''