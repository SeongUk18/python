import inspect

def sample_function(a, b=2, *args, c=3, **kwargs):
    pass

sig = inspect.signature(sample_function)
print(sig)
for name, param in sig.parameters.items():
    print(f"Name: {name}")
    print(f"  Kind: {param.kind}")
    print(f"  Default: {param.default}")
    print(f"  Annotation: {param.annotation}")


import inspect

def foo(a, b: int = 42, *args, c: float = 3.14, d, **kwargs):
    pass

sig = inspect.signature(foo)
print("Function signature:", sig)
# Function signature: (a, b: int = 42, *args, c: float = 3.14, d, **kwargs)

for name, param in sig.parameters.items():
    print(f"Parameter Name: {name}")
    # Parameter Name: a
    # Parameter Name: b
    print(f"  Type: {param.annotation}")
    # Type: <class 'inspect._empty'>
    # Type: <class 'int'>
    print(f"  Kind: {param.kind}")
    # Kind: POSITIONAL_OR_KEYWORD
    # Kind: POSITIONAL_OR_KEYWORD
    print(f"  Default: {param.default if param.default is not inspect.Parameter.empty else 'No default'}")
    # Default: No default
    # Default: 42