class BaseClass:
    def show_message(self):
        print("Message from BaseClass")


class SubClass(BaseClass):
    def show_message(self):
        super().show_message()
        print("Message from SubClass")


instance = SubClass()
instance.show_message()
# Message from BaseClass
# Message from SubClass
