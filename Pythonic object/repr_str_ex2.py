class MyClass:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"MyClass({self.value!r})"

    def __str__(self):
        return f"Value is {self.value}"


obj = MyClass(42)
print(str(obj)) # Value is 42
print(repr(obj)) # MyClass(42)
