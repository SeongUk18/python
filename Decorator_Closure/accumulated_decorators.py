def decorator1(func):
    def wrapper():
        print("Decorator 1 before call")
        result = func()
        print("Decorator 1 after call")
        return result
    return wrapper

def decorator2(func):
    def wrapper():
        print("Decorator 2 before call")
        result = func()
        print("Decorator 2 after call")
        return result
    return wrapper

@decorator1
@decorator2
def say_hello():
    print("Hello!")

say_hello()
"""
Decorator 1 before call
Decorator 2 before call
Hello!
Decorator 2 after call
Decorator 1 after call
"""