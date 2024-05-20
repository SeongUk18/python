class Parent:
    def greet(self):
        print("Hello from Parent")


class Child(Parent):
    def greet(self):
        print("Hello from Child")


parent = Parent()
child = Child()

parent.greet()  # Hello from Parent
child.greet()   # Hello from Child
