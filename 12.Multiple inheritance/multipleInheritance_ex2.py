class A:
    def method(self):
        print("Method from A")


class B(A):
    def method(self):
        print("Method from B")


class C(A):
    def method(self):
        print("Method from C")


class D(B, C):
    pass


d = D()
d.method()  # Method from B


print(D.mro())