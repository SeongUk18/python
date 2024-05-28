class MyClass:
    def __init__(self, value):
        self.value = value

    def show_value(self):
        print(self.value)


instance = MyClass(10)
instance.show_value()  # "10" 출력
