def add(x: int, y: int) -> int:
    return x + y

def greet(name: str) -> str:
    return f"Hello, {name}!"

print(greet.__annotations__)
# {'name': <class 'str'>, 'return': <class 'str'>}
