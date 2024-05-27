# repr
class MyClass:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"MyClass({self.value})"


obj = MyClass(42)
print(repr(obj))# MyClass(42)


# str
class MyClass2:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"MyClass({self.value})"


obj2 = MyClass2(42)
print(obj2)# MyClass(42)
