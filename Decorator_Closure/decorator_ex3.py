def my_decorator(func):
    print("Decorator is being applied.")
    def wrapper():
        print("Before the function is called.")
        func()
        print("After the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

print("Finished defining functions.")
say_hello()

"""
Decorator is being applied.
Finished defining functions.
Before the function is called.
Hello!
After the function is called.
"""