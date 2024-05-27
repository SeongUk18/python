from decorator_module import log_function_data

@log_function_data
def add(a, b):
    """두 숫자를 더하는 함수"""
    return a + b

@log_function_data
def multiply(a, b):
    """두 숫자를 곱하는 함수"""
    return a * b

# 함수 호출
add(3, 4)
"""
Function 'add' called with arguments (3, 4) and kwargs {}
Returned value: 7
Execution time: 0.000000 seconds
"""
multiply(4, 5)
"""
Function 'multiply' called with arguments (4, 5) and kwargs {}
Returned value: 20
Execution time: 0.000000 seconds
"""