class CustomClass:
    def __init__(self, value):
        self._value = value

    def __getattr__(self, name):
        if name == 'value':
            return self._value
        raise AttributeError(f"'CustomClass' object has no attribute '{name}'")

    def __setattr__(self, name, value):
        if name == 'value':
            if value < 0:
                raise ValueError("Value must be non-negative")
            self._value = value
        else:
            super().__setattr__(name, value)

    def __delattr__(self, name):
        if name == 'value':
            print(f"Deleting {name}")
            super().__delattr__(f'_{name}')
        else:
            super().__delattr__(name)

    def __dir__(self):
        return ['value', '_value']


# 예제 사용
obj = CustomClass(10)
print(obj.value)  # 10

obj.value = 20
print(obj.value)  # 20

try:
    obj.value = -10
except ValueError as e:
    print(e)  # Value must be non-negative

del obj.value  # Deleting value
