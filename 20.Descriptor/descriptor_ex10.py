class CustomMethod:
    def __get__(self, instance, owner):
        def wrapper(*args, **kwargs):
            print("Before method call")
            result = self.method(instance, *args, **kwargs)
            print("After method call")
            return result
        return wrapper

    def __set_name__(self, owner, name):
        self.name = name

    def method(self, instance, *args, **kwargs):
        print("Custom method called")


class MyClass:
    method = CustomMethod()


# 사용 예
obj = MyClass()
obj.method()
