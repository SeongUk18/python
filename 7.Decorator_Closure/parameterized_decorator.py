from functools import wraps

def logger(level):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if level == "high":
                print(f"[HIGH LEVEL] Running {func.__name__} with arguments {args} {kwargs}")
            elif level == "medium":
                print(f"[MEDIUM LEVEL] Running {func.__name__}")
            else:
                print(f"[LOW LEVEL] Running function")

            result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@logger(level="high")
def add(a, b):
    return a + b

@logger(level="low")
def subtract(a, b):
    return a - b

print(add(2, 3))
print(subtract(5, 3))

"""
[HIGH LEVEL] Running add with arguments (2, 3) {}
5
[LOW LEVEL] Running function
2
"""