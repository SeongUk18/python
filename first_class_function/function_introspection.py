import inspect

# 함수 정의
def sample_function(param1, param2="default"):
    """This is a sample function to demonstrate introspection."""
    return param1 + param2

# dir()을 사용하여 속성 및 메서드 목록 조회
print("Attributes and Methods:", dir(sample_function))
# Attributes and Methods: ['__annotations__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__globals__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__kwdefaults__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']

# type()과 id()를 사용하여 함수의 타입과 메모리 주소 출력
print("Type of the function:", type(sample_function))
# Type of the function: <class 'function'>
print("Memory address of the function:", id(sample_function))
# Memory address of the function: 140456780318400  # 메모리 주소는 실행할 때마다 달라질 수 있음.

# inspect 모듈을 사용하여 독스트링, 소스 코드, 시그니처 조회
print("Documentation:", inspect.getdoc(sample_function))
# Documentation: This is a sample function to demonstrate introspection.
print("Source Code:\n", inspect.getsource(sample_function))
# Source Code:
# def sample_function(param1, param2="default"):
#     """This is a sample function to demonstrate introspection."""
#     return param1 + param2
print("Signature:", inspect.signature(sample_function))
# Signature: (param1, param2='default')

# __doc__, __name__, __module__ 속성 조회
print("Docstring:", sample_function.__doc__)
# Docstring: This is a sample function to demonstrate introspection.
print("Function Name:", sample_function.__name__)
# Function Name: sample_function
print("Module Name:", sample_function.__module__)
# Module Name: __main__