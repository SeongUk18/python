class Parent:
    class_attr = "I am a class attribute in Parent"

    def __init__(self):
        self.instance_attr = "I am an instance attribute in Parent"


class Child(Parent):
    class_attr = "I am a class attribute in Child"

    def __init__(self):
        super().__init__()
        self.instance_attr = "I am an instance attribute in Child"


parent = Parent()
child = Child()

# 클래스 속성 접근
print(Parent.class_attr)  # I am a class attribute in Parent
print(Child.class_attr)   # I am a class attribute in Child

# 인스턴스 속성 접근
print(parent.instance_attr)  # I am an instance attribute in Parent
print(child.instance_attr)   # I am an instance attribute in Child
