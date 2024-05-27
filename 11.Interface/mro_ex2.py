class X:
    def method(self):
        print("X.method")


class Y(X):
    def method(self):
        print("Y.method")


class Z(X):
    def method(self):
        print("Z.method")


class A(Y, Z):
    def method(self):
        print("A.method")


print(A.__mro__)
# 출력: (<class '__main__.A'>, <class '__main__.Y'>, <class '__main__.Z'>, <class '__main__.X'>, <class 'object'>)
