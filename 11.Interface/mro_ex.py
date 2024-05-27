class A:
    def method(self):
        print("A.method")


class B(A):
    def method(self):
        print("B.method")


class C(A):
    def method(self):
        print("C.method")


class D(B, C):
    def method(self):
        print("D.method")


print(D.__mro__)
# 출력: (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)

# 또는
print(D.mro())
# 출력: [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
